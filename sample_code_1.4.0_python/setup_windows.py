import os
import subprocess
import shutil

def main():
    subprocess.check_call(['python', './virtualenv-16.0.0/virtualenv.py', 'venv'])
    if os.path.isdir('./venv/bin'):
        shutil.rmtree('./venv/bin')
    shutil.copytree('./venv/Scripts', './venv/bin')
    os.chdir('avro-python3-1.8.2')
    subprocess.check_call(['../venv/bin/python', 'setup.py', 'install'])
    os.chdir('..')
    os.chdir('hyper')
    subprocess.check_call(['../venv/bin/python', 'setup.py', 'install'])

if __name__=='__main__':
    main()
