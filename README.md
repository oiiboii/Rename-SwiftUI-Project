# SwiftUI Project Renamer

This script helps you to rename an iOS project by replacing all occurrences of the old project name with the new project name. It updates file names and content in various file types like Swift, plist, JSON, etc.


## Requirements

- Python 3.6 or later

## How to use

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory where the `rename_ios_project.py` script is located.
3. Run the script using the following command:

Rename-SwiftUI-Project.py <old_project_path> <new_project_path> <old_project_name> <new_project_name>


Replace the arguments with the appropriate values:

- `<old_project_path>`: The path to the directory containing the current iOS project.
- `<new_project_path>`: The path to the directory where you want the renamed project to be created.
- `<old_project_name>`: The current name of the iOS project.
- `<new_project_name>`: The new name for the iOS project.

4. The script will create a new directory at the specified `<new_project_path>` containing the renamed project. All files and their content will be updated with the new project name.

**Note:** The original project directory will not be modified, and the script will create a copy of the project with the updated name.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
