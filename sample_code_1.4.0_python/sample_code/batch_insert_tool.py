# -*- coding: utf-8 -*-
# coding=utf-8
import hyper  # 发送 HTTP/2.0 package
import getopt  # 命令行转化
import sys
import os
import datetime
import io
import util
import hashlib


class BatchInsertTool:
    # 初始化工作
    # url: 服务器地址 e.g: 192.168.2.80
    # image_folder: 图片文件夹地址
    # repo_id: 人像库编号
    def __init__(self, url, image_folder, repo_id, **kwargs):
        self.id = int(kwargs.get('start_id', 1))
        self.append = kwargs.get('append', False)
        self.repo_id = repo_id
        self.image_folder = image_folder
        self.url = '{}:17331'.format(url)

    # 从 image_folder 读取图片的raw数据
    def images(self):
        directory = os.fsencode(self.image_folder)
        image_list = list()

        # 遍历image_folder下每个文件
        for file in os.listdir(directory):
            # 如果不是文件夹, 读取raw数据
            if os.path.isfile(os.path.join(directory, file)):
                with open(os.path.join(directory, file), 'rb') as f:
                    image_raw_data = f.read()
                    image_list.append(image_raw_data)
        return image_list

    # 插入人像
    def insert(self):
        for image in self.images():
            # 插入人像的api
            path = '/face/v1/repositories/{}/faces/{}'.format(
                self.repo_id, self.id)
            # 建立链接
            conn = hyper.HTTP20Connection(self.url)

            # 准备序列化 datum
            request_obj = {
                'face_image': {
                    'content': image,
                    'content_type': 'jpg'
                },
                'extra_meta': 'insert at {}'.format(datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
            }

            # 序列化
            with io.BytesIO() as f:
                util.write_avro(util.INSERT_FACE_SCHEMA, f, request_obj)
                body = f.getvalue()

            # 计算body的sha256
            body_hash = hashlib.sha256(body).hexdigest()

            # 准备请求header
            header = {
                # x-kassq-sha256 是body的sha256
                'x-kassq-sha256': body_hash,
                'Accept': 'application/x.avro',
                'Content-type': 'application/x.avro'
            }
            # 发送数据
            conn.request('PUT', path, body, header)
            # 获取 response
            res = conn.get_response()
            # 读取response的body
            body = res.read()
            status = res.status

            if status != 200:
                # 反序列化错误信息
                with io.BytesIO(body) as f:
                    msg = util.read_avro(
                        util.ERROR_SCHEMA, util.ERROR_SCHEMA, f)
                    print('Insert Face Failed')
                    print('Status: {}'.format(status))
                    print('Reason: {}'.format(msg['reason']))
                    sys.exit(2)
            else:
                print('Insert face Success')
                print('Face ID: {}'.format(self.id))
                print('Status: {}'.format(status))

            self.id += 1
            res.close()

    # 删除人像库
    def delete_repo(self):
        # 删除人像库api
        path = '/face/v1/repositories/{}'.format(self.repo_id)
        conn = hyper.HTTP20Connection(self.url)

        # 请求body是空, 所以x-kassq-sha256填None
        header = {
            'x-kassq-sha256': "",
            'Accept': 'application/x.avro',
            'Content-type': 'application/x.avro'
        }

        # 发送请求
        conn.request('DELETE', path, None, header)
        # 获取response
        res = conn.get_response()

        status = res.status
        if status != 200:
            # 反序列化错误信息
            with io.BytesIO(res.read()) as f:
                msg = util.read_avro(util.ERROR_SCHEMA, util.ERROR_SCHEMA, f)
                print('Delete Repo Failed')
                print('Status: {}'.format(status))
                print('Reason: {}'.format(msg['reason']))
        else:
            print('Delete Repo Suucess')
            print('Status: {}'.format(status))

        res.close()

    # 创建人像库
    def create_repo(self):
        # 创建人像库api
        path = '/face/v1/repositories/{}'.format(self.repo_id)
        # 建立连接 HTTP/2.0 连接
        conn = hyper.HTTP20Connection(self.url)

        # 准备序列化 datum
        request_obj = {
            'name': 'Repo {}'.format(self.repo_id),
            'extra_meta': 'insert at {}'.format(datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
        }

        # 序列化
        with io.BytesIO() as f:
            util.write_avro(util.PUT_REPO_SCHEMA, f, request_obj)
            body = f.getvalue()

        # 计算body的sha256
        body_hash = hashlib.sha256(body).hexdigest()

        # 准备请求header
        header = {
            # x-kassq-sha256 是body的sha256
            'x-kassq-sha256': body_hash,
            'Accept': 'application/x.avro',
            'Content-type': 'application/x.avro'
        }
        # 发送请求
        conn.request('PUT', path, body, header)
        # 获取response
        res = conn.get_response()
        status = res.status

        if status != 200:
            # 反序列化错误信息
            with io.BytesIO(res.read()) as f:
                msg = util.read_avro(util.ERROR_SCHEMA, util.ERROR_SCHEMA, f)
                print('Create Repo Failed')
                print('Status: {}'.format(status))
                print('Reason: {}'.format(msg['reason']))
        else:
            print('Create Repo Suucess')
            print('Status: {}'.format(status))

        res.close()

    def execute(self):
        if self.append is False:
            self.delete_repo()
            self.create_repo()
        self.insert()


def main(argv):
    url = None
    start_id = 1
    append = False
    image_folder = None
    repo_id = 1

    try:
        opts, args = getopt.getopt(
            argv,
            'hi:s:r:au:',
            [
                'help',
                'image_folder=',
                'start_id',
                'repo_id=',
                'append',
                'url='
            ]
        )

    except:
        print('batch_insert_tool.py -h for more information')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(
                'batch_insert_tool.py -u/--url $url -i/--image_folder $image_folder [options]')
            print('options:')
            print('-a/--append append mode, default False')
            print('-s/--start_id $start_id default 1')
            print('-r/--repo_id $repo_id default 1')
            sys.exit()
        if opt in ('-u', '--url'):
            url = arg
        if opt in ('-i', '--image_folder'):
            image_folder = arg
        if opt in ('-s', '--start_id'):
            start_id = arg
        if opt in ('-r', '--repo_id'):
            repo_id = arg
        if opt in ('-a', '--append'):
            append = True

    if url is None or image_folder is None:
        print('batch_insert_tool.py -h for more information')
        sys.exit(2)
    else:
        print('url: {}'.format(url))
        print('image_folder: {}'.format(image_folder))
        print('start_id: {}'.format(start_id))
        print('repo_id: {}'.format(repo_id))
        print('append: {}'.format(append))

    tool = BatchInsertTool(url, image_folder, repo_id,
                           start_id=start_id, append=append)
    tool.execute()


if __name__ == "__main__":
    main(sys.argv[1:])
