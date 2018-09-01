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
    """ Lists content in a Google Drive directory. """
    gnarly_string = "'{}' in parents and trashed=false"

    if gdrive_directory_id is None:
        gdrive_directory_id = 'root'

    listfile_arg = {'q': gnarly_string.format(gdrive_directory_id)}
    gdrive_files = gdrive.ListFile(listfile_arg)

    title_to_id_dict = dict()

    for gdrive_file in gdrive_files.GetList():
        key = gdrive_file['title']
        value = gdrive_file['id']

        title_to_id_dict[key] = value

    return title_to_id_dict


def get_gdrive_id(gdrive, gdrive_fpath, gdrive_parent_directory_id=None):
    """ Finds the ID of a file. """
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
        assert type(fpath_parts) == tuple
        assert len(fpath_parts) > 1

        for part in fpath_parts[:-1]:
            gdrive_parent_directory_id = current_ls_dict[part]
            current_ls_dict = ls_gdrive(gdrive, gdrive_parent_directory_id)

        last_part = fpath_parts[-1]

        return current_ls_dict[last_part]


def push_to_gdrive(gdrive, fpath_to_upload, gdrive_save_directory_id):
    """ Uploads content to Google Drive from Google Colaboratory. """
    createfile_arg = {'parents': [{'id': gdrive_save_directory_id}]}
    gdrive_file = gdrive.CreateFile(createfile_arg)
    gdrive_file.SetContentFile(fpath_to_upload)
    gdrive_file['title'] = os.path.basename(fpath_to_upload)
    gdrive_file.Upload()

    # print(gdrive_file['id'])
    # print(gdrive_file['title'])
    # print(gdrive_file['parents'])

    return gdrive_file


def pull_from_gdrive(gdrive, gdrive_id):
    """ Downloads content from Google Colaboratory to Google Drive. """
    gdrive_file = gdrive.CreateFile({'id': tmp_saved['id']})
    gdrive_file.GetContentFile(tmp_loaded['title'])

    return gdrive_file
