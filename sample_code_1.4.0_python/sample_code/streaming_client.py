# -*- coding: utf-8 -*-
# coding=utf-8
import hyper
import sys
import getopt
import util
import io
import os
import json

ALL = 0
CAPTURE = 1
RETRIEVE = 2

class StupidFlowControlManager(hyper.http20.window.BaseFlowControlManager):
    def increase_window_size(self, frame_size):
        return 2147483647 -self.window_size

class StreamingClient:
    # 初始化
    # mode: 收图模式(抓拍/比对)
    # url: 服务器地址, e.g: 192.168.2.80
    # port: 端口
    def __init__(self, mode, url, **kwargs):
        self.conn = hyper.HTTP20Connection(url, 17332, window_manager=StupidFlowControlManager)
        path = '/face/v1/face_results'
        self.mode = mode

        # 建立连接
        self.conn.request('GET', path)
        # 获取response
        self.response = self.conn.get_response()
        # 在headers中拿到write_schema, 用于反序列化
        self.write_schema = b','.join(
            self.response.headers.get('x-kassq-schema')).decode()
        self.save_scene = kwargs.get('save_scene')
        self.save_feature = kwargs.get('save_feature')
        self.save_face = kwargs.get('save_face')
        self.directory = kwargs.get('directory')
        self.count = 0

    def receive(self):
        # 每个包的前4个byte是标识这个包的大小, 大端表示
        read = self.response.read(4)
        package_len = int.from_bytes(read, byteorder='big')
        print(read)
        print(package_len)
        print("====")
        if package_len <= 0:
            return
        self.count += 1
        # 读取一个数据包
        data = self.response.read(package_len)
        # 处理收到的数据
        self.result_handler(data)

    # 处理人像结果
    def result_handler(self, data):
        # 反序列化
        with io.BytesIO(data) as f:
            datum = util.read_avro(util.RESULT_SCHEMA,
                                   self.write_schema, f)

        # 如果收到的图的类型与期望不一致则跳过
        if datum['result_type'] == 'Capture' and self.mode == RETRIEVE:
            return

        if datum['result_type'] == 'Retrieval' and self.mode == CAPTURE:
            return

        print('Receive {} {} Packages'.format(self.count, datum['result_type']))

        target_path = None
        extra_meta = {}
        if len(datum['face']['extra_meta']) != 0 and self.directory is not None:
            extra_meta = json.loads(datum['face']['extra_meta'])
            save_id = extra_meta['channel_id']
            save_name = extra_meta['channel_name']

            # 准备文件夹, 用于存放图片, 特征, 结果
            if self.directory is not None:
                target_path = '{}/{}_{}/{}'.format(
                    self.directory, save_id, save_name, extra_meta['track_id'])
                if os.path.exists(target_path) is not True:
                    os.makedirs(target_path)

        # 存人脸图
        if self.save_face and target_path is not None:
            content = datum['face']['face_image']['content']
            if content is not None and len(content) != 0:
                self.save_image(content, target_path, 'face')

        # 存特征
        if self.save_feature and target_path is not None:
            content = datum['face']['face_feature']
            if content is not None and len(content) != 0:
                self.save_feature_content(content, target_path)
        # 存场景图
        if self.save_scene and target_path is not None:
            content = datum['face']['scene_image']['content']
            if content is not None and len(content) != 0:
                self.save_image(content, target_path, 'scene')
        result = {
            'timestamp': datum['face']['timestamp'],
            'extra_meta': extra_meta,
            'type': datum['result_type'],
            'retrieval_result': list()
        }

        # 存比对结果
        for retrieval_result in datum['retrieval_results']:
            for similar_face in retrieval_result['similar_faces']:
                res = {
                    'repository_id': retrieval_result['repository_id'],
                    'face_id': similar_face['id'],
                    'similarity': similar_face['similarity'],
                    'extra_meta': similar_face['extra_meta']
                }
                result['retrieval_result'].append(res)
        if target_path != None:
            self.save_json(result, target_path)
        pass

    # 保存特征到文件
    def save_feature_content(self, data, dir):
        with open(os.path.join(dir, 'feature_{}.feature'.format(self.count)), 'wb+') as f:
            f.write(data)

    # 保存图片
    def save_image(self, data, dir, img_type):
        with open(os.path.join(dir, '{}_{}.jpg'.format(img_type, self.count)), 'wb+') as f:
            f.write(data)

    # 保存json
    def save_json(self, data, dir):
        with open(os.path.join(dir, 'Result_{}.json'.format(self.count)), 'w+') as f:
            json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)

    # 开始收图
    def poll(self):
        while True:
            self.receive()


def main(argv):
    mode = ALL
    url = '192.168.2.80'
    save_feature = False
    save_scene = False
    save_face = False
    directory = None
    try:
        opts, args = getopt.getopt(
            argv,
            'hu:crafsFd:',
            [
                'help',
                'url=',
                'capture',
                'retrieval',
                'all',
                'save_feature',
                'save_scene',
                'save_face',
                'directory='
            ]
        )
    except:
        print('python streaming_client.py -h for help')
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h, --help'):
            print('Usage:')
            print(
                '  python streaming_client.py [-c/--capture|-r/--retrieval|-a/--all(default)]')
            print('Options:')
            print('  [-u/--url ${box_url}] target box ip, default: 192.168.2.80')
            print('  [-d/--directory ${save_path}] target directory to save data')
            print('  [-f/--save_feature] save feature to target directory')
            print('  [-F/--save_face] save face image to target directory')
            print('  [-s/--save_scene] save scene image to target directory')
            sys.exit()
        elif opt in ('-u', '--url'):
            url = arg
        elif opt in ('-c', '--capture'):
            mode = CAPTURE
        elif opt in ('-r', '--retrieval'):
            mode = RETRIEVE
        elif opt in ('-a', '--all'):
            mode = ALL
        elif opt in ('-f', '--save_feature'):
            save_feature = True
        elif opt in ('-F', '--save_face'):
            save_face = True
        elif opt in ('-s', '--save_scene'):
            save_scene = True
        elif opt in ('-d', '--directory'):
            directory = arg

    if (save_face or save_feature or save_scene) and directory is None:
        print('Need to specify saveing directory')
        sys.exit()
    print('host: %s' % url)
    if mode == CAPTURE:
        print('mode: capture')
    elif mode == RETRIEVE:
        print('mode: retrieval')
    else:
        print('mode: all')

    print('############################################################################')
    print('### WARNING: please make sure your app version is 1.4.0 or newer version ###')
    print('############################################################################')
    print('save feature: %s' % save_feature)
    print('save face: %s' % save_face)
    print('save scene: %s' % save_scene)
    print('directory: %s' % directory)

    client = StreamingClient(
        mode, url, save_face=save_face,
        save_feature=save_feature,
        save_scene=save_scene, directory=directory
    )
    client.poll()


if __name__ == "__main__":
    main(sys.argv[1:])
