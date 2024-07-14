from pathlib import Path

from loguru import logger
import pandas as pd
import numpy as np
from scipy import stats

from machine_failure_prediction import config
from machine_failure_prediction.config import PROCESSED_DATA_DIR
from machine_failure_prediction.config import DATA_DIR = PROJ_ROOT / "data"
from machine_failure_prediction.config import RAW_DATA_DIR = DATA_DIR / "raw"


def eliminate_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each row in dataframe, retain column values that are within
    3 standard deviations from the mean
    """
    
    initial_length = len(df)
    df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)].copy()
    print(f"Eliminated {initial_length - len(df)} outliers")
    return df


def main(
    input_path: Path = config.RAW_DATA_DIR / "data.csv",
    output_path: Path = config.PROCESSED_DATA_DIR / "features.csv",
):
    logger.info("Generating features from dataset...")

    df_raw = pd.read_csv(input_path)

    df = df_raw.rename(columns={
        "tempMode":"temp_mode",
        "AQ":"air_quality", 
        "USS":"proximity_sensor", 
        "CS":"current_usage", 
        "VOC":"voc_level", 
        "RP":"revolutions_per_minute", 
        "IP":"input_pressure",
        "Temperature":"temperature"
    })

    df = eliminate_outliers(df)
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()
