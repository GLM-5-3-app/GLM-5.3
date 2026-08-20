# project_library.py
import os

class ProjectLibrary:
    """
    Manages local project library, code history, and context tracking on the user's machine.
    """
    def __init__(self, storage_path: str = "./glm_projects"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def save_project(self, project_name: str, files: dict):
        """Saves project files locally to maintain private state."""
        proj_dir = os.path.join(self.storage_path, project_name)
        os.makedirs(proj_dir, exist_ok=True)
        for file_name, content in files.items():
            file_path = os.path.join(proj_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

    def load_project_files(self, project_name: str) -> dict:
        """Loads all files for a given project to pass into GLM-5.3 context."""
        proj_dir = os.path.join(self.storage_path, project_name)
        if not os.path.exists(proj_dir):
            return {}
        
        files = {}
        for root, _, filenames in os.walk(proj_dir):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                rel_path = os.path.relpath(file_path, proj_dir)
                with open(file_path, "r", encoding="utf-8") as f:
                    files[rel_path] = f.read()
        return files
