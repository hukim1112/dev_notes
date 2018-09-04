# git guide

## 1. How to ignore specific types of files and folders while using git.

ref :http://vinyll.scopyleft.fr/using-gitignore-the-right-way/

### How to write a line in a gitignore?

These simple rule can make it easier to read and avoid name collision

- if it's a folder, add a final `/` 

  Ex) `dist/` / `__pycache__/` (any folder anywhere with that name)

  

- if it's at the root folder, add a starting `/` 

  ex) `/node_modules/` (root folder)

  

- if it's a sub-file or sub-folder add a starting `*/` 

  Ex) `*.pyc` (any file anywhere with *.pyc* extension)

  

- if you want to create an exception, add a starting `!`

  

### Understanding gitignore locations

There are (more than) 3 possible locations where to ignore a file/folder for *git*:

- `~/.gitignore`
- `.gitignore` in the project's folder
- `.git/info/exclude` in the project's folder

#### home gitignore

is located in `~/.gitignore` and contains anything that is specific to you like your OS files, your editors files, etc.

- `.DS_Store` if you're on a MacBook
- `Thumbs.db` is you're on Windows
- your favorite code editors files / folders (`.atom`, `.idea/`, `.project`, `*.sublime-workspace`, …)

Globally anything that will be common to multiple projects in a different language should probably be here.

#### Project's gitignore

Here you should insert anything that is specific to the nature of your project, like `*.pyc` for python 2, `__pycache__/` for python 3, `/node_modules/` for npm projects, …

#### Project's .git/info/exclude

for ignoring files and folders that are specific to your project **and** to your preferences or environment. In other words, this location is to common point between your home gitignore and your project's gitignore. It is less common to use this though.

Examples for python: `/env/`, `/venv/`



## Common usage

```
#add .gitignore in project root folder.

# Ignore file named 'README.txt'
README.txt

# Ignore folder named 'output'
output/

#Ignore all .jave file
*.java

#Ignore all folders named '__pycache__'
__pycache__/
```

