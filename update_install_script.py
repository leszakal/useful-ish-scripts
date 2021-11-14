import subprocess
import sys

def update_upgrade_autorm():
    # Get updates
    try:
        print('\n' + "...Trying to UPDATE...")
        p = subprocess.check_output(['sudo', 'apt', '-y', 'update'])
        for line in p.splitlines():
            # decode() gets rid of the b prefix on output strings
            print(line.decode())
        print('\n' + '--> UPDATE DONE' + '\n')
    except:
        print("ERROR: Update failed")
        sys.exit(1)
    # Upgrade the system
    try:
        print("...Trying to UPGRADE...")
        p = subprocess.check_output(['sudo', 'apt', '-y', 'upgrade'])
        for line in p.splitlines():
            print(line.decode())
        print('\n' + '--> UPGRADE DONE' + '\n')
    except:
        print("ERROR: Upgrade failed")
        sys.exit(1)
    # Automatically remove unused packages
    try:
        print("...Trying to AUTOREMOVE...")
        p = subprocess.check_output(['sudo', 'apt', '-y', 'autoremove'])
        for line in p.splitlines():
            print(line.decode())
        print('\n' + "--> AUTOREMOVE DONE" + '\n')
    except:
        print("ERROR: Autoremove failed")

def install_pkgs():
    try:
        print("---What packages would you like to INSTALL?---\n")
        pkgs = input("Please list desired package names seperated by spaces: ")
        # Alternatively, place desired packages for pkgs variable and comment out input
        # pkgs = 'ssh vim curl git fortune man'
        pkgs = pkgs.split()
        p = subprocess.check_output(['sudo', 'apt', '-y', 'install'] + pkgs)
        for line in p.splitlines():
            print(line.decode())
        print('\n' + "--> INSTALL DONE")
    except:
        print('ERROR: Install has failed')
        sys.exit(1)

update_upgrade_autorm()
# Uncomment install_pkgs() if you want to install packages w/ this script
# install_pkgs()
print("\n---All done; going to bed UwU---")
