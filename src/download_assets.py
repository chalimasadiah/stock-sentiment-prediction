from functools import lru_cache
from pathlib import Path

from huggingface_hub import hf_hub_download

from dashboard.config import HF_DATASET_REPO


@lru_cache(maxsize=None)
def download_asset(filename: str) -> str:
    """
    Return local asset if available.
    Otherwise download it from Hugging Face Dataset.
    """

    project_root = Path(__file__).resolve().parent.parent

    local_file = project_root / "sample_data" / filename

    if local_file.exists():
        return str(local_file)

    local_model = project_root / "models" / filename

    if local_model.exists():
        return str(local_model)

    return hf_hub_download(
        repo_id=HF_DATASET_REPO,
        repo_type="dataset",
        filename=filename,
    )