# Mover.py

## Description
This is a simple python script to organize files in a directory. It will move files into folders based on their file extension. It is customizable to your needs.

## Requirements
- Python 3.10 or higher
- A computer
- A directory to organize
- A text editor
- A brain

## Usage
1. Clone the repository
2. Edit the `settings.json` file to your needs
3. Run the script -- `py main.py`--
4. Enjoy your organized files!

## Settings
The settings file is a JSON file that contains the settings for the script. The settings are as follows:

- `targetFolder`: The path to the directory you want to organize
- `testFolder`: The path to the directory you want to use for testing
- `testMode`: Enable or disable test mode
- `formats`: A list of file formats that you want to organize
  - `name`: The name of the format
  - `folder`: The name of the folder to move the files to
  - `extensions`: A list of extensions for the format

### Test mode
Test mode takes a different directory and, before organizing it, creates an empty file inside for each extension. This is useful for testing the script before using it on your actual files.