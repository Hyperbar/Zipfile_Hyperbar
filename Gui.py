import FreeSimpleGUI as sg

label_1 = sg.Text("Select files to compress: ")
input_1 = sg.Input()
choose_button_1 = sg.FileBrowse("Choose")

label_2 = sg.Text("Select destination folder: ")
input_2 = sg.Input()
choose_button_2 = sg.FolderBrowse("Choose")

window = sg.Window("Zipfile - Hyperbar")