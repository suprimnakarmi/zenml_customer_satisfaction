from pipelines.training_pipeline import train_pipeline
import pandas as pd

if __name__ == "__main__":
    train_pipeline("../olist_customers_dataset.csv")
    # df = pd.read_csv("../olist_customers_dataset.csv")
    # print(df)