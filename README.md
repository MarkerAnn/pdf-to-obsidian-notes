# PDF to Obsidian Notes

Convert your lecture PDFs into Obsidian notes with embedded images
automatically. This script creates a structured note with all slides from your
PDF and prepares them for note-taking in Obsidian.

## 🚀 Getting Started with Git

There are two ways to get this project:

### Option 1: Fork the Project (Recommended for making contributions)

1. Click the "Fork" button at the top right of this GitHub repository
2. This creates your own copy of the project on your GitHub account
3. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/pdf-to-obsidian-notes.git
   cd pdf-to-obsidian-notes
   ```

### Option 2: Direct Clone (If you just want to use the tool)

```bash
git clone https://github.com/markerann/pdf-to-obsidian-notes.git
cd pdf-to-obsidian-notes
```

### Installing Git

If you don't have Git installed:

- **Mac**:
  1. Open Terminal
  2. Type `git --version`
  3. If Git is not installed, you'll be prompted to install it
- **Windows**:
  1. Download Git from https://git-scm.com/download/windows
  2. Run the installer with default settings

## 🎓 Complete Beginner's Guide

### Prerequisites

If this is your first time using Python, follow these steps carefully:

1. **Install Python**

   - Go to https://python.org/downloads/
   - Download and install Python for your system (click "Download Python")
   - During installation, make sure to check "Add Python to PATH"

2. **Install VS Code (recommended editor)**
   - Go to https://code.visualstudio.com/
   - Download and install VS Code
   - Open VS Code and install the Python extension (search for "Python" in the
     extensions tab)

### Setting Up the Project (First Time Setup)

1. **Create a project folder**

   - Create a new folder on your computer for this project
   - Open VS Code
   - Click File → Open Folder and select your new folder

2. **Open the terminal in VS Code**

   - Click View → Terminal (or press Ctrl+` on Windows/Linux, Cmd+` on Mac)

3. **Set up the virtual environment** Copy and paste these commands into the
   terminal, one at a time:

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate it (choose the right command for your system)
   # For Windows:
   venv\Scripts\activate
   # For Mac/Linux:
   source venv/bin/activate

   # Install required packages
   pip install PyMuPDF Pillow
   ```

4. **Save the script**
   - Create a new file called `script.py`
   - Copy the entire script code into this file
   - Save the file

### Running the Script

1. Make sure your virtual environment is activated (you should see `(venv)` at
   the start of your terminal line)
2. Run the script:
   ```bash
   python script.py
   ```
3. The script will ask you for:
   - Path to your PDF file
   - Course name
   - Note name
   - Path to your Obsidian vault notes folder
   - Path where you want to save the images

### Tips for Absolute Beginners

- **Paths**: When entering paths, you can copy them from your file explorer
  - Windows example: `C:\Users\YourName\Documents\my-file.pdf`
  - Mac example: `/Users/YourName/Documents/my-file.pdf`
- **Vault Path**: To find your Obsidian vault path

On Mac:

1. In Obsidian, right-click any note and select "Reveal in Finder"
2. In Finder, right-click the vault folder while holding the Option key
3. Select "Copy [folder name] as Pathname"
4. Paste this path when asked

Alternative method for Mac:

1. Open your vault folder in Finder
2. Right-click the vault folder while holding the Option key
3. Select "Copy [folder name] as Pathname"
4. Paste this path when asked

On Windows:

1. In Obsidian, right-click any note and select "Show in system explorer"
2. In File Explorer, click the path bar at the top to show the full path
3. Copy this path
4. Paste it when asked

---

## 💻 Technical Documentation

### Overview

This script converts PDF presentations into Obsidian-compatible notes with
high-quality image exports of each slide.

### Features

- Converts PDF slides to high-quality PNG images
- Creates an Obsidian note with embedded image references
- Organizes images in a dedicated folder
- Uses a consistent naming scheme for easy reference

### Requirements

- Python 3.7+
- Dependencies:
  - PyMuPDF
  - Pillow

### Installation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install PyMuPDF Pillow
```

### Usage

```bash
python script.py
```

### Output Structure

```
obsidian-vault/
├── notes/
│   └── your-note.md
└── images/
    └── course-name - note-name - photos/
        ├── slide_1.png
        ├── slide_2.png
        └── ...
```

### Note Format

```markdown
## Slide 1

![[image_name.png]] **Note**:

## Slide 2

![[image_name.png]] **Note**: ...
```

### Error Handling

The script includes error handling for:

- Missing PDF files
- Invalid paths
- PDF processing errors

### Contributing

Feel free to fork and submit pull requests for improvements.

---

## ❗ Troubleshooting

### Common Issues and Solutions

1. **"Command not found: python"**

   - Make sure Python is installed
   - Try using `python3` instead of `python`

2. **"externally-managed-environment" error**

   - This is normal on newer Python installations
   - Make sure you're using a virtual environment as described above

3. **"ModuleNotFoundError"**

   - Make sure you've activated the virtual environment
   - Reinstall dependencies: `pip install PyMuPDF Pillow`

4. **Path errors**
   - Use forward slashes (/) even on Windows
   - Make sure paths don't have quotes around them
   - Check for typos in file/folder names

For any other issues, make sure:

1. Your virtual environment is activated (`(venv)` visible in terminal)
2. All paths exist and are accessible
3. You have write permissions in the output directories

Need more help? Create an issue on the GitHub repository with:

- Your operating system
- The exact error message
- Steps to reproduce the problem
