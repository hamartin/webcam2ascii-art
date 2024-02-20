"""
Module that contains helper functions.
"""


import argparse
import numpy as np


def get_arguments() -> argparse.Namespace:
    parser  = argparse.ArgumentParser()
    # Webcam settings and webcam input settings.
    parser.add_argument("--webcam-id", required=False, default=0, type=int, help="The cv2 ID of the webcam you wish to you.")
    parser.add_argument("--webcam-height", required=False, default=480, type=int, help="The height which to set the input webcam to.")
    parser.add_argument("--webcam-width", required=False, default=640, type=int, help="The width which to set the input webcam to.")
    parser.add_argument("--webcam-fps", required=False, default=30, type=int, help="The framerate to set the input camera to.")
    parser.add_argument("--webcam-buffersize", required=False, default=1, type=int, help="The buffersize to use on the camera.")
    parser.add_argument("--webcam-flip", required=False, default=False, action="store_true", help="Flip the image in the horisontal direction.")
    parser.add_argument("--webcam-grayscale", required=False, default=False, action="store_true", help="Convert the frame returned from the webcamera into grayscale.")
    
    # ASCII art settings.
    parser.add_argument("--ascii-font-size", required=False, default=12, type=int, help="The point size of the font.")
    parser.add_argument("--ascii-translation-table", required=False, default=".:-=+*#%@", type=str, help="The translation table to use.")
    return parser.parse_args()