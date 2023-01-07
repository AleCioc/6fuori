import os
from io import BytesIO
import streamlit as st
from google.cloud import storage


def read_from_google_bucket(blob_name, mode="string_to_bytes_io"):

    storage_client = storage.Client.from_service_account_json(
        os.path.join(os.path.dirname(__file__), "lucky-album-374011-ab30cb1a3556.json")
    )
    bucket = storage_client.bucket("6fuori_telegram_data")
    blob = bucket.blob(blob_name)
    if mode == "string_to_bytes_io":
        blob_as_string = blob.download_as_string()
        return BytesIO(blob_as_string)
    elif mode == "bytes":
        return blob.download_as_bytes()


def list_bucket_folder(bucket_folder_path):

    storage_client = storage.Client.from_service_account_json(
        os.path.join('.', "lucky-album-374011-ab30cb1a3556.json")
    )
    blobs_name_list = list()
    for blob in storage_client.list_blobs(
            "6fuori_telegram_data", prefix=bucket_folder_path
    ):
        blobs_name_list.append(
            ",".join(str(blob).split(',')[1:-1])[1:]
        )
    return blobs_name_list
