import os
import shutil

# Ask for the path to the Xcode project
project_path = input("Enter the path to the Xcode project folder: ")

# Ask for the new project name
new_project_name = input("Enter the new project name: ")

# Get the current project name
current_project_name = os.path.basename(project_path)

# Create the new project directory
new_project_directory = os.path.join(os.path.dirname(project_path), new_project_name)
shutil.copytree(project_path, new_project_directory)

# Rename the Xcode project file
old_project_file_path = os.path.join(
    new_project_directory, current_project_name + ".xcodeproj"
)
new_project_file_path = os.path.join(
    new_project_directory, new_project_name + ".xcodeproj"
)
os.rename(old_project_file_path, new_project_file_path)

# Replace project name in .pbxproj file
pbxproj_path = os.path.join(new_project_file_path, "project.pbxproj")
with open(pbxproj_path, "r") as f:
    contents = f.read()
    updated_contents = contents.replace(current_project_name, new_project_name)
with open(pbxproj_path, "w") as f:
    f.write(updated_contents)

# Replace project name in folders and .swift files, and their contents
for files in os.walk(new_project_directory):
    for name in files:
        print(f"Checking file: {name}")
        if (name == current_project_name.replace(" ", "_").replace("-", "_") + "App.swift"):
            file_path = os.path.join(root, name)
            new_file_name = (new_project_name.replace(" ", "_").replace("-", "_") + "App.swift")
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            shutil.copyfile(file_path, new_file_path)
            
            with open(new_file_path, "r") as f:
                contents = f.read()
                updated_contents = contents.replace(current_project_name, new_project_name)
            with open(new_file_path, "w") as f:
                f.write(updated_contents)
            print(f"Copied {file_path} to {new_file_path}")
            os.remove(file_path)  # Delete the old file
        elif name.endswith(".swift"):
            file_path = os.path.join(root, name)
            with open(file_path, "r") as f:
                contents = f.read()
                updated_contents = contents.replace(
                    current_project_name, new_project_name
                )
            with open(file_path, "w") as f:
                f.write(updated_contents)
            print(f"Replaced project name in {file_path}")

            # Replace project name in folder name if necessary
            if current_project_name.replace(" ", "_").replace("-", "_") in file_path:
                old_folder_name = os.path.dirname(file_path)
                new_folder_name = old_folder_name.replace(
                    current_project_name.replace(" ", "_").replace("-", "_"),
                    new_project_name.replace(" ", "_").replace("-", "_"),
                )
                os.rename(old_folder_name, new_folder_name)
                print(f"Renamed folder {old_folder_name} to {new_folder_name}")

# Clear Xcode cache
os.system("rm -rf ~/Library/Developer/Xcode/DerivedData/*")

print("Done!")
