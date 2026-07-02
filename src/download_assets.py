from pathlib import Path

from huggingface_hub import hf_hub_download


from huggingface_hub import hf_hub_download
from dashboard.config import HF_DATASET_REPO

from functools import lru_cache


def download_asset(filename: str) -> str:

    return hf_hub_download(
        repo_id=HF_DATASET_REPO,
        repo_type="dataset",
        filename=filename,
    )


def download_asset(filename: str):

    return hf_hub_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        filename=filename,
    )

@lru_cache(maxsize=None)
def download_asset(filename: str) -> str:

    return hf_hub_download(
        repo_id=HF_DATASET_REPO,
        repo_type="dataset",
        filename=filename,
    )