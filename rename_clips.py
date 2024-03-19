import os

def rename_clips(folder_path, names_file):
    # Read clip names from the text file
    with open(names_file, 'r') as file:
        clip_names = file.read().splitlines()
    
    # List all MP4 files in the folder
    mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
    print(mp4_files)
    
    # Ensure number of clips in names_file matches number of MP4 files
    if len(clip_names) != len(mp4_files):
        print("Number of clip names does not match number of MP4 files.")
        return
    
    # Rename MP4 files
    for i, mp4_file in enumerate(mp4_files):
        old_path = os.path.join(folder_path, mp4_file)
        if i < 9:
            new_name = f"0{i+1}. "
        else: 
            new_name = f"{i+1}. "
        new_name += clip_names[i] + ".mp4"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{mp4_file}' to \n\t'{new_name}'")

# Example usage
folder_path = r"C:\Users\theCode\Documents\clips\output"
names_file = "clips_names.txt"

rename_clips(folder_path, names_file)
