import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_dataset(path):
    df = pd.read_csv('C:\\Users\\kikiv\\Downloads\\diabetes_streamlit_app\\diabetes_prediction_dataset.csv')
    return df


def preprocess_data(df):

    encoder = LabelEncoder()

    df["gender"] = encoder.fit_transform(df["gender"])
    df["smoking_history"] = encoder.fit_transform(df["smoking_history"])

    X = df.drop("diabetes", axis=1)
    y = df["diabetes"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, scaler