import sys
import os

# Add farm directory to system path
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'farm'))

# Import app_farm from main module in farm directory
from main import app

# Set up test client fixture
import pytest
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
