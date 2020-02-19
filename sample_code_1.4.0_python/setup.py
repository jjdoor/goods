import os
import subprocess

def main():
    subprocess.check_call(['python3', './virtualenv-16.0.0/virtualenv.py', 'venv'])
    os.chdir('avro-python3-1.8.2')
    subprocess.check_call(['../venv/bin/python3', 'setup.py', 'install'])
    os.chdir('..')
    os.chdir('hyper')
    subprocess.check_call(['../venv/bin/python3', 'setup.py', 'install'])

if __name__=='__main__':
    main()
