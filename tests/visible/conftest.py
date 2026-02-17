"""
Pytest configuration for Lab 3 visible tests.
Provides fixed test data for deterministic visible testing.
"""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample test data for various tests."""
    return [
        {'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.45, 'depth': 150},
        {'sample_id': 'GEO-002', 'rock_type': 'Basalt', 'grade': 1.80, 'depth': 280},
        {'sample_id': 'GEO-003', 'rock_type': 'Granite', 'grade': 3.20, 'depth': 175},
        {'sample_id': 'GEO-004', 'rock_type': 'Sandstone', 'grade': 0.95, 'depth': 320},
        {'sample_id': 'GEO-005', 'rock_type': 'Basalt', 'grade': 2.10, 'depth': 410},
    ]


@pytest.fixture
def empty_sample_list():
    """Provide an empty sample list for edge case testing."""
    return []
