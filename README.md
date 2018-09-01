# Minimize boilerplate code for Google's Colaboratory Notebooks

__Target Audience__:
- Researchers and other users who want their [Colab Notebooks + Google Drives] 
   to work like [Jupyter Notebooks + hard disks] on their local machines, 
   without wasting time.
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

## Usage: Download and Import
1. Open your __Colab__ notebook. 
   None of the following code will run in IPython or Jupyter notebook.

2. Set the `Runtime type` for your notebook.
    - At the top of the page, click `Runtime`. 
    - Then, in the drop-down menu, click `Change runtime type`.
    - Set `Runtime type` to `Python 3`.
    - If you want GPU acceleration, which you probably do, 
       set `Hardware accelerator` to `GPU`.
    - Click `Save`.

2. Clone and import this package by running the following.
    ```
    !git clone https://github.com/RaviSoji/colab_utils.git
    import colab_utils
    ```

3. Create your Google Drive object.
    ``` python
    drive = colab_utils.get_gdrive()
    ```

    - Running this will display something like the following:
       ```
       Go to the following link in your browser:
   
       https://accounts.google.com/o/oauth2/auth?redirectXXXXXXXXXXXXXXXXX
   
       Enter verification code: ___________________
       ```
4. Authenticate your Google Drive object by clicking the link,
    supplying consent, copying the displayed code, 
    and pasting into the `verification code` field.
   Remember to press `<enter>` on your keyboard.

5. Now, you can use this package to do the things you wish were easier to do.

## Usage
__ls a directory in your Google Drive__

__Get the ID of a directory, file, or path in your Google Drive__


__\"clone\"/download content from your Google Drive to your Colaboratory__

__\"push\"/upload content from your Colaboratory to your Google Drive__
