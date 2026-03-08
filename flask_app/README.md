# VORA
VORA - Voice Operated Robotic Assistant

## Installation Procedure

`create a python environment`
```cmd
python -m venv venv
```

`activate the environment`
```cmd
.\venv\Scripts\activate.bat
```

`install necessary libraries`
```cmd
pip install -r requirements.py
```

## Setup
1. In windows you need to install `ffmpeg`.
    
    `To download`
    
    - Open the command prompt.
    - Download the `ffmpeg` using the below command.
    ```cmd
    winget install ffmpeg
    ``` 
    - Now note the path of the `ffmpeg` using the below command.
    ```cmd
    where ffmpeg
    ```

2. Create a `config.py` file in the root directory `VORA`.
3. Add the below format in the `config.py`.
    ```py
    host = '0.0.0.0'
    port = 5000
    ffmpeg_bin_folder = r"<path>"
    ```

## Run the server

`To run the flask server`
```cmd
python app.py
```