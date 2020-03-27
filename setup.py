import os, sys
import glob

packages = '''
respi-wheat
farquhar-wheat
elong-wheat
growth-wheat
senesc-wheat
cn-wheat
fspm-wheat
'''.split()

def sh(cmd):
    return os.system(cmd)

def apply(*args):
    status = 0
    cmd = 'python setup.py %s'%(' '.join(*args))
    for pkg in packages:
        os.chdir(pkg)
        st = sh(cmd)
        status = max(st, status)
        os.chdir('..')
    return status
if __name__ == "__main__": 
    #print('packages', packages)
    #print('Args', sys.argv[1:])
    status = apply(sys.argv[1:])
    