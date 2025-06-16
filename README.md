Sure! Here's a well-formatted `README.md` for your **Python File Organizer & Sorter** project:

---

````markdown
# 📁 Python File Organizer & Sorter

The **Python File Organizer & Sorter** is a command-line tool that helps declutter and organize your files with ease. It scans a specified directory and automatically moves files into categorized subfolders based on their file extensions—making your digital life a lot cleaner!

---

## 🚀 Features

- **🔄 Automated File Sorting**  
  Sorts files into predefined categories like `Images`, `Documents`, `Videos`, `Audio`, `Code`, and more.

- **🛠️ Customizable Categories**  
  Easily update the extension-to-folder mappings to suit your personal or project-specific needs.

- **🧱 Robust Error Handling**  
  Handles invalid paths, permission errors, and duplicate file names gracefully without crashing.

- **🖥️ Intuitive CLI**  
  Prompts guide users to input the directory path for organization.

- **📋 Movement Logs**  
  Real-time feedback shows which files are moved and to which folders.

---

## 📦 How to Use

### 1. Save the Script

Save the script as `file_organizer.py` or any filename ending in `.py`.

### 2. Open Terminal / Command Prompt

Navigate to the folder where the script is located:

```bash
cd /path/to/your/script/folder
````

### 3. Run the Script

Run the script with Python:

```bash
python file_organizer.py
```

### 4. Enter Directory Path

The script will prompt you to enter the full path of the directory you want to organize.
Examples:

* **Windows**: `C:\Users\YourUser\Downloads`
* **macOS/Linux**: `/home/youruser/Downloads`

Type the path and press `Enter`. You can also type `exit` to quit the program.

### 5. Watch the Magic ✨

The script will begin processing files, creating category folders (if they don’t already exist), and moving files accordingly. You'll see real-time logs of all movements in your terminal.

---

## 🔧 Customization

The categorization logic is based on the `extension_to_folder` dictionary inside the `organize_files` function.

### ➕ Add New Categories

```python
extension_to_folder.update({
    '.csv': 'Spreadsheets',
    '.xlsx': 'Spreadsheets',
    # Add more as needed
})
```

### ✏️ Modify Existing Mappings

```python
extension_to_folder.update({
    '.zip': 'CompressedFiles',  # Changed from 'Archives'
})
```

### 📂 Default “Others” Category

Any files with extensions not explicitly mapped will go into the `Others` folder by default.

---

## 🧪 Technologies Used

* **Python 3.x**
* [`os`](https://docs.python.org/3/library/os.html) – Directory and file path operations
* [`shutil`](https://docs.python.org/3/library/shutil.html) – High-level file operations
* [`collections.defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) – Flexible category mapping

---

## ⚠️ Error Handling

This script includes multiple safeguards to ensure smooth operation:

* ✅ Validates input directory paths
* ✅ Automatically creates missing category folders
* ✅ Avoids overwriting existing files (adds suffix like `file(1).txt`)
* ✅ Catches permission and file movement errors

---

## 📃 License

This project is open-source and free to use.

---

## 🤝 Contributing

Feel free to fork this repository and open a pull request if you want to improve the script, add more categories, or enhance its features.

---

## 🙌 Acknowledgments

Thanks to the Python standard library for making scripting easy and powerful!

---

Happy organizing! 🧹📂

```

---

Let me know if you'd like the actual code snippet embedded inside the README or want me to generate a `requirements.txt` (though it's not needed for this basic script).
```
