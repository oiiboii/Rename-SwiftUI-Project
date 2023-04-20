import os
import shutil
import mimetypes

def copy_and_rename_project():
    # Prompt the user for the path to the project folder and the new project name
    old_project_path = input("Enter the path to the project root folder: ")
    new_project_name = input("Enter the new project name: ")
    # Construct the new project path by joining the old project's parent folder and the new project name
    new_project_path = os.path.join(os.path.dirname(old_project_path), new_project_name)

    # Copy the old project folder to the new project folder
    shutil.copytree(old_project_path, new_project_path)

    # Extract the old project name from the old project path
    old_project_name = os.path.basename(old_project_path)

    # Define a helper function to format the project name for use in the Swift file
    def format_name(name):
        return name.replace(" ", "_").replace("-", "_") + "App"

    # Format the old and new project names using the helper function
    old_project_name_formatted = format_name(old_project_name)
    new_project_name_formatted = format_name(new_project_name)

    # Define a helper function to update and rename a given path
    def update_and_rename_path(path, old, new):
        if old in path:
            new_path = path.replace(old, new)
            os.rename(path, new_path)
            print(f"Renamed {path} to {new_path}")
            return new_path
        return path

    # Rename files and folders containing the old project name with the new project name
    for root, dirs, files in os.walk(new_project_path):
        for name in files + dirs:
            path = os.path.join(root, name)
            update_and_rename_path(path, old_project_name, new_project_name)

    # Update the CFBundleName key in the Info.plist file
    info_plist_path = os.path.join(new_project_path, new_project_name, "Info.plist")
    with open(info_plist_path, "r+") as f:
        contents = f.read()
        new_contents = contents.replace(old_project_name, new_project_name)
        f.seek(0)
        f.write(new_contents)
        f.truncate()
    print(f"Updated {info_plist_path}")

    # Add custom MIME type for .plist files
    mimetypes.add_type('text/xml', '.plist')

    # Update the main Swift file with the new project name and non-Swift text files
    for root, dirs, files in os.walk(new_project_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            mime_type, _ = mimetypes.guess_type(file_path)
            
            if file_name.endswith(('.swift', '.plist', '.md', '.json', '.xcconfig', '.xcscheme', '.strings', '.h', '.m', '.cpp', '.hpp')):
                with open(file_path, "r", errors='replace') as f:
                    lines = f.readlines()
                with open(file_path, "w", errors='replace') as f:
                    for line in lines:
                        line = line.replace(old_project_name_formatted, new_project_name_formatted)
                        line = line.replace(old_project_name, new_project_name)
                        f.write(line)
                print(f"Updated {file_path}")

                if file_name.endswith(".swift"):
                    new_file_name = file_name.replace(old_project_name_formatted + ".swift", new_project_name_formatted + ".swift")
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {file_path} to {new_file_path}")

copy_and_rename_project()
