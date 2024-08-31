import pandas as pd
from web.utils.scale_data import scale
from web.utils.get_main_features import main_features


def processing_input_data(input_data):
    # Создаем DataFrame
    df = pd.DataFrame([input_data])

    print("Original DataFrame:", df.head())

    return scale(df)
