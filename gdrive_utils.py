import os

from pathlib import Path
from subprocess import call


def install_pydrive():
    """ See https://colab.research.google.com/notebooks/io.ipynb. """
    call(['pip', 'install', '-U', '-q', 'PyDrive'])


def get_gdrive():
    """ Installs pydrive and returns an authenticated GoogleDrive object. """
    install_pydrive()

    from google.colab import auth  # Will throw error if not run from a Colab.
    from oauth2client.client import GoogleCredentials
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    # Authenticate and create the PyDrive client.
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    gdrive = GoogleDrive(gauth)

    return gdrive


def ls_gdrive(gdrive, gdrive_directory_id=None):
    gnarly_string = "'{}' in parents and trashed=false"

    if gdrive_directory_id is None:
        gdrive_directory_id = 'root'

    listfile_arg = {'q': gnarly_string.format(gdrive_directory_id)}
    files = gdrive.ListFile(listfile_arg)

    title_to_id_dict = dict()

    for file in files.GetList():
        key = file['title']
        value = file['id']

        title_to_id_dict[key] = value

    return title_to_id_dict


def get_gdrive_id(gdrive, gdrive_fpath, gdrive_parent_directory_id=None):
    fpath_parts = Path(gdrive_fpath).parts

    if fpath_parts[0] == os.sep:
        fpath_parts = fpath_parts[1:]
        gdrive_parent_directory_id = 'root'

    elif gdrive_parent_directory_id is None:
        gdrive_parent_directory_id = 'root'

    current_ls_dict = ls_gdrive(gdrive, gdrive_parent_directory_id)

    if len(fpath_parts) == 1:
        return current_ls_dict[fpath_parts[0]]

    else:
        for part in fpath_parts[:-1]:
            gdrive_parent_directory_id = current_ls_dict[part]
            current_ls_dict = ls_gdrive(gdrive, gdrive_parent_directory_id)

        last_part = fpath_parts[-1]

        return current_ls_dict[last_part]


def push_to_gdrive(gdrive, fpath_to_upload, gdrive_save_directory_id):
    file = gdrive.CreateFile({'parents': [{'id': gdrive_save_directory_id}]})
    file.SetContentFile(fpath_to_upload)
    file.Upload()

    # print(file['id'])
    # print(file['title'])
    # print(file['parents'])

    return file


def clone_from_gdrive(gdrive, gdrive_id):
    gdrive_file = drive.CreateFile({'id': tmp_saved['id']})
    gdrive_file.GetContentFile(tmp_loaded['title'])

    return gdrive_file
