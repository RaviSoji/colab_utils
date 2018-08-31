# Simple data management functions for Google Colab.

## Usage
Suppose you have a Google Colab notebook open, then:

1. Clone this repository.
    ``` python
    !git clone https://github.com/RaviSoji/colab_utils.git
    ```

2. Import this python package into your notebook.
    ``` python
    import colab_utils
    ```

3. Create your drive object and then authenticate it by copy and pasting 
    the key provided by the link in the prompt (remember to press enter).
    ``` python
    drive = colab_utils.get_gdrive()
    ```

4. Now, you can use the functions (I will add a demo Colab notebook soon).
