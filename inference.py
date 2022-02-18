
from array import array
import cv2
import numpy as np
from PIL import Image as PImage
from fastai.vision import *

class Mnist:
    def __init__(self, base_dir, fn=None) -> None:
        self.load_learn = load_learner(base_dir)

    def infer(self, fn):
        if type(fn) == str:
            img = cv2.imread(fn)
        else:
            img1 = np.array(PImage.open(fn))
            img = np.repeat(img1[..., np.newaxis], 3, axis=-1)

        pil_im = PImage.fromarray(img) 

        x = pil2tensor(pil_im ,np.float32)

        preds_num = self.load_learn.predict(Image(x))[2]

        idx = preds_num.argmax().item()

        return ['3', '7'][idx]
    


if __name__ == '__main__':
    base_dir = Path('.')
    model = Mnist(base_dir)
    print(model.infer('3.jpg'))