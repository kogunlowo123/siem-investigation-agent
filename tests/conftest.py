"""Test configuration for SIEM Investigation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "siem-investigation-agent", "category": "Security AI"}
