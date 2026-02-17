"""
Pytest configuration for Lab 3 hidden tests.
Loads variant configuration and provides variant-specific test data.
"""

import json
import sys
import pytest
from pathlib import Path

# Add src directory to path
SRC_DIR = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

VALID_ROCK_TYPES = [
    'Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss', 'Quartzite', 'Diorite'
]


@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Fall back to computing variant from get_variant.py
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "get_variant",
        str(Path(__file__).parent.parent.parent / "scripts" / "get_variant.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.get_my_variant()


@pytest.fixture(scope="session")
def variant_params(variant_config):
    """Extract parameters from variant config."""
    return variant_config["parameters"]


@pytest.fixture
def expected_sample_count(variant_params):
    """Return expected sample count from variant (8-15)."""
    return variant_params["sample_count"]


@pytest.fixture
def expected_rock_types(variant_params):
    """Return expected rock types list from variant (3-5 types)."""
    return variant_params["rock_types"]


@pytest.fixture
def expected_grade_range(variant_params):
    """Return expected grade range dict from variant."""
    return variant_params["grade_range"]


@pytest.fixture
def sample_data(variant_params):
    """Provide variant-aware sample test data."""
    rock_types = variant_params["rock_types"]
    gr = variant_params["grade_range"]
    grade_min = gr["min"]
    grade_max = gr["max"]
    grade_mid = (grade_min + grade_max) / 2

    samples = []
    depths = [150, 280, 175, 320, 410, 225, 195, 485]
    grades = [
        round(grade_mid + 0.5, 2),
        round(grade_mid - 0.3, 2),
        round(grade_max - 0.2, 2),
        round(grade_min + 0.1, 2),
        round(grade_mid + 0.1, 2),
        round(grade_mid - 0.8, 2),
        round(grade_mid + 1.0, 2),
        round(grade_min + 0.3, 2),
    ]

    for i in range(min(8, len(depths))):
        rt = rock_types[i % len(rock_types)]
        samples.append({
            'sample_id': f'GEO-{i+1:03d}',
            'rock_type': rt,
            'grade': grades[i],
            'depth': depths[i],
        })
    return samples


@pytest.fixture
def alternative_sample_data():
    """Alternative test data to catch hardcoded values."""
    return [
        {'sample_id': 'ALT-001', 'rock_type': 'Diorite', 'grade': 1.10, 'depth': 200},
        {'sample_id': 'ALT-002', 'rock_type': 'Quartzite', 'grade': 3.50, 'depth': 350},
        {'sample_id': 'ALT-003', 'rock_type': 'Gneiss', 'grade': 2.20, 'depth': 120},
        {'sample_id': 'ALT-004', 'rock_type': 'Diorite', 'grade': 4.00, 'depth': 500},
        {'sample_id': 'ALT-005', 'rock_type': 'Quartzite', 'grade': 0.50, 'depth': 275},
        {'sample_id': 'ALT-006', 'rock_type': 'Gneiss', 'grade': 2.80, 'depth': 390},
    ]


@pytest.fixture
def large_sample_data():
    """Larger dataset for stress testing."""
    import random
    rng = random.Random(42)
    rock_pool = ['Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss']
    samples = []
    for i in range(30):
        samples.append({
            'sample_id': f'STRESS-{i+1:03d}',
            'rock_type': rng.choice(rock_pool),
            'grade': round(rng.uniform(0.1, 5.0), 2),
            'depth': rng.randint(100, 500),
        })
    return samples


@pytest.fixture
def single_sample():
    """Provide a single sample for edge case testing."""
    return [{'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.5, 'depth': 200}]
