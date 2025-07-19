# KaliArch

## Index
* [How does it work?](#how-it-works)
* [Usage](#usage)
* [Future Features](#future-features)
* [References](#references)

---

## 💡 About
> ***A script that automatically installs utilities and offers the user the option to customize ArchLinux (Xorg + i3-wm) with a KaliLinux-like theme.***

---

## How does it work?
The script will receive the name of the system package manager and a `.txt` list of the utilities the user will install, and then it will begin installing the packages on the system.
With the script, the user can also delete the packages installed with the script, using the `--uninstall utilities.txt` command.

The user can also pass the `--kalitheme` argument to configure the automatic default theme I developed, which simulates the KaliLinux aesthetic.
**By passing the `--kalitheme` argument, the script may install some additional packages, but these can be removed with `--uninstall kalitheme`. See what will be added and configured [Configurator](configure.sh)**

With the `--kalitheme` argument, the user can also pass the `--dynamic-background` argument. The second argument is a number (e.g., `5`) to specify the time each wallpaper should change. The third argument specifies whether they should change randomly (`--randomize`) or in the default order of the files in the directory (`--orderd`). Finally, the fourth argument is the directory path to the wallpapers (e.g., `~/wallpapers/`).

You can copy the `wallpapers` directory from this repository to your home folder.

> 🔴 **The original system settings will not be modified or deleted; they will be saved in the same location, with the `.old` extension for security.**

**See the list of packages and files that will be installed on your system, and the path to the configuration files that will be created for them [Packages list](packages.list)**
**With this, you can modify the added configuration files as needed, or return to the old ones with the `.old` extension.**

---

## Usage Modes
```bash
# Install packages listed in a file
python3 kaliarch.py pacman utilities.txt

# Uninstall packages installed with the list
python3 kaliarch.py --uninstall utilities.txt

# Apply the Kali-like theme (includes Zsh, i3, terminal, etc. settings)
python3 kaliarch.py --kalitheme

# Apply the Kali-like theme with wallpaper Dynamic
python3 kaliarch.py --kalitheme --dynamic-background 5 --randomize ~/wallpapers/

# You can also use the default order instead of random.
python3 kaliarch.py --kalitheme --dynamic-background 5 --ordered ~/wallpapers/

# Remove packages and configuration files installed by the script.
python3 kaliarch.py --uninstall kalitheme
```
---

### Recommendations
- Configure the terminal color and transparency, if necessary.
- Set zsh as the default shell.

---

## Future features
- The user can pass the `--uninstall-autoreplace kalitheme` argument to remove packages and configuration files installed by the script and automatically replace them with the .old file in their directories.

---

## References
- [Zsh](https://github.com/clamy54/kali-like-zsh-theme/blob/main/README.md)
- [Kitty Themes](https://github.com/dexpota/kitty-themes)
