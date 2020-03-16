########################################
# utility that contains a class that gets the configuration



########################################

import logging
import datetime

import json

class Config:
    """
    Class containing the parameters 
    """
    
    def __init__(self, config_path = './CSF_chenfu_config.json'):
        with open(config_path) as config_file:
            config_data = json.load(config_file)
            
            for key in config_data:
                setattr(self, key, config_data[key])
                
        self._init_logging()

        self.file_to_process = None
        
    def _init_logging(self):
        cur_date = datetime.datetime.now()
        
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("{0}/{1}.log".format(self.logs_dir, f"{cur_date.year}-{cur_date.month}-{cur_date.day}_{cur_date.hour}.{cur_date.minute}.{cur_date.second}"), mode="a"),
                logging.StreamHandler()]) 