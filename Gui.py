import FreeSimpleGUI as sg
from zip_creator import make_archive

# Create GUI elements
label_1 = sg.Text("Select files to compress: ")
input_1 = sg.Input(key="file_input")
choose_button_1 = sg.FilesBrowse("Choose", key="files")

label_2 = sg.Text("Select destination folder: ")
input_2 = sg.Input(key="folder_input")
choose_button_2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

# Create the main window with all elements
window = sg.Window("Zipfile - Hyperbar",
                   layout=[[label_1, input_1, choose_button_1],
                           [label_2, input_2, choose_button_2],
                           [compress_button, output_label]])

# Main application loop
while True:
    event, values = window.read()

    # Handle window closure
    if event == sg.WINDOW_CLOSED:
        break

    # Handle compression button click
    if event == "Compress":
        filepaths = values["files"].split(";")
        folder = values["folder"]

        # Validate inputs
        if not filepaths or not folder:
            window["output"].update("Please select both files and destination folder", text_color="red")
            continue

        try:
            make_archive(filepaths, folder)
            window["output"].update("Compression completed successfully", text_color="green")
        except Exception as e:
            window["output"].update(f"An error occurred: {str(e)}", text_color="red")

    # Optional: Clear input fields after successful compression
    if event == "Compress" and window["output"].get() == "Compression completed successfully":
        window["file_input"].update("")
        window["folder_input"].update("")

# Close the window
window.close()

