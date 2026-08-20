# main.py
from glm_client import GLMClient
from project_library import ProjectLibrary

def main():
    """
    Main entry point for the GLM-5.3 lightweight client application.
    """
    print("Initializing GLM-5.3 Client (Free through October)...")
    
    library = ProjectLibrary()
    client = GLMClient()

    project_name = "sample_vibe_app"
    sample_files = {
        "main.py": "print('Hello from GLM-5.3 local project!')\n"
    }
    
    print(f"Loading local project library: '{project_name}'...")
    library.save_project(project_name, sample_files)
    
    project_context = library.load_project_files(project_name)

    task_prompt = "Refactor main.py to include a CLI argument parser using argparse."
    print(f"Sending task to GLM-5.3: '{task_prompt}'")

    generated_code = client.generate_code(task_prompt, project_context)
    
    print("\n--- GLM-5.3 Generated Code Output ---")
    print(generated_code)

    if generated_code and not generated_code.startswith("# Error"):
        library.save_project(project_name, {"main.py": generated_code})
        print(f"\n[Success] Project '{project_name}' updated locally.")

if __name__ == "__main__":
    main()
