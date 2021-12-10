import subprocess

def update():
    p = subprocess.check_output(['sudo', 'apt', '-y', 'update'])
    for line in p.splitlines():
        # decode() removes the b prefix on the output strings
        print(line.decode())
        
def install_spc():
    p = subprocess.call(['sudo', 'apt', 'install', '-y', 'software-properties-common'])
                                 
def add_repo():
    p = subprocess.call(['sudo', 'add-apt-repository', '--yes', '--update', 'ppa:ansible/ansible'])
                                 
def install_ansible_pkg():
    p = subprocess.call(['sudo', 'apt', 'install', '-y', 'ansible'])

update()
install_spc()
add_repo()
install_ansible_pkg()
