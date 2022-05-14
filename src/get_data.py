## read params
## Process
## Return Dataframe

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    """
    This function reads the params.yaml file
    :param config_path:
    :return: Configuration
    """
    with open(config_path) as yml_file:
        config = yaml.safe_load(yml_file)

    return config

def get_data(config_path):
    """
    its reads the data from the config_path and return dataframe
    :param config_path:
    :return: dataframe
    """
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path)
    #print(df.head())
    return df



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_arg = args.parse_args()
    get_data(config_path=parsed_arg.config)