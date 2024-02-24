import os
import configparser
import shutil

def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config ['File Manager']['working_folder']

def main ():
    working_folder = load_settings()
    current_folder = working_folder

    while True:
        command = input(f'{current_folder}> Enter Command: ').strip()
        if command == 'exit':
            break

        elif command.startswith ('Create_Folder'):
            create_folder(current_folder, command.split(' ', 1)[1])

        elif command.startswith('Delete_Folder'):
            delete_folder(current_folder, command.split(' ',1)[1])

        elif command == ('List_Folders'):
            list_folders(current_folder)

        elif command.startswith ('Create_File'):
            create_file(current_folder, command.split(' ', 1)[1])

        elif command.startswith ('Write_To_File'):
            write_to_file(current_folder, *command.split(' ', 2)[1:])

        elif command.startswith ('View_File'):
            view_file(current_folder, command.split(' ', 1)[1])

        elif command.startswith ('Delete_File'):
            delete_file(current_folder, command.split(' ', 1)[1])

        elif command.startswith ('Copy_File'):
            copy_file(current_folder, *command.split(' ', 2)[1:])

        elif command.startswith ('Move_File'):
            move_file(current_folder, *command.split(' ', 2)[1:])

        elif command.startswith ('Rename_File'):
            rename_file(current_folder, *command.split(' ', 2)[1:])
       
def create_folder(current_folder, folder_name):
    folder_path = os.path.join(current_folder, folder_name)
    os.makedirs(folder_path)
    print(f'Folder "{folder_name}" created.')
       
def delete_folder(current_folder, folder_name):
    folder_path = os.path.join(current_folder, folder_name)
    os.rmdir(folder_path)
    print(f'Folder "{folder_name}" deleted.')

def list_folders(current_folder):
    folders = [f for f in os.listdir(current_folder) if os.path.isdir(os.path.join(current_folder,f))]
    print(f'Folders in {current_folder}: {", ".join(folders)}')

def create_file(current_folder, file_name):
    file_path = os.path.join(current_folder, file_name)
    with open(file_path, 'w'):
        pass #creating an empty file

    print(f'File "{file_name}" created.')


def write_to_file(current_folder, file_name, content):
    file_path = os.path.join(current_folder, file_name)
    with open(file_path, 'w') as file:
        file.write(content)

    print(f'Content written to "{file_name}".')

def view_file(current_folder, file_name, content):
    file_path = os.path.join(current_folder, file_name)
    with open(file_path, 'r') as file:
        content= file.read()


    print(f'Content of "{file_name}":\n{content}.')

def delete_file(current_folder, file_name):
    file_path = os.path.join(current_folder, file_name)
    os.remove(file_path)
    print(f'File "{file_name}" deleted.')

def copy_file(current_folder, source_file, destination_folder):
    source_path = os.path.join(current_folder, source_folder)
    destination_path = os.path.join(current_folder, destination_folder, source_file)
    shuril.copy2(source_path, destination_path)

    print(f'File "{source_fil}" copied to "{destination_folder}".')

def move_file(current_folder, source_file, destination_folder):
    source_path = os.path.join(current_folder, source_folder)
    destination_path = os.path.join(current_folder, destination_folder, source_file)
    shuril.move(source_path, destination_path)

    print(f'File "{source_file}" moved to "{destination_folder}".')

def rename_file(current_folder, old_name, new_name):
    old_path = os.path.join(current_folder, old_name)
    new_path = os.path.join(current_folder, new_name)
    os.rename(old_path, new_path)

    print(f'File "{old_name}" rename to "{new_name}".')


if __name__ == "__main__":
    main()
