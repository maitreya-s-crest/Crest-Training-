import os
import re
import json
import subprocess
import datetime

workspace = r"C:\Users\MaitreyaSapariya\Desktop\Training\Crest-Training-"
log_file_path = os.path.join(workspace, "daily_pusher.log")

# API Key Redaction Regex
api_key_regex = re.compile(r'\b(sk-proj-[A-Za-z0-9_-]{30,}|sk-[A-Za-z0-9_-]{30,}|gsk_[A-Za-z0-9_-]{30,}|sk-ant-[A-Za-z0-9_-]{30,})\b')

def log_message(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}"
    print(formatted_msg)
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

def personalize_and_redact(filepath):
    # Skip binary files
    if filepath.endswith(('.png', '.jpg', '.pdf', '.zip', '.db', '.pyc', '.lock', '.ico', '.svg')):
        return
        
    modified = False
    
    # 1. Personalize
    if filepath.endswith('.py'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if not content.startswith("# Owner: Maitreya"):
                header = "# Owner: Maitreya Sapariya\n# Project: Crest Training\n\n"
                content = header + content
                modified = True
                
            # Redact keys
            matches = api_key_regex.findall(content)
            for match in matches:
                if not any(placeholder in match.lower() for placeholder in ['placeholder', 'your_key', 'insert_here', 'xxxx']):
                    content = content.replace(match, "")
                    modified = True
                    
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
        except Exception as e:
            log_message(f"Error personalizing/redacting Python file {filepath}: {e}")
            
    elif filepath.endswith('.sql'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            if not content.startswith("-- Owner: Maitreya"):
                header = "-- Owner: Maitreya Sapariya\n-- Project: Crest Training\n\n"
                content = header + content
                modified = True
                
            # Redact keys
            matches = api_key_regex.findall(content)
            for match in matches:
                if not any(placeholder in match.lower() for placeholder in ['placeholder', 'your_key', 'insert_here', 'xxxx']):
                    content = content.replace(match, "")
                    modified = True
                    
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
        except Exception as e:
            log_message(f"Error personalizing/redacting SQL file {filepath}: {e}")
            
    elif filepath.endswith('.ipynb'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                notebook = json.load(f)
            cells = notebook.get('cells', [])
            
            # Personalize
            already_personalized = False
            if cells and cells[0].get('cell_type') == 'markdown':
                source = cells[0].get('source', [])
                if any("Maitreya Sapariya" in line for line in source):
                    already_personalized = True
                    
            if not already_personalized:
                meta_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "# Completed by Maitreya Sapariya\n",
                        "**Project**: Crest Training  \n",
                        "**Status**: Completed and Reviewed"
                    ]
                }
                cells.insert(0, meta_cell)
                notebook['cells'] = cells
                modified = True
                
            # Redact
            for cell_idx, cell in enumerate(cells):
                if cell.get('cell_type') == 'code':
                    source_lines = cell.get('source', [])
                    for line_idx, line in enumerate(source_lines):
                        matches = api_key_regex.findall(line)
                        for match in matches:
                            if not any(placeholder in match.lower() for placeholder in ['placeholder', 'your_key', 'insert_here', 'xxxx']):
                                source_lines[line_idx] = line.replace(match, "")
                                modified = True
                                
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(notebook, f, indent=1)
        except Exception as e:
            log_message(f"Error personalizing/redacting Notebook {filepath}: {e}")
            
    elif filepath.endswith('.env'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            lines = content.splitlines()
            for idx, line in enumerate(lines):
                if '=' in line and not line.strip().startswith('#'):
                    parts = line.split('=', 1)
                    key = parts[0].strip()
                    val = parts[1].strip().strip('"').strip("'")
                    if val and ('key' in key.lower() or 'token' in key.lower() or len(val) > 20):
                        if len(val) > 15 and not any(placeholder in val.lower() for placeholder in ['placeholder', 'your_key', 'insert_here', 'xxxx']):
                            lines[idx] = f"{key}="
                            modified = True
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines) + '\n')
        except Exception as e:
            log_message(f"Error redacting env file {filepath}: {e}")

def main():
    log_message("Starting daily pusher script...")
    
    # Run git status to find untracked files
    res = subprocess.run(["git", "status", "--porcelain"], cwd=workspace, capture_output=True, text=True)
    if res.returncode != 0:
        log_message("Error running git status: " + res.stderr)
        return
        
    lines = res.stdout.splitlines()
    untracked_files = []
    
    # Filter for files that are untracked (marked as ??)
    # We want files inside: 10-LLM Engineering, 11-AI Practitioner AIF-C01, 12-Blogs, Extras
    target_prefixes = (
        "10-LLM Engineering/",
        "11-AI Practitioner AIF-C01/",
        "12-Blogs/",
        "Extras/"
    )
    
    for line in lines:
        if line.startswith("?? "):
            filepath = line[3:].strip().strip('"')
            if filepath.startswith(target_prefixes):
                untracked_files.append(filepath)
                
    if not untracked_files:
        log_message("No untracked files left to commit for Phase B!")
        return
        
    # Sort files to commit them in logical order (e.g. LLM Engineering Week 1 first)
    untracked_files.sort()
    
    # Pick the first file
    file_to_commit = untracked_files[0]
    full_path = os.path.join(workspace, file_to_commit)
    
    log_message(f"Selected file to commit today: {file_to_commit}")
    
    # Personalize and redact file
    personalize_and_redact(full_path)
    
    # Git add
    add_res = subprocess.run(["git", "add", file_to_commit], cwd=workspace, capture_output=True, text=True)
    if add_res.returncode != 0:
        log_message(f"Error running git add: {add_res.stderr}")
        return
        
    # Commit message based on path/file basename
    basename = os.path.basename(file_to_commit)
    folder_name = file_to_commit.split('/')[0]
    commit_msg = f"Completed study material: {basename} ({folder_name})"
    
    # Git commit
    commit_res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=workspace, capture_output=True, text=True)
    if commit_res.returncode != 0:
        log_message(f"Error running git commit: {commit_res.stderr}")
        return
        
    log_message(f"Successfully committed: {commit_msg}")
    
    # Git push
    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=workspace, capture_output=True, text=True)
    if push_res.returncode != 0:
        log_message(f"Error running git push: {push_res.stderr}")
        return
        
    log_message("Successfully pushed commit to GitHub! Green dot achieved.")

if __name__ == "__main__":
    main()
