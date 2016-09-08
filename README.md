# SikuliTools
The primary purpose for this collection of tools is to leave [SikuliX IDE](http://sikulix.com/) and write GUI tests in Sublime Text.
  
- captures a selection from the screen, saves it to the currently active directory and inserts the filename at the cursor position.

## Installation
**With the Package Control plugin:** The easiest way to install SikuliTools is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart Sublime Text and bring up the Command Palette (`Command+Shift+P`). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select SikuliTools when the list appears. The advantage of using this method is that Package Control will automatically keep SikuliTools up to date with the latest version.

**Without Git:** Download the latest source from `GitHub <https://github.com/hendrikelsner/SikuliTools>`_ and copy the whole directory into the Packages directory.

**With Git:** Clone the repository in your Sublime Text Packages directory, located somewhere in user's "Home" directory::

    git clone https://github.com/hendrikelsner/SikuliTools.git


To access the "Package" directory use:
Sublime Text -> Preferences -> Browse Packages...

## Usage

### Capture
- Hit `cmd+alt+c`
- type image name and hit ENTER (if you leave this blank, a timestamp is used as filename)
- select a part of the screen

The selection is saved to an image file in the directory of the currently active tab.

## TODO
- Command to clean up a test folder (remove unused images, show missing)
- A match overlay that highlights all matches on screen for a selected image pattern
- Build script to run the currently open test
- CheatSheet view (like https://packagecontrol.io/packages/Cheat%20Sheets)
