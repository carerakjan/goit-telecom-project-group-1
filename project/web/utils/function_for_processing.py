import pandas as pd
from web.utils.scale_data import scale


def processing_input_data(input_data):
    # Створюємо DataFrame
    df = pd.DataFrame([input_data])

    print("Original DataFrame:", df.head())

    return scale(df)
