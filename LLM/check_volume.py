import modal
import os

volume = modal.Volume.from_name("llama3-finetune-volume")
app = modal.App("volume-checker")

@app.function(volumes={"/model_root": volume})
def list_files():
    volume.reload() # Sync files
    
    print("--- 🚀 Checking contents of your 'llama3-finetune-volume' ---")
    
    model_dir = "/model_root"
    
    if not os.path.exists(model_dir):
        print(f"Error: The root directory {model_dir} does NOT exist.")
        return

    try:
        # Recursively list all files and directories
        print(f"Listing all files in: {model_dir}")
        for root, dirs, files in os.walk(model_dir):
            # Don't print the root path every time, just the sub-path
            path = root.replace(model_dir, "")
            if path == "":
                path = "/"

            print(f"\n📁 Directory: {path}")
            
            if not dirs and not files:
                print("   ... (empty) ...")
                
            for d in dirs:
                print(f"   [DIR]  {d}")
            for f in files:
                print(f"   [FILE] {f}")
                
    except Exception as e:
        print(f"An error occurred while listing files: {e}")
        
    print("\n--- ✅ Check complete. ---")

@app.local_entrypoint()
def main():
    print("Connecting to Modal to read the volume...")
    list_files.remote()