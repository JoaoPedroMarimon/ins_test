import cv2
import numpy as np
import qimage2ndarray
from PySide6.QtCore import Signal, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout
from src.IHM.src.components.video_preview.videoqthread import VideoQThread, get_rtsp_url
from src.IHM.src.components.video_preview.photo_viewer import PhotoViewer
from src.IHM.src.config import Config


class VideoPreview(QWidget):
    onVideoOpen = Signal()
    onVideonotOpened = Signal()
    def __init__(self, parent=None):
        """
        This component has the resposability to show the images from the VideoQThread class,
         passing the images and setting in Photoviewer
        """
        super().__init__(parent)
        _config = Config()
        self._creating_instances(_config.get_camera_config())
        self._adjusting_photo_viewer()

    def _creating_instances(self, config_camera:dict = None):
        self.video_thread = None
        if config_camera is None:
            self._camera_source = get_rtsp_url("192.168.1.108", "admin", "admin123", subtype=1)
        else:
            self._camera_source = get_rtsp_url(**config_camera,subtype=1)
        self._size: tuple[int, int] = (self.parent().height(),self.parent().width())
        self.photo_viewer = PhotoViewer(self)

    def _adjusting_photo_viewer(self):
        self.vertical_layout = QVBoxLayout(self)
        self.photo_viewer.resize(QSize(*self._size))
        self.vertical_layout.addWidget(self.photo_viewer)

    def start_video(self):
        self.video_thread = VideoQThread(self._camera_source, self)
        self.video_thread.imageSig.connect(self._update_video_label)
        self.video_thread.videoOpenedSig.connect(self._on_video_open)
        self.video_thread.videoNotOpenedSig.connect(self._on_video_not_opened)

        self.video_thread.start()

    def _update_video_label(self, frame: np.ndarray):
        self._latest_frame = frame
        self._size = (self.parent().width(),self.parent().height())
        self.setGeometry(0,0,self.parent().width(),self.parent().height())
        frame = cv2.resize(frame,self._size, cv2.INTER_AREA)
        q_image = qimage2ndarray.array2qimage(frame)
        pixmap = QPixmap.fromImage(q_image)
        self.photo_viewer.set_photo(pixmap)
        self.photo_viewer.fitInView()

    def _on_video_open(self):
        self.onVideoOpen.emit()

    def _on_video_not_opened(self):
        self.onVideonotOpened.emit()
