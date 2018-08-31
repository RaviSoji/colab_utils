# Convenient data management functions for Google Colaboratory.

## Usage
Suppose you have a Google Colab notebook open, then:

1. Clone this repository.
    ``` shell
    !git clone https://github.com/RaviSoji/colab_utils.git
    ```

2. Import this python package into your notebook.
    ``` shell
    import colab_utils
    ```

3. Create your drive object and then authenticate it by copy and pasting 
    the key provided by the link in the prompt (remember to press enter).
    ``` shell
    drive = colab_utils.get_gdrive()
    ```

4. Now, you can use the functions (I'll update this README later).
