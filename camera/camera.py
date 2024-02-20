"""
Module that handles all interaction with the chosen webcamera.
"""


import argparse

import cv2
import numpy as np

from PIL import Image, ImageDraw, ImageFont


class CameraException(Exception):
    pass
    

class Camera():

    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self._init_webcam()
        self.font = ImageFont.truetype("cour.ttf", args.ascii_font_size)
    
    def __repr__(self) -> str:
        return f"Camera(args={self.args})"
        
    def __str__(self) -> str:
        return self.__repr__()
        
    def _init_webcam(self) -> None:
        self.cap = cv2.VideoCapture(self.args.webcam_id)
        if self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) != self.args.webcam_width:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.args.webcam_width)
        if self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) != self.args.webcam_height:
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.args.webcam_height)
        if self.cap.get(cv2.CAP_PROP_FPS) != self.args.webcam_fps:
            self.cap.set(cv2.CAP_PROP_FRAME_FPS, self.args.webcam_fps)
        if self.cap.get(cv2.CAP_PROP_BUFFERSIZE) != self.args.webcam_buffersize:
            self.cap.set(cv2.CAP_PROP_BUFFERSIZE, self.args.webcam_buffersize)
        
    def _destroy_all_windows(self) -> None:
        cv2.destroyAllWindows()
        
    def get_ascii_frame(self) -> str:
        frame = self.read_frame()
        frame = normalize_frame(frame)

        ret = ""
        for row_start in range(0, frame.shape[0], self.args.ascii_font_size):
            row_end = min(row_start+self.args.ascii_font_size, frame.shape[0])
            for col_start in range(0, frame.shape[1], self.args.ascii_font_size):
                col_end = min(col_start+self.args.ascii_font_size, frame.shape[1])
                sub_array = frame[row_start:row_end, col_start:col_end]
                average = np.average(sub_array)
                index = int(average*(len(self.args.ascii_translation_table)-1))
                ret += self.args.ascii_translation_table[index]
                if col_end%frame.shape[1] == 0:
                    ret += "\n"
        return ret
        
    def get_ascii_image(self) -> Image.Image:
        ascii_frame = self.get_ascii_frame()
        _t = ascii_frame.split("\n")
        
        image = Image.new("L", (self.args.webcam_height, self.args.webcam_width))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), ascii_frame, fill="white", font=self.font)

        return image
        
    def read_frame(self) -> np.ndarray:
        if not self.isOpened():
            raise CameraException("The camera reports it is not initialized before trying to read frame.")
        ret, frame = self.cap.read()
        if not ret:
            raise CameraException("The camera did not return a frame. Something went wrong!")
        if self.args.webcam_flip:
            frame = cv2.flip(frame, 1)
        if self.args.webcam_grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame
        
    def isOpened(self) -> bool:
        return self.cap.isOpened()
        
    def release(self) -> None:
        self.cap.release()
        self._destroy_all_windows()
        
    def show_video_stream(self) -> None:
        if not self.isOpened():
            self._init_webcam()
        while self.isOpened():
            frame = self.read_frame()
            cv2.imshow("Webcam stream", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        self._destroy_all_windows()
        
        
def normalize_frame(frame: np.ndarray, denominator: float=255.0) -> np.ndarray:
    assert isinstance(frame, np.ndarray)
    assert frame.ndim == 2, f"The frame must be two dimensional, not {frame.ndim} dimensional."
    return frame/denominator