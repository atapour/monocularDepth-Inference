import torch.utils.data
from data.base_data_loader import BaseDataLoader


def CreateDataLoader(args):
    data_loader = CustomDatasetDataLoader()
    print(data_loader.name())
    data_loader.initialize(args)
    return data_loader


def CreateDataset(args):
    dataset = None
    from data.single_dataset import SingleDataset
    dataset = SingleDataset()
    print("dataset [%s] was created" % (dataset.name()))
    dataset.initialize(args)
    return dataset


class CustomDatasetDataLoader(BaseDataLoader):
    def name(self):
        return 'CustomDatasetDataLoader'

    def initialize(self, args):
        BaseDataLoader.initialize(self, args)
        self.dataset = CreateDataset(args)
        self.dataloader = torch.utils.data.DataLoader(
            self.dataset,
            batch_size=args.batchSize,
            shuffle=not args.serial_batches,
            num_workers=int(args.nThreads))

    def load_data(self):
        return self

    def __len__(self):
        return min(len(self.dataset), self.args.max_dataset_size)

    def __iter__(self):
        for i, data in enumerate(self.dataloader):
            if i >= self.args.max_dataset_size:
                break
            yield data
