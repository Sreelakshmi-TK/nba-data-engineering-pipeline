"""
Module: file_utils

Purpose:
    Provide reusable utility functions for saving API responses as JSON
    files on the local file system.

Description:
    This module contains helper functions used by the ingestion layer to
    create output directories and save raw API responses. Centralizing
    file operations avoids duplication and makes future migration to
    Azure Data Lake Storage simpler.

Inputs:
    - Output directory path
    - Output file name
    - JSON-serializable Python object

Returns:
    None

Side Effects:
    - Creates directories if they do not exist.
    - Writes JSON files to disk.
"""

import json
from pathlib import Path


def save_json(data: dict, output_directory: str, file_name: str) -> None:
    """
    Save JSON data to a file.

    Purpose:
        Save a JSON-serializable Python object to the specified
        directory and file.

    Parameters:
        data (dict):
            The JSON data to save.

        output_directory (str):
            Directory where the file should be written.

        file_name (str):
            Name of the output JSON file.

    Returns:
        None

    Side Effects:
        Creates the output directory if it does not already exist.
        Writes a JSON file to disk.

    Raises:
        TypeError:
            If the provided data cannot be serialized to JSON.
        OSError:
            If the file cannot be written.
    """

    output_path = Path(output_directory)

    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / file_name

    with file_path.open("w", encoding="utf-8") as json_file:
        json.dump(
            data,
            json_file,
            indent=4,
            ensure_ascii=False
        )