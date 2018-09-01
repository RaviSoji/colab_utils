# Minimize boilerplate code for Google's Colaboratory Notebooks

__Target Audience__:
- Users who want [Colab Notebooks + Google Drives] 
   to work like [Jupyter Notebooks + hard disks] on their local machines.
- Experienced with writing Python code to manage data and train models.
- Familiar with Jupyter and/or Colaboratory notebooks.

__Dependencies__
- A [Google account](https://accounts.google.com/signup)
- A [Colab notebook](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=-Rh3-Vt9Nev9)

__Background__
1. Skim the \"Working with Python\" and \"System Aliases\" sections in 
    [Colab Overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb).

2. All files and folders on your Google Drive have two important attributes.
   - `'title'`: this is what we typically call the `filename` or `basename`.
   - `'id'`: a unique ID for a specific file or folder. 
      In order to download anything from Google Drive to the Colab notebook, 
       you need this ID; 
       when you upload new files or folders from your Colaboratory to your 
       Google Drive, each is assigned a unique ID as well.
      This package also makes getting this information easy.

3. Do not conflate your Colaboratory and Google Drive directory structures.
   They are separate from one another.

## Setup and Installation
1. Open your __Colab__ notebook. 
   None of the following code will run in IPython or Jupyter notebook.

2. Set the `Runtime type` for your notebook.
    - At the top of the page, click `Runtime`. 
    - Then, in the drop-down menu, click `Change runtime type`.
    - Set `Runtime type` to `Python 3`.
    - If you want GPU acceleration, which you probably do, 
       set `Hardware accelerator` to `GPU`.
    - Click `Save`.

3. Clone this package by running the following in a Colab notebook cell.
    ```
    !git clone https://github.com/RaviSoji/colab_utils.git  # Don't forget "!".
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
    and pasting into the `verification code` field.
   Remember to press `<enter>` on your keyboard.

3. Now, you can use this package to do the things you wish were easier to do.

## List contents of a directory in your Google Drive
- The default behavior is to use the root directory of your Google Drive.
  ```
  In [1]: colab_utils.ls_gdrive(drive)
  Out[1]: {'a_sample_folder': 'WWWWWWWWWWWWWWWWWWWWWWWWWWW',
           'Colab Notebooks': 'XXXXXXXXXXXXXXXXXXXXXXXXXXX',
           'Getting started': 'YYYYYYYYYYYYYYYYYYYYYYYYYYY',
           'sample_nb.ipynb': 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZ'}
  ```
- If you want to list contents of a specific directory, 
   supply its Google Drive ID.
  ```
  In [1]: root_contents = colab_utils.ls_gdrive(drive)
  In [2]: colab_utils.ls_gdrive(drive, root_contents['a_sample_folder'])
  Out[2]: {'some_stuff': 'AAAAAAAAAAAAAAAAAAAAAAAAAAA',
           'more_stuff': 'BBBBBBBBBBBBBBBBBBBBBBBBBBB'}
  ```

## Get the ID of any directory, file, or path in your Google Drive
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
- I find that sticking with absolute paths promotes code clarity.

## Upload (i.e. \"push\") from your Colaboratory to your Google Drive
``` python
# Generate some random data for us to save.
import numpy as np
data = np.random.randint(0, 100, (10, 10))

# Save data to colaboratory.
import os
colaboratory_data_dir = os.path.join('.', 'data')
os.mkdir(colaboratory_data_dir)
colaboratory_save_path = os.path.join(colaboratory_data_dir, 'random_data.npy')
np.save(colaboratory_save_path, data)

# Upload data to Google Drive.
google_drive_save_dir = os.path.join('a_sample_folder')
google_drive_save_dir_id = colab_utils.get_gdrive_id(drive,
                                                     google_drive_save_dir)
colab_utils.push_to_gdrive(drive,
                           colaboratory_save_path,
                           google_drive_save_dir_id)
```

## Download (i.e. \"clone\") from your Google Drive to your Colaboratory
