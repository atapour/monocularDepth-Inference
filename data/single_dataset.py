import os.path
from data.base_dataset import BaseDataset, get_transform
from data.image_folder import make_dataset
from PIL import Image


class TestDataset(BaseDataset):
    def initialize(self, opt):
        self.opt = opt
        self.root = opt.data_directory
        self.dir_A = os.path.join(opt.data_directory)

        self.A_paths = make_dataset(self.dir_A)

        self.A_paths = sorted(self.A_paths)

        self.transform = get_transform(opt)

    def __getitem__(self, index):
        A_path = self.A_paths[index]
        A_img = Image.open(A_path).convert('RGB')
        A_size = A_img.size

        A = self.transform(A_img)
        input_nc = 3

        return {'A': A, 'A_paths': A_path, 'A_sizes': A_size}

    def __len__(self):
        return len(self.A_paths)

    def name(self):
        return 'TestDataset'
