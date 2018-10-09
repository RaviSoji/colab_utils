# Utility functions for Google Colaboratory

__Dependencies__
- A [Google account](https://accounts.google.com/signup)
- A [Colab notebook](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=-Rh3-Vt9Nev9)

__Background__
- Skim the \"Working with Python\" and \"System Aliases\" sections in 
   [Colab Overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb).

## Setup and Installation
1. Open your __Colab__ notebook. 
   None of the following code will run in IPython or Jupyter notebook.
2. Set the `Runtime type` for your notebook.
    - At the top of the page, click the `Runtime` tab. 
    - Then, in the drop-down menu, click `Change runtime type`.
    - Set `Runtime type` to `Python 3`.
    - If you want GPU acceleration, which you probably do, 
       set `Hardware accelerator` to `GPU`.
    - Click `Save`.
3. Clone this package by running the following in a Colab notebook cell.
    ```
    !git clone https://github.com/RaviSoji/colab_utils.git  # Include the "!".
    ```

## Usage
1. Import this package and create your Google Drive object.
    ``` python
    import colab_utils
    drive = colab_utils.get_gdrive()
    ```
    - Running this should display something like the following.
       ```
       Go to the following link in your browser:
       https://accounts.google.com/o/oauth2/auth?redirectXXXXXXXXXXXXXXXXX
       Enter verification code: ___________________
       ```
2. Authenticate your Google Drive object by clicking the link,
    supplying consent, copying the displayed code, 
    and pasting it into the `verification code` field.
   Remember to press `<enter>` on your keyboard.
3. Now, you can use this package to do the things you wish were easier to do.

## Upload (i.e. \"push\") files from your Colaboratory to your Google Drive
``` python
colab_utils.push_to_gdrive(drive, colaboratory_path, google_drive_directory)
```

## Download (i.e. \"pull\") files from your Google Drive to your Colaboratory
``` python
colab_utils.pull_from_gdrive(drive, google_drive_path, colaboratory_directory)
```

## List contents of a directory in your Google Drive
- The default behavior is to use the root directory of your Google Drive.
  ```
  In [1]: colab_utils.ls_gdrive(drive)
  Out[1]: {'a_sample_folder': 'WWWWWWWWWWWWWWWWWWWWWWWWWWW',
           'Colab Notebooks': 'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
           'Getting started': 'YYYYYYYYYYYYYYYYYYYYYYYYYYY',
           'sample_nb.ipynb': 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZ'}
  ```
- The output is a dictionary, 
   where keys are files in the directory and 
   values are unique Google Drive IDs.
- If you want to list contents of a specific directory, 
   supply its Google Drive ID.
  ```
  In [1]: root_contents = colab_utils.ls_gdrive(drive)
  In [2]: colab_utils.ls_gdrive(drive, root_contents['a_sample_folder'])
  Out[2]: {'some_stuff': 'AAAAAAAAAAAAAAAAAAAAAAAAAAA',
           'more_stuff': 'BBBBBBBBBBBBBBBBBBBBBBBBBBB'}
  ```

## Get the Google Drive ID of a directory or file path in your Google Drive
- Default behavior assumes the given path is relative to the root directory.
  ```
  In [1]: colab_utils.get_gdrive_id(drive, 'a_sample_folder/some_stuff')
  Out[1]: 'AAAAAAAAAAAAAAAAAAAAAAAAAAA'
  ```

- If you would like to use a relative path, 
   supply the ID of its parent directory.
  ```
  In [1]: parent_id = colab_utils.get_gdrive_id(drive, 'a_sample_folder')
  In [2]: colab_utils.get_gdrive_id(drive, 'more_stuff', parent_id)
  Out[2]: 'BBBBBBBBBBBBBBBBBBBBBBBBBBB'
  ```
