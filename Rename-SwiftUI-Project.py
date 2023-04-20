import os
import shutil

def copy_and_rename_project():
    # Prompt the user to enter the project folder and name
    old_project_path = input("Enter the path to the project root folder: ")
    new_project_name = input("Enter the new project name: ")

    # Create a copy of the old project
    new_project_path = f"{os.path.dirname(old_project_path)}/{new_project_name}"
    shutil.copytree(old_project_path, new_project_path)

    # Get the old project name from the old project path
    old_project_name = os.path.basename(old_project_path)

    # Loop through all files and folders in the new project
    for root, dirs, files in os.walk(new_project_path):
        for name in files + dirs:
            # Construct the full path to the file or folder
            path = os.path.join(root, name)

            # Rename the file or folder if it contains the old project name
            if old_project_name in path:
                new_path = path.replace(old_project_name, new_project_name)
                os.rename(path, new_path)
                print(f"Renamed {path} to {new_path}")

    # Update the CFBundleName key in Info.plist
    info_plist_path = f"{new_project_path}/{new_project_name}/Info.plist"
    with open(info_plist_path, "r") as f:
        contents = f.read()
    new_contents = contents.replace(old_project_name, new_project_name)
    with open(info_plist_path, "w") as f:
        f.write(new_contents)
    print(f"Updated {info_plist_path}")

    # Update the @main struct name in [ProjectName]App.swift
    app_swift_path = f"{new_project_path}/{new_project_name}/{new_project_name}App.swift"
    with open(app_swift_path, "r") as f:
        contents = f.read()
    new_contents = contents.replace(f"@main struct {old_project_name}", f"@main struct {new_project_name}")
    with open(app_swift_path, "w") as f:
        f.write(new_contents)
    print(f"Updated {app_swift_path}")

    print("Done!")

# Example usage
copy_and_rename_project()
