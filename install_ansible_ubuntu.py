import subprocess

def update():
    p = subprocess.check_output(['sudo', 'apt', '-y', 'update'])
    for line in p.splitlines():
        # decode() removes the b prefix on the output strings
        print(line.decode())
        
def install_spc():
    p = subprocess.check_output([['sudo', 'apt', 'install', 'software-properties-common'])
    for line in p.splitlines():
        print(line.decode())
                                 
def add_repo():
    p
                                 
