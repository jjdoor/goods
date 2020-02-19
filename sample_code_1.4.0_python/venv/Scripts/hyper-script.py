#!D:\python_project\sample_code_1.4.0_python\venv\bin\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'hyper==0.7.0','console_scripts','hyper'
__requires__ = 'hyper==0.7.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hyper==0.7.0', 'console_scripts', 'hyper')()
    )
