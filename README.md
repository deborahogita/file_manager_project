# File Manager Utility

A Python-based file management utility that helps create, backup, organize, and log files automatically.

## Features:
- Creates a `StudentFiles` folder if it doesn't exist.
- Creates a file with student names and writes them into the file.
- Displays file information such as size and last modified date.
- Creates backups of files and moves them to an archive folder.
- Allows users to delete files from the folder and logs the activity.

## Requirements:
- Python 3.x

## Installation:
To set up this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/deborahogita/file-manager-project.git

2. Navigate to the project directory:

cd file-manager-project


3. Set up a virtual environment (optional but recommended):

python -m venv venv


4. Activate the virtual environment:

For Windows:

venv\Scripts\activate


For Mac/Linux:

source venv/bin/activate


5. Install required dependencies:
This project doesn’t have external dependencies, but if you add any in the future, you can use:

pip install -r requirements.txt

Usage:

1. Run the script:

python file_manager.py


2. Follow the prompts to:

Enter student names.

Backup files.

Archive files.

Delete files.

Example:

When you run the script, you will:

Create a file called records_YYYY-MM-DD.txt containing student names.

Backup the file into an archive.

Optionally, delete files and log the actions.

License:

This project is licensed under the MIT License - see the LICENSE
 file for details.


### **What to Do Next:**
1. **Create a new file** named `README.md` in your project directory.
2. **Copy and paste** the above content into your `README.md` file.
3. **Save the file**.

Once you've done that, you can add it to Git, commit it, and push it to GitHub:

### **Git Commands:**
1. Add the README
   git add README.md


2. Commit the change:

git commit -m "Added README file"


3. Push to GitHub:

git push origin master