from mmseg.apis import show_result_pyplot
import numpy as np
import mmcv

if __name__ == '__main__':
    # dummy image and seg map
    img = np.ones((64,64,3), dtype=np.uint8)*255
    seg = np.zeros((64,64), dtype=np.uint8)
    seg[16:48,16:48]=1
    palette = np.array([[0,0,0],[0,255,0]])
    mmcv.imwrite(img, 'demo_image.png')
    show_result_pyplot('demo_image.png', (seg,), palette=palette, opacity=0.5)
