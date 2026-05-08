# GitHub Integration Guide for Amigo/X4ra Assets

To integrate your local music repository `E:\musica\x4ra_ara` with GitHub and the Amigo/X4ra project, follow these steps:

## 1. Initialize the Local Repository
Open a terminal or command prompt and navigate to your asset folder:
```bash
cd /d E:\musica\x4ra_ara
git init
```

## 2. Create a .gitignore
Prevent large or unnecessary files from being uploaded. Create a file named `.gitignore` in that directory:
```text
# Ignore OS generated files
.DS_Store
Thumbs.db

# Optional: Ignore very large raw audio if you only want to track project files
# *.wav
```

## 3. Add and Commit Files
```bash
git add .
git commit -m "Initial commit of Radio Piratona assets"
```

## 4. Create a GitHub Repository
1. Go to [GitHub](https://github.com/new).
2. Name your repository (e.g., `x4ra-assets`).
3. Do **not** initialize with a README, license, or gitignore.
4. Click "Create repository".

## 5. Link and Push
Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual details:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## 6. Integration with Amigo/X4ra
Once the repository is online, you can use Git submodules or simply keep the path in `src/utils/config.py` pointing to the local clone of this repository.

To add it as a submodule to the main project:
```bash
git submodule add https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git assets/music
```
Then update `src/utils/config.py` to use `"music": "assets/music"`.
