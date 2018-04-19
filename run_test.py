import os
from arguments import Arguments
from data import CreateDataLoader
from models import create_model
from util import save_images


if __name__ == '__main__':
    args = Arguments().parse()

    data_loader = CreateDataLoader(args)
    dataset = data_loader.load_data()
    model = create_model(args)

    for i, data in enumerate(dataset):
        if i >= args.how_many:
            break
        model.set_input(data)
        model.test()
        visuals = model.get_current_visuals()
        img_path = model.get_image_paths()
        img_size = model.get_image_sizes()
        print('%04d: processing image... %s' % (i, img_path))
        save_images(args.results_dir, visuals, img_path, size=img_size)
