import subprocess

def get_git_diff(path: str):
    try:
        result = subprocess.run(["git", "diff"], cwd=path, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[diff error] {e}"
