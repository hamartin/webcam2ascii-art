# Webcam to ASCII art
This script grabs frames from your webcam using OpenCV, converts the frame into grayscale, does some average pooling on the image and convert the pooled pixels into characters.
When the conversion is done, it prints the "ASCII art".

## Running the application
There are no required arguments, but at the current time, the application will fail without the --webcam-grayscale argument.

``` bash
python webcam2ascii.py --webcam-flip --webcam-grayscale
```

You can get information about the arguments the application takes by running the following command.

``` bash
python webcam2ascii.py --help
```

## Requirements
The script needs OpenCV, Pillow and Numpy.

``` bash
pip install -r requirements.txt
```

## Virtual environments
I use both conda and pythons venv module. It depends on which host I am working on.
This script has been developed and tested on python 3.12.

For the sake of simplification I will be calling the virtual environments in this explanation for "venv". You can call them whatever you want.

### Conda
Create a new virtual environment.

``` bash
conda create --name venv python=3.12
```

Activate the new virtual environment.

``` bash
conda activate venv
```

The virtual environment is now ready for install required modules using pip.
When your done with working in the virtual environment, you can deactivate it by running the following command.

``` bash
conda deactivate
```

### Python venv module
Create a new virtual environment.
Note that when using pythons venv module, the virtual environment will be for the python version installed on the host.
Also note that if you upgrade your local python, then you might need to recreate your virtual environment.

``` bash
python -m venv venv
```

Activate the virtual environment.

``` bash
source venv/bin/activate
```

The virtual environment is now ready for installing the required modules using pip.
When your done with working in the virtual environment, you can deactivate it by running the following command.

``` bash
deactivate
```