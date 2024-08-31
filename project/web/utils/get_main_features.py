numerical_features = [
    "is_tv_subscriber",
    "is_movie_package_subscriber",
    "subscription_age",
    "reamining_contract",
    "download_avg",
    "upload_avg",
    "download_over_limit",
]

feature_titles = [
    "Підписник телевізійного пакету",
    "Підписник пакету фільмів",
    "Вік підписки",
    "Залишок контракту",
    "Середній об'єм завантаження",
    "Середній об'єм відвантаження",
    "Перевищення ліміту",
]


def get_feature_titles(features):
    mapping = dict(zip(numerical_features, feature_titles))
    return [mapping[f] for f in features]


def main_features(df):
    return df[numerical_features]
