import pandas as pd
from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(
    input_path: Path = config.RAW_DATA_DIR / "data.csv",
    ):
    """
    Load data from locally downloaded dataset.
    """
    
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

    # df = eliminate_outliers(df)
    
    # df.to_csv(output_path, index=False)

    return FileIO().load(filepath)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
