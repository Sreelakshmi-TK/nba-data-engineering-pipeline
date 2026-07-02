"""
Module: api_constants

Purpose:
    Store constant values related to the BallDontLie API.

Description:
    This module centralizes API configuration values such as the
    base URL and endpoint names. Keeping these values in one place
    improves maintainability and avoids hardcoding them throughout
    the project.

Side Effects:
    None.
"""

# Base URL for the BallDontLie API
BASE_URL = "https://api.balldontlie.io/v1"

# API Endpoints
TEAMS_ENDPOINT = "/teams"
PLAYERS_ENDPOINT = "/players"
GAMES_ENDPOINT = "/games"
STATS_ENDPOINT = "/stats"

# Default request configuration
DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 100