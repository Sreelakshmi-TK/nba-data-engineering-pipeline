"""
Module: ingest_teams

Purpose:
    Retrieve NBA teams data from the BallDontLie API and save the raw
    response as a JSON file.

Description:
    This module is responsible for ingesting the Teams dataset. It uses
    the reusable APIClient to retrieve data and the save_json utility
    to persist the raw response locally.

Inputs:
    None

Returns:
    None

Side Effects:
    - Sends an HTTP request to the BallDontLie API.
    - Creates the output directory if necessary.
    - Writes a JSON file to disk.
"""

from src.constants.api_constants import TEAMS_ENDPOINT
from src.utils.api_client import APIClient
from src.utils.file_utils import save_json


def ingest_teams() -> None:
    """
    Retrieve NBA teams data and save it locally.

    Purpose:
        Download the Teams dataset from the BallDontLie API and store
        the raw response as a formatted JSON file.

    Parameters:
        None

    Returns:
        None

    Side Effects:
        - Makes an HTTP request.
        - Writes a JSON file to the local filesystem.

    Raises:
        requests.HTTPError:
            If the API request fails.
        OSError:
            If the JSON file cannot be written.
    """

    client = APIClient()

    response = client.get(TEAMS_ENDPOINT)

    save_json(
        data=response,
        output_directory="data/raw/teams",
        file_name="teams.json"
    )


if __name__ == "__main__":
    ingest_teams()