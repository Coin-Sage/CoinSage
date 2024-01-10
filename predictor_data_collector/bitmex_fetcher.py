import hydra
from omegaconf import DictConfig
from bitmex_dataset import BitmexDataset  # Import your BitmexDataset class
import os
import django
import sys

# Get the absolute path to the config file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '../configs/hydra/predictor_data_collector/bitmex_config.yaml')

# Add the project directory to the sys.path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
django_project_directory = os.path.join(project_directory, 'CoinSageWeb')
sys.path.append(project_directory)
sys.path.append(django_project_directory)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoinSageWeb.settings')
# Initialize Django
django.setup()

os.environ['HYDRA_FULL_ERROR'] = '1'


@hydra.main(
    config_path="../configs/hydra/predictor_data_collector", config_name="bitmex_config", version_base="1.1"
)
def bitmex_fetcher(cfg: DictConfig):
    # Create an instance of BitmexDataset with Hydra configurations
    bitmex_dataset = BitmexDataset(cfg)

    # Call the get_dataset method
    dataset = bitmex_dataset.get_dataset()

    print(dataset)


if __name__ == '__main__':
    bitmex_fetcher()
