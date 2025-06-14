from argparse import ArgumentParser

from mmseg.apis import inference_segmentor, init_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette

from PIL import Image
import numpy as np

def main():
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--palette',
        default='cityscapes',
        help='Color palette used for segmentation map')
    parser.add_argument('--out-file', default=None, help='Path to output file')
    args = parser.parse_args()


    # build the model from a config file and a checkpoint file
    model = init_segmentor(args.config, args.checkpoint, device=args.device)
    # test a single image
    result = inference_segmentor(model, args.img)
    # show the results
    show_result_pyplot(model, args.img, result, get_palette(args.palette),out_file=args.out_file, opacity=0.9)


if __name__ == '__main__':
    main()
