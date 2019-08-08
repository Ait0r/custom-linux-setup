#!/usr/bin/env python
# -*- coding: utf-8 -*-


from subprocess import run
import subprocess

APT_PACKAGES = ['python3-pip', 'python-pip', 'htop', 'git', 'snapd', 'gnome-tweaks']
PIP_INSTALL = ['jupyterlab', 'numpy', 'pandas', 'matplotlib', 'tqdm', 'inquirer', 'seaborn']
SNAP_PACKAGES = [('bitwarden', False),
                 ('gitkraken', False),
                 ('pycharm-professional', True),
                 ('thunderbird', True),
                 ('sublime-text', True)]

STD_OUT = None


def update_apt():
    print("Performing update...")
    run(["apt", "update"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    print("Done!\n")


def install_package_apt(package):
    print(f"Installing package {package}")
    run(["apt", "install", "-y", package], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    print("Done!\n")


def install_package_snap(snap):
    package, classic = snap
    print(f"Installing package {package}")
    if classic:
        run(["snap", "install", "--classic", package], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    else:
        run(["snap", "install", package], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    print("Done!\n")


def install_package_pip(package):
    print(f"Installing python package {package}")
    run(["python3", "-m", "pip", "install", package], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    print("Done!\n")


def change_bashrc():
    print(f"Changing bashrc...")
    run(["rm", "~/.bashrc"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    run(["cp", "bashrc", "~/.bashrc"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    run(["rm", "bashrc"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    print("Done!\n")


def change_theme():
    print(f"Changing theme...")
    run(["cp", "theme/02-McMojave-circle-black.tar.xz", "~/.icons"], check=True, stdout=STD_OUT,
        stderr=subprocess.STDOUT)
    run(["cp", "theme/02-McMojave-circle-black.tar.xz", "~/.themes"], check=True, stdout=STD_OUT,
        stderr=subprocess.STDOUT)
    run(["tar", "xf", "~/.themes/*.tar.xz"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    run(["tar", "xf", "~/.icons/*.tar.xz"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    run(["rm", "~/.themes/*.tar.xz"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)
    run(["rm", "~/.icons/*.tar.xz"], check=True, stdout=STD_OUT, stderr=subprocess.STDOUT)

    run(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", "\"Mojave-dark-solid\""], check=True,
        stdout=STD_OUT, stderr=subprocess.STDOUT)
    run(["gsettings", "set", "org.gnome.desktop.interface", "icon-theme", "\"McMojave-circle-dark\""], check=True,
        stdout=STD_OUT, stderr=subprocess.STDOUT)
    print("Done!\n")


if __name__ == '__main__':
    import os

    if os.getuid():
        print("Error: Script need root permission")
    else:
        update_apt()

        for p in APT_PACKAGES:
            install_package_apt(p)

        for p in SNAP_PACKAGES:
            install_package_snap(p)

        for p in PIP_INSTALL:
            install_package_pip(p)

        change_bashrc()
        change_theme()
