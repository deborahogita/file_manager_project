import os
import sys

# Task 1: Check if "StudentFiles" exists, and create it if it doesn't
try:
    folder_name = "StudentFiles"
    if not os.path.exists(folder_name):
        # Folder doesn't exist, create it
        os.mkdir(folder_name)
        print(f"The folder '{folder_name}' has been created at: {os.path.abspath(folder_name)}")
    else:
        print(f"The folder '{folder_name}' already exists at: {os.path.abspath(folder_name)}")
except Exception as e:
    # If any error occurs, terminate the program gracefully
    print(f"Error: {e}")
    sys.exit("An error occurred while creating the folder. Program terminated.")

import datetime
import os

# Task 2: File Creation and Writing
try:
    # Step 1: Generate the file name using the current date
    filename = "records_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    file_path = os.path.join("StudentFiles", filename)

    # Step 2: Prompt the user to enter five student names and write them into the file
    with open(file_path, "w") as file:
        for _ in range(5):
            student_name = input("Enter student name: ")
            file.write(student_name + "\n")

    # Step 3: Display a success message with the file name and creation time
    print(f"File '{filename}' created successfully at {datetime.datetime.now()}")

except Exception as e:
    print(f"Error: {e}")
    import os
import datetime

# Task 3: Reading and File Information
try:
    # Construct the path for the file created in Step 2
    filename = "records_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    file_path = os.path.join("StudentFiles", filename)

    # Step 1: Read and display the contents of the file
    with open(file_path, "r") as file:
        print("\nFile Contents:")
        print(file.read())  # Display all contents of the file

    # Step 2: Display the file’s size in bytes
    file_size = os.path.getsize(file_path)
    print(f"\nFile Size: {file_size} bytes")

    # Step 3: Display the file’s last modified date
    last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    print(f"Last Modified: {last_modified}")

except Exception as e:
    print(f"Error: {e}")

import shutil
import os
import datetime

# Task 4: Backup and Archiving
try:
    # Construct the path for the original file
    filename = "records_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    file_path = os.path.join("StudentFiles", filename)

    # Step 1: Create a backup of the file
    backup_filename = "backup_" + filename
    backup_file_path = os.path.join("StudentFiles", backup_filename)

    # Check if the backup already exists and rename it if it does
    counter = 1
    while os.path.exists(backup_file_path):
        backup_file_path = os.path.join("StudentFiles", f"backup_{datetime.datetime.now().strftime('%Y-%m-%d')}_{counter}.txt")
        counter += 1

    shutil.copy(file_path, backup_file_path)
    print(f"\nBackup created: {backup_filename}")

    # Step 2: Create an 'Archive' folder if it doesn't exist
    archive_folder = os.path.join("StudentFiles", "Archive")
    if not os.path.exists(archive_folder):
        os.mkdir(archive_folder)
        print(f"Archive folder created at: {archive_folder}")
    else:
        print(f"Archive folder already exists at: {archive_folder}")

    # Step 3: Move the backup file into the Archive folder
    shutil.move(backup_file_path, archive_folder)
    print(f"Backup moved to Archive folder: {os.path.join(archive_folder, os.path.basename(backup_file_path))}")

    # Step 4: List all files in the Archive folder
    print("\nFiles in Archive folder:")
    print(os.listdir(archive_folder))

except Exception as e:
    print(f"Error: {e}")

# Task 5: Logging System
log_file = os.path.join("StudentFiles", "activity_log.txt")

def log_activity(message):
    try:
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as log:
            log.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Error while logging activity: {e}")

try:
    # Construct the file name for today's records file
    filename = "records_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    file_path = os.path.join("StudentFiles", filename)

    # Log file creation and archiving activity
    log_activity(f"{filename} created and archived successfully.")

except Exception as e:
    # Log the error if an exception occurs
    log_activity(f"Error: {e}")
    print(f"Error: {e}")

import os
import datetime

# Task 6: Advanced File Operations
log_file = os.path.join("StudentFiles", "activity_log.txt")

def log_activity(message):
    try:
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as log:
            log.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Error while logging activity: {e}")

try:
    # Step 1: Ask the user if they want to delete a file
    delete_file = input("Would you like to delete a file from StudentFiles? (Yes/No): ").strip().lower()

    if delete_file == "yes":
        # Step 2: Ask for the file name and delete the file
        file_to_delete = input("Enter the file name to delete: ").strip()
        file_to_delete_path = os.path.join("StudentFiles", file_to_delete)

        if os.path.exists(file_to_delete_path):
            # Delete the file
            os.remove(file_to_delete_path)
            print(f"File '{file_to_delete}' deleted successfully.")

            # Step 3: Log the deletion event
            log_activity(f"{file_to_delete} deleted successfully.")
        else:
            print(f"The file '{file_to_delete}' does not exist in the folder.")

    # Step 4: Display all remaining files in the StudentFiles folder
    print("\nRemaining files in StudentFiles:")
    print(os.listdir("StudentFiles"))

except Exception as e:
    print(f"Error: {e}")
    log_activity(f"Error: {e}")
