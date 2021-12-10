# useful-ish-scripts
Scripts that might be nice to have.

Mainly so I don't have to retype sudo until the fingers fall off.
I make no promise of elegance within this code.

___
- __update_install_script.py__: Simple python3 script that does `apt update`, `apt upgrade`, and `apt autoremove` in one fell swoop. Also has a function for getting packages via `apt install`. Just uncomment the function if desired. Must be run as root (just `sudo python3 update_install_script.py`).
- __install_ansible_ubuntu.py__: Tired of looking up how to install Ansible? Just run this. It will hopefully work... Follows Ansible's instructions for Ubuntu installation.
