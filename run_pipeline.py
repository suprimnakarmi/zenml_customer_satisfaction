from pipelines.training_pipeline import train_pipeline
import pandas as pd
from zenml.client import Client

if __name__ == "__main__":

    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline("../olist_customers_dataset.csv")
    # df = pd.read_csv("../olist_customers_dataset.csv")
    # print(df)