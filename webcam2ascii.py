#!/usr/bin/env python3


import argparse

from camera import Camera
from utils import get_arguments


def main(args: argparse.Namespace, cap: Camera) -> None:
    while cap.isOpened():
        print("\033c", end="")
        print(cap.get_ascii_frame())


if __name__ == "__main__":

    args = get_arguments()
    cap = Camera(args)
    
    try:
        main(args, cap)
    except KeyboardInterrupt:
        print("User pressed CTRL^C -> Quitting!")
    finally:
        cap.release()