import os
import shutil
from collections import defaultdict

def organize_files(source_directory):
    """
    Scans the specified directory and organizes files into subfolders
    based on their file extensions.

    Args:
        source_directory (str): The path to the directory to organize.
    """
    # Check if the source directory exists
    if not os.path.isdir(source_directory):
        print(f"Error: The directory '{source_directory}' does not exist.")
        return

    # Define a dictionary to map common file extensions to target folder names.
    # You can customize this dictionary to add more categories or specific extensions.
    # The keys are extensions (lowercase) and values are folder names.
    extension_to_folder = defaultdict(lambda: "Others")
    extension_to_folder.update({
        # Images
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
        '.bmp': 'Images', '.tiff': 'Images', '.webp': 'Images', '.svg': 'Images',
        '.heic': 'Images',

        # Documents
        '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents',
        '.txt': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents',
        '.xls': 'Documents', '.xlsx': 'Documents', '.odt': 'Documents',
        '.rtf': 'Documents', '.tex': 'Documents', '.epub': 'Documents',
        '.md': 'Documents', '.pages': 'Documents', '.key': 'Documents',
        '.numbers': 'Documents',

        # Audio
        '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio', '.aac': 'Audio',
        '.ogg': 'Audio', '.wma': 'Audio',

        # Video
        '.mp4': 'Videos', '.mov': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
        '.flv': 'Videos', '.wmv': 'Videos', '.webm': 'Videos',

        # Archives
        '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives', '.tar': 'Archives',
        '.gz': 'Archives', '.bz2': 'Archives',

        # Executables/Installers
        '.exe': 'Executables', '.dmg': 'Executables', '.app': 'Executables',
        '.msi': 'Executables', '.deb': 'Executables', '.rpm': 'Executables',

        # Programming/Code Files
        '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code',
        '.java': 'Code', '.c': 'Code', '.cpp': 'Code', '.h': 'Code',
        '.json': 'Code', '.xml': 'Code', '.php': 'Code', '.rb': 'Code',
        '.sh': 'Code', '.bat': 'Code', '.cs': 'Code',

        # Spreadsheets
        '.csv': 'Spreadsheets', '.ods': 'Spreadsheets',

        # Presentations
        '.odp': 'Presentations',

        # Fonts
        '.ttf': 'Fonts', '.otf': 'Fonts', '.woff': 'Fonts', '.woff2': 'Fonts',

        # Virtual Machine / Disk Images
        '.iso': 'Disk Images', '.vmdk': 'Disk Images', '.vhd': 'Disk Images'
    })

    print(f"\nStarting organization in: '{source_directory}'")
    files_moved_count = 0
    folders_created_count = 0

    # Iterate over all items (files and folders) in the source directory
    for item_name in os.listdir(source_directory):
        item_path = os.path.join(source_directory, item_name)

        # Skip directories and the script itself if it's in the same folder
        if os.path.isdir(item_path) or item_name == os.path.basename(__file__):
            continue

        # Get the file extension
        # os.path.splitext returns a tuple: ('filename', '.extension')
        file_name, file_extension = os.path.splitext(item_name)
        file_extension = file_extension.lower() # Convert to lowercase for consistent mapping

        # Determine the target folder based on the extension
        target_folder_name = extension_to_folder[file_extension]
        target_folder_path = os.path.join(source_directory, target_folder_name)

        try:
            # Create the target folder if it doesn't exist
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path)
                folders_created_count += 1
                print(f"Created folder: '{target_folder_name}'")

            # Define the destination path for the file
            destination_path = os.path.join(target_folder_path, item_name)

            # Handle cases where a file with the same name already exists in the destination
            # This appends a number to the file name (e.g., 'document(1).pdf')
            original_destination_path = destination_path
            counter = 1
            while os.path.exists(destination_path):
                name, ext = os.path.splitext(item_name)
                destination_path = os.path.join(target_folder_path, f"{name}({counter}){ext}")
                counter += 1

            # Move the file
            shutil.move(item_path, destination_path)
            files_moved_count += 1
            print(f"Moved: '{item_name}' -> '{target_folder_name}/'")

        except shutil.Error as e:
            print(f"Error moving '{item_name}': {e}. Skipping this file.")
        except OSError as e:
            print(f"OS Error for '{item_name}': {e}. Skipping this file.")
        except Exception as e:
            print(f"An unexpected error occurred for '{item_name}': {e}. Skipping this file.")

    print(f"\nOrganization complete!")
    print(f"Total files moved: {files_moved_count}")
    print(f"Total new folders created: {folders_created_count}")

if __name__ == "__main__":
    print("--- File Organizer & Sorter ---")
    while True:
        directory_path = input("Enter the directory path to organize (or 'exit' to quit): ").strip()
        if directory_path.lower() == 'exit':
            print("Exiting File Organizer. Goodbye!")
            break
        elif not directory_path:
            print("Path cannot be empty. Please enter a valid path.")
            continue
        
        # Normalize the path to handle various input formats (e.g., with/without trailing slash)
        normalized_path = os.path.abspath(directory_path)

        organize_files(normalized_path)
