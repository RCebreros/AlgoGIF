import numpy as np
from abc import ABC, abstractmethod

class GIFMaker(ABC):
    def __init__(self, dataset, gif_n_slides=3, gif_slide_spd=1):
        self.dataset = None
        self._plot_captures = []
        self._n_slides = gif_n_slides
        self._gif_ms_speed = gif_slide_spd * 1000
        self._setValidDataset(dataset)

    def _setValidDataset(self, dataset):
        if not isinstance(dataset, np.ndarray):
            dataset = np.array(dataset)
        if dataset.ndim == 1:
            indices = [[i] for i in range(len(dataset))]
            values = dataset.reshape(-1, 1)
            dataset = np.hstack((indices, values))
        elif dataset.ndim > 3:
            raise Exception(f'Supported dataset dimensions is 1-3. Input shape: {dataset.shape}')
        self.dataset = dataset

    @abstractmethod
    def _savePlotImage_2D(self):
        ...

    @abstractmethod
    def _savePlotImage_3D(self):
        ...

    def save(self, filename):
        if '.' not in filename:
            filename = f'{filename.strip()}.gif'
        self._plot_captures[0].save(filename,
                                    save_all=True,
                                    append_images=self._plot_captures[1:],
                                    duration=self._gif_ms_speed,
                                    loop=0)
