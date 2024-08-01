
import os.path as osp
import cv2, os
import numpy as np

from tqdm import tqdm
from glob import glob

if __name__ == '__main__':

    new_dir = osp.join('data', 'character_edge2color')
    os.makedirs(new_dir, exist_ok=True)

    for _dir in ['train', 'val']:
        print(f'processing dir : {_dir}')
        img_list = glob(osp.join('data', _dir, '*.png'))
        edge_dir = osp.join(new_dir, f'{_dir}_A')
        color_dir = osp.join(new_dir, f'{_dir}_B')
        for img_path in tqdm(img_list):

            img_base_name = osp.basename(img_path)
            img = cv2.imread(img_path)
            H, W, _ = np.shape(img)

            color = img[:, : W // 2]
            edge = img[:, W // 2:]

            cv2.imwrite(osp.join(edge_dir, img_base_name), edge)
            cv2.imwrite(osp.join(color_dir, img_base_name), color)


