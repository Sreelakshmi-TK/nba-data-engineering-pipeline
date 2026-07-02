"""
Module: api_client

Purpose:
    Provide a reusable client for interacting with the BallDontLie API.

Description:
    This module defines the APIClient class, which is responsible for
    communicating with the BallDontLie API. It centralizes API
    authentication, request handling, and error checking so that all
    ingestion modules can reuse the same implementation.

Inputs:
    - API endpoint
    - Optional query parameters
    - API key from environment variables

Returns:
    - Parsed JSON response as a Python dictionary

Side Effects:
    - Makes HTTP requests to the BallDontLie API.
"""

import os

import requests
from dotenv import load_dotenv

from src.constants.api_constants import BASE_URL

load_dotenv()


class APIClient:
    """
    Reusable client for the BallDontLie API.

    Purpose:
        Manage authenticated communication with the BallDontLie API.

    Parameters:
        None

    Returns:
        APIClient instance.

    Side Effects:
        Reads the API key from environment variables.
    """

    def __init__(self):
        """
        Initialize the API client.

        Purpose:
            Load the API key and prepare request headers.

        Parameters:
            None

        Returns:
            None

        Raises:
            ValueError:
                If the API key is not found.
        """

        self.api_key = os.getenv("BALLDONTLIE_API_KEY")

        if not self.api_key:
            raise ValueError(
                "BALLDONTLIE_API_KEY was not found in the environment."
            )

        self.headers = {
            "Authorization": self.api_key
        }

    def get(self, endpoint, params=None):
        """
        Send a GET request to the BallDontLie API.

        Purpose:
            Retrieve data from a specified API endpoint.

        Parameters:
            endpoint (str):
                Relative API endpoint.

            params (dict, optional):
                Query parameters.

        Returns:
            dict:
                Parsed JSON response.

        Raises:
            requests.HTTPError:
                If the API request fails.

        Side Effects:
            Sends an HTTP request.
        """

        url = BASE_URL + endpoint

        response = requests.get(
            url=url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()