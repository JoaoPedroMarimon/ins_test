import multiprocessing
import time

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal


class VideoQThread(QThread):
    """
    This Class have the responsibility to get the video from the camera

    The Signals act like pass through class functions.
    A Parent Class who use the VideoQThread can pass functions to change ou send something in Parent class
    ImageSig - receive a function to send the image from the camera
    VideoOpenedSig - execute the function received when video open
    VideoNotOpenedSig - execute the function received when video NOT open
    frameNotRetSig - execute the function when have error to get the ret of the frame
    """
    imageSig = Signal(np.ndarray)
    videoOpenedSig = Signal()
    videoNotOpenedSig = Signal()
    frameNotRetSig = Signal()

    def __init__(self, source: str, parent=None, delay=0.02):
        super().__init__(parent)
        self._source = source
        self._delay = delay
        self._running = False

    def run(self):
        self._running = True
        succeeded, _ = try_camera_connection(self._source, 15)
        if not succeeded:
            self.videoNotOpenedSig.emit()
            return

        cap = cv2.VideoCapture(self._source)

        if not cap.isOpened():
            self.videoNotOpenedSig.emit()
            return

        self.videoOpenedSig.emit()
        while cap.isOpened() and self._running:
            ret, frame = cap.read()
            if not ret:
                self.frameNotRetSig.emit()
                break

            self.imageSig.emit(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            time.sleep(self._delay)
        cap.release()

    def stop(self):
        self._running = False


def try_camera_connection(source: str, timeout: float):
    succeeded = timed_out = False
    pool = multiprocessing.Pool(processes=1)
    async_obj = pool.apply_async(is_camera_working, (source,))

    try:
        succeeded = async_obj.get(timeout=timeout)

    except multiprocessing.TimeoutError:
        # Terminate the process if it times out
        if hasattr(async_obj, "terminate"):
            async_obj.terminate()
        else:
            pool.terminate()
        timed_out = True

    pool.close()
    pool.join()

    return succeeded, timed_out


def is_camera_working(src: str):
    result = False
    cap = cv2.VideoCapture(src)
    # Check if the camera opened successfully
    if cap.isOpened():
        result = True
        cap.release()  # Release the camera when done
    return result


def get_rtsp_url(server: str, login: str, password: str, rtsp_port=80, channel=1, subtype=0) -> str:
    url = f'rtsp://{login}:{password}@{server}:{rtsp_port}' \
          f'/cam/realmonitor?channel={channel}&subtype={subtype}'
    return url


def get_source_by_type(camera_type: str, config: dict):
    if camera_type == "dahuaIpCamera":
        return get_rtsp_url(**config)

    elif camera_type == "webcam":
        return config["source"]

    else:
        msg = f"Camera type '{camera_type}' is not listed as a valid source."
        raise NotImplementedError(msg)
