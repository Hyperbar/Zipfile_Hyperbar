# Import the zipfile module for creating ZIP archives
import zipfile
# Import pathlib for handling file paths in a platform-independent way
import pathlib

def make_archive(filepaths, dest_dir):
    """
    Create a ZIP archive containing the specified files.

    Args:
    filepaths (list): List of file paths to be included in the archive.
    dest_dir (str): Destination directory for the created archive.
    """

    # Create a Path object for the destination ZIP file
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    # Open a new ZIP file in write mode
    with zipfile.ZipFile(dest_path, "w") as archive:

        # Iterate through each file path in the provided list
        for filepath in filepaths:
            # Convert the file path to a Path object
            filepath = pathlib.Path(filepath)
            # Write the file to the ZIP archive
            # arcname=filepath.name ensures only the filename is used in the archive, not the full path
            archive.write(filepath, arcname=filepath.name)

# This block only executes if the script is run directly (not imported)
if __name__ == "__main__":
    # Call the make_archive function with example file paths and destination directory
    make_archive(filepaths=[r"C:\Users\sztre\Desktop\code word studi.txt",
                            r"C:\Users\sztre\Desktop\entree_recipes.csv"],
                 dest_dir=r"C:\Users\sztre\Desktop")