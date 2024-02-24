#File Manager
This is a primitive file manager written in Python.

#Project Structure

Create a project folder and organize it as follow:

'''plaintext

file_manager/

|--file_manager.py
|--settings.ini
|--README.md

git clone https://github.com/Nour275/File_Manager.git

cd File_Manager

#Run the File manager:
python file_manager.py

#Available Commands:
Create_Folder foldername : Create a new folder.
Delete_Folder folder_name : Delete an existing folder.
List_Folders : List all folders in the current directory.
Create_File file_name : Create a new blank file.
Write_To_File file_name "Content" : Write content to a file.
View_file file_name : View the content of a file.
Delete_File file_name : Delete an existing file.
Copy_File source_file destination_folder : copy a file to another folder.
Move_File source_file destination_folder : Move a file to another folder.
Rename_File old_name new_name : Rename a file.

To exit the File Manager, simply type 'exit'.


Notes:
The file manager operates within working folders specified in 'settings.ini'.
Ensure that the python version is compatible (e.g., python3)


