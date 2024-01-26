from bitmex_dataset import BitmexDataset

DATASETS = [
    'Bitmex',
]

DATA_TYPES = ['train',
              'validation',
              'test'
              ]


def get_dataset(dataset_name, args):
    assert dataset_name in DATASETS, \
        f"Dataset {args.dataset_name} is not available."

    if dataset_name == 'Bitmex':
        btc = BitmexDataset(args)
        dataset = btc.get_dataset()

        return dataset


