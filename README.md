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
For Windows: venv\Scripts\activate

5. Install required dependencies:
This project doesn’t have external dependencies, but if you add any in the future, you can use: pip install -r requirements.txt

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
 

---

### **Explanation of the Sections:**
1. **Project Title and Description**:
   - Describes the purpose of your project (in this case, a Python file management utility).
   
2. **Features**:
   - Lists the main features of your project, highlighting what it does.
   
3. **Requirements**:
   - Specifies any software or versions needed to run your project. For this project, you only need **Python 3.x**.

4. **Installation**:
   - Explains how to set up the project locally.
   - Provides commands to clone the repository, set up a virtual environment, and install dependencies (if any).
   
5. **Usage**:
   - Explains how to run the project and what actions the user can perform.
   
6. **Example**:
   - Gives an example of what the user should expect when they run the script.

7. **License**:
   - If you’re open to sharing or collaborating, you can include a license (like the MIT License) or state that it's open-source.

---

### **Step-by-Step to Create the README File:**

1. Open your **VS Code** and navigate to the **Explorer**.
2. **Create a new file** named `README.md`.
3. Copy and **paste the template** above into the `README.md` file.
4. **Save** the file.

---

### **Next Steps**
Once the `README.md` file is added, commit it to Git and push it to your GitHub repository:

1. **Add the README file** to Git:
   ```bash
   git add README.md
2. Commit the change: 
git commit -m "Added README file"
3. Push the changes to github:
git push origin master
