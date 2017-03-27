# ubuntu-macos-keys
Ubuntu key-binding configuration to emulate some common macOS key-bindings

Tested in a Ubuntu 16.04 VMWare Fusion VM on a Macbook Pro

## Install CompizConfig Settings Manager
`# apt-get install compizconfig-settings-manager`
## Install AutoKey
`# apt-get install autokey-gtk`

## Set CCSM Settings
1. Launch CompizConfig Settings Manager
2. Go To Ubuntu Unity Plugin
3. Disable Launcher -> Key to show the Dash, Launcher, and Help Overlay
4. Set Switcher -> 'Key to start the switcher' to `<Super>Tab`
5. Set Switcher -> 'Key to switch to the previous window in the switcher' to `<Super><Shift>Tab`
6. Set Switcher -> 'Key to flip through windows in the switcher' to `<Super>grave` (`/~ key)
7. Set Switcher -> 'Key to flip through windows in the switcher backwards' to `<Super><Shift>grave` (`/~ key)

# Set AutoKey Settings
1. Launch AutoKey
2. Add a Folder and point it to ubuntu-macos-keys/autokey (File -> New -> Folder)
3. Quit AutoKey and restart (Note: it's not enough to just close the window, you need to close the application by using the Ubuntu toolbar icon in the top right.
