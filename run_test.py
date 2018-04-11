import os
from arguments import Arguments
from data import CreateDataLoader
from models import create_model
from util.visualizer import Visualizer
from util import html


if __name__ == '__main__':
    args = Arguments().parse()
    #args.nThreads = 1   # test code only supports nThreads = 1
    #args.batchSize = 1  # test code only supports batchSize = 1
    #args.serial_batches = True  # no shuffle
    #args.no_flip = True  # no flip

    data_loader = CreateDataLoader(args)
    dataset = data_loader.load_data()
    model = create_model(args)
    visualizer = Visualizer(args)
    # create website
    web_dir = os.path.join(args.results_dir, 'inference')
    webpage = html.HTML(web_dir, 'inference')
    # test
    for i, data in enumerate(dataset):
        if i >= args.how_many:
            break
        model.set_input(data)
        model.test()
        visuals = model.get_current_visuals()
        img_path = model.get_image_paths()
        img_size = model.get_image_sizes()
        print('%04d: process image... %s' % (i, img_path))
        visualizer.save_images(webpage, visuals, img_path, size=img_size)

    webpage.save()
