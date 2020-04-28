import os
from pathlib import Path



class Config():
    DEFAULT_CONFIG_FILE = Path.joinpath(Path(__file__).parent.absolute(), "../../defaultData/default_config.yaml")
    TEST_CONFIG_FILE = Path.joinpath(Path(__file__).parent.absolute(), "../../defaultData/test_config.yaml")
    
    