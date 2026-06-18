import os

KNOWN_FACES_DIR = "known_faces"

print("Folders found in known_faces:")
for folder in os.listdir(KNOWN_FACES_DIR):
    if os.path.isdir(os.path.join(KNOWN_FACES_DIR, folder)):
        print("→", folder)

print("\nChecking images inside each folder:")
for folder in os.listdir(KNOWN_FACES_DIR):
    folder_path = os.path.join(KNOWN_FACES_DIR, folder)
    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        print(f"📁 {folder} → {len(files)} images")
        for f in files[:5]:   # show first 5 files
            print("   ", f)