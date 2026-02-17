"""
Lab 3 Hidden Tests - Data Structures: Lists & Dictionaries
These tests verify correctness with variant-specific values and catch hardcoded answers.
"""

import sys
from pathlib import Path

# Add src directory to path
SRC_DIR = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

VALID_ROCK_TYPES = [
    'Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss', 'Quartzite', 'Diorite'
]


# ---------------------------------------------------------------------------
# TestHiddenLists
# ---------------------------------------------------------------------------
class TestHiddenLists:
    """Hidden tests for Task 1: List Operations (lab3_lists.py)"""

    def test_create_depth_list_variant_count(self, expected_sample_count):
        """create_depth_list returns correct count from variant"""
        from lab3_lists import create_depth_list
        result = create_depth_list(expected_sample_count)
        assert result is not None, "create_depth_list should not return None"
        assert isinstance(result, list), "Should return a list"
        assert len(result) == expected_sample_count, \
            f"Should return {expected_sample_count} items, got {len(result)}"

    def test_create_depth_list_values_are_integers_in_range(self, expected_sample_count):
        """create_depth_list values should be integers between 100 and 500"""
        from lab3_lists import create_depth_list
        result = create_depth_list(expected_sample_count)
        assert result is not None, "create_depth_list should not return None"
        for val in result:
            assert isinstance(val, int), f"Each depth should be an integer, got {type(val)}"
            assert 100 <= val <= 500, f"Depth {val} out of range [100, 500]"

    def test_create_rock_type_list_uses_variant_types(self, expected_rock_types):
        """create_rock_type_list should return variant's rock types"""
        from lab3_lists import create_rock_type_list
        result = create_rock_type_list()
        assert result is not None, "create_rock_type_list should not return None"
        assert isinstance(result, list), "Should return a list"
        assert len(result) >= 3, "Should have at least 3 rock types"
        for rt in result:
            assert rt in VALID_ROCK_TYPES, \
                f"'{rt}' is not a valid rock type from the assignment pool"

    def test_demonstrate_indexing_correct_values(self):
        """demonstrate_indexing returns correct values for known data"""
        from lab3_lists import demonstrate_indexing
        test_list = [110, 220, 330, 440, 550, 660]
        result = demonstrate_indexing(test_list)
        assert result is not None, "Should not return None"
        assert result.get('first') == 110, f"First should be 110, got {result.get('first')}"
        assert result.get('last') == 660, f"Last should be 660, got {result.get('last')}"
        assert result.get('second') == 220, f"Second should be 220, got {result.get('second')}"
        assert result.get('second_to_last') == 550, \
            f"Second to last should be 550, got {result.get('second_to_last')}"

    def test_calculate_depth_statistics_alternative_data(self):
        """calculate_depth_statistics returns correct values on alternative data"""
        from lab3_lists import calculate_depth_statistics
        test_list = [250, 350, 150, 450]
        result = calculate_depth_statistics(test_list)
        assert result is not None, "Should not return None"
        assert result.get('count') == 4, f"Count should be 4, got {result.get('count')}"
        assert result.get('sum') == 1200, f"Sum should be 1200, got {result.get('sum')}"
        assert result.get('min') == 150, f"Min should be 150, got {result.get('min')}"
        assert result.get('max') == 450, f"Max should be 450, got {result.get('max')}"
        assert abs(result.get('average', 0) - 300.0) < 0.01, \
            f"Average should be 300.0, got {result.get('average')}"

    def test_demonstrate_slicing_correct_values(self):
        """demonstrate_slicing returns correct slices"""
        from lab3_lists import demonstrate_slicing
        test_list = [10, 20, 30, 40, 50, 60, 70]
        result = demonstrate_slicing(test_list)
        assert result is not None, "Should not return None"
        assert result.get('first_three') == [10, 20, 30], \
            f"first_three should be [10,20,30], got {result.get('first_three')}"
        assert result.get('last_three') == [50, 60, 70], \
            f"last_three should be [50,60,70], got {result.get('last_three')}"
        assert result.get('middle') == [30, 40, 50], \
            f"middle should be [30,40,50], got {result.get('middle')}"
        assert result.get('reversed') == [70, 60, 50, 40, 30, 20, 10], \
            f"reversed incorrect, got {result.get('reversed')}"


# ---------------------------------------------------------------------------
# TestHiddenDictionaries
# ---------------------------------------------------------------------------
class TestHiddenDictionaries:
    """Hidden tests for Task 2: Dictionary Operations (lab3_dictionaries.py)"""

    def test_create_sample_record_with_variant_rock_type(self, expected_rock_types):
        """create_sample_record should work with variant rock types"""
        from lab3_dictionaries import create_sample_record
        rt = expected_rock_types[0]
        result = create_sample_record('TEST-001', rt, 2.5, 200)
        assert result is not None, "Should not return None"
        assert result['rock_type'] == rt, f"rock_type should be '{rt}'"

    def test_create_nested_sample_database_structure(self):
        """create_nested_sample_database should have proper nested structure"""
        from lab3_dictionaries import create_nested_sample_database
        result = create_nested_sample_database()
        assert result is not None, "Should not return None"
        assert isinstance(result, dict), "Should return a dict"
        assert len(result) >= 3, "Should have at least 3 samples"
        for sid, record in result.items():
            assert isinstance(sid, str), "Keys should be strings"
            assert isinstance(record, dict), f"Value for '{sid}' should be a dict"
            assert 'rock_type' in record, f"'{sid}' missing 'rock_type'"
            assert 'grade' in record, f"'{sid}' missing 'grade'"
            assert 'depth' in record, f"'{sid}' missing 'depth'"

    def test_query_sample_database_finds_correct_record(self):
        """query_sample_database returns the correct record"""
        from lab3_dictionaries import query_sample_database
        db = {
            'X-001': {'rock_type': 'Diorite', 'grade': 1.5, 'depth': 300},
            'X-002': {'rock_type': 'Gneiss', 'grade': 3.0, 'depth': 150},
        }
        result = query_sample_database(db, 'X-002')
        assert result is not None, "Should find existing sample"
        assert result['rock_type'] == 'Gneiss', "Should return correct record"

    def test_add_sample_to_database_works(self):
        """add_sample_to_database adds entry correctly"""
        from lab3_dictionaries import add_sample_to_database
        db = {}
        result = add_sample_to_database(db, 'NEW-001', 'Quartzite', 2.2, 180)
        assert result is not None, "Should return updated database"
        assert 'NEW-001' in result, "Should contain new sample"
        entry = result['NEW-001']
        assert entry['rock_type'] == 'Quartzite'
        assert entry['grade'] == 2.2
        assert entry['depth'] == 180

    def test_get_all_rock_types_unique(self):
        """get_all_rock_types should return unique types"""
        from lab3_dictionaries import get_all_rock_types
        db = {
            'A-001': {'rock_type': 'Granite', 'grade': 1.0, 'depth': 100},
            'A-002': {'rock_type': 'Basalt', 'grade': 2.0, 'depth': 200},
            'A-003': {'rock_type': 'Granite', 'grade': 3.0, 'depth': 300},
        }
        result = get_all_rock_types(db)
        assert result is not None, "Should return a list"
        assert len(result) == 2, f"Should have 2 unique types, got {len(result)}"
        assert set(result) == {'Granite', 'Basalt'}

    def test_filter_by_minimum_grade_correctness(self):
        """filter_by_minimum_grade filters correctly on alternative data"""
        from lab3_dictionaries import filter_by_minimum_grade
        db = {
            'F-001': {'rock_type': 'Schist', 'grade': 4.5, 'depth': 100},
            'F-002': {'rock_type': 'Gneiss', 'grade': 1.2, 'depth': 200},
            'F-003': {'rock_type': 'Basalt', 'grade': 3.0, 'depth': 300},
            'F-004': {'rock_type': 'Schist', 'grade': 2.9, 'depth': 400},
        }
        result = filter_by_minimum_grade(db, 3.0)
        assert result is not None, "Should return a dict"
        assert 'F-001' in result, "Should include grade 4.5"
        assert 'F-003' in result, "Should include grade 3.0"
        assert 'F-002' not in result, "Should exclude grade 1.2"
        assert 'F-004' not in result, "Should exclude grade 2.9"

    def test_access_sample_values_correctness(self):
        """access_sample_values should return correct structure"""
        from lab3_dictionaries import access_sample_values
        sample = {'sample_id': 'T-001', 'rock_type': 'Diorite', 'grade': 3.3, 'depth': 250}
        result = access_sample_values(sample)
        assert result is not None, "Should not return None"
        assert result.get('direct_access') == 'Diorite'
        assert result.get('get_method') == 3.3
        assert result.get('get_with_default') == 'Unknown'
        assert isinstance(result.get('all_keys'), list)
        assert isinstance(result.get('all_values'), list)


# ---------------------------------------------------------------------------
# TestHiddenSampleManager
# ---------------------------------------------------------------------------
class TestHiddenSampleManager:
    """Hidden tests for Task 3: Sample Collection Manager (lab3_sample_manager.py)"""

    def test_full_crud_cycle(self):
        """Full CRUD cycle: create -> add -> find -> update -> remove"""
        from lab3_sample_manager import (
            create_sample_collection, add_sample, find_sample_by_id,
            update_grade, remove_sample, get_sample_count
        )
        coll = create_sample_collection()
        assert coll is not None

        add_sample(coll, 'CRUD-001', 'Basalt', 1.5, 200)
        add_sample(coll, 'CRUD-002', 'Granite', 2.5, 300)
        assert get_sample_count(coll) == 2

        found = find_sample_by_id(coll, 'CRUD-001')
        assert found is not None
        assert found['grade'] == 1.5

        update_grade(coll, 'CRUD-001', 3.0)
        found = find_sample_by_id(coll, 'CRUD-001')
        assert found['grade'] == 3.0

        removed = remove_sample(coll, 'CRUD-001')
        assert removed is True
        assert get_sample_count(coll) == 1
        assert find_sample_by_id(coll, 'CRUD-001') is None

    def test_find_by_rock_type_with_variant_types(self, expected_rock_types):
        """find_by_rock_type works with variant rock types"""
        from lab3_sample_manager import create_sample_collection, add_sample, find_by_rock_type
        coll = create_sample_collection()
        target_type = expected_rock_types[0]
        add_sample(coll, 'RT-001', target_type, 2.0, 150)
        add_sample(coll, 'RT-002', 'SomeOther' if len(expected_rock_types) < 2 else expected_rock_types[1], 1.5, 250)
        add_sample(coll, 'RT-003', target_type, 3.0, 350)

        result = find_by_rock_type(coll, target_type)
        assert result is not None
        assert len(result) == 2, f"Should find 2 samples of type '{target_type}'"

    def test_find_by_depth_range_correctness(self):
        """find_by_depth_range returns correct samples"""
        from lab3_sample_manager import create_sample_collection, add_sample, find_by_depth_range
        coll = create_sample_collection()
        add_sample(coll, 'DR-001', 'Granite', 1.0, 100)
        add_sample(coll, 'DR-002', 'Basalt', 2.0, 200)
        add_sample(coll, 'DR-003', 'Schist', 3.0, 300)
        add_sample(coll, 'DR-004', 'Gneiss', 4.0, 400)
        add_sample(coll, 'DR-005', 'Granite', 5.0, 500)

        result = find_by_depth_range(coll, 200, 400)
        assert result is not None
        assert len(result) == 3, f"Should find 3 samples in [200, 400], got {len(result)}"
        ids = [s['sample_id'] for s in result]
        assert 'DR-002' in ids
        assert 'DR-003' in ids
        assert 'DR-004' in ids

    def test_bulk_add_samples_returns_count(self):
        """bulk_add_samples adds all and returns correct count"""
        from lab3_sample_manager import create_sample_collection, bulk_add_samples, get_sample_count
        coll = create_sample_collection()
        data = [
            ('B-001', 'Granite', 1.0, 100),
            ('B-002', 'Basalt', 2.0, 200),
            ('B-003', 'Schist', 3.0, 300),
            ('B-004', 'Gneiss', 4.0, 400),
            ('B-005', 'Quartzite', 5.0, 500),
        ]
        count = bulk_add_samples(coll, data)
        assert count == 5, f"Should return 5, got {count}"
        assert get_sample_count(coll) == 5

    def test_get_unique_rock_types_correctness(self):
        """get_unique_rock_types returns only unique types"""
        from lab3_sample_manager import create_sample_collection, add_sample, get_unique_rock_types
        coll = create_sample_collection()
        add_sample(coll, 'U-001', 'Granite', 1.0, 100)
        add_sample(coll, 'U-002', 'Basalt', 2.0, 200)
        add_sample(coll, 'U-003', 'Granite', 3.0, 300)
        add_sample(coll, 'U-004', 'Schist', 4.0, 400)
        add_sample(coll, 'U-005', 'Basalt', 5.0, 500)

        result = get_unique_rock_types(coll)
        assert result is not None
        assert len(result) == 3, f"Should have 3 unique types, got {len(result)}"
        assert set(result) == {'Granite', 'Basalt', 'Schist'}

    def test_get_sample_count_after_operations(self):
        """get_sample_count reflects adds and removes"""
        from lab3_sample_manager import (
            create_sample_collection, add_sample, remove_sample, get_sample_count
        )
        coll = create_sample_collection()
        assert get_sample_count(coll) == 0
        add_sample(coll, 'C-001', 'Granite', 1.0, 100)
        add_sample(coll, 'C-002', 'Basalt', 2.0, 200)
        assert get_sample_count(coll) == 2
        remove_sample(coll, 'C-001')
        assert get_sample_count(coll) == 1

    def test_update_sample_multiple_fields(self):
        """update_sample updates multiple fields at once"""
        from lab3_sample_manager import (
            create_sample_collection, add_sample, update_sample, find_sample_by_id
        )
        coll = create_sample_collection()
        add_sample(coll, 'UP-001', 'Granite', 1.0, 100)
        result = update_sample(coll, 'UP-001', grade=5.0, depth=999)
        assert result is True, "Should return True for successful update"
        found = find_sample_by_id(coll, 'UP-001')
        assert found['grade'] == 5.0
        assert found['depth'] == 999


# ---------------------------------------------------------------------------
# TestHiddenStatistics
# ---------------------------------------------------------------------------
class TestHiddenStatistics:
    """Hidden tests for Task 4: Computing Statistics (lab3_statistics.py)"""

    def test_calculate_average_grade_alternative_data(self, alternative_sample_data):
        """calculate_average_grade on alternative data (catches hardcoded)"""
        from lab3_statistics import calculate_average_grade
        result = calculate_average_grade(alternative_sample_data)
        expected = sum(s['grade'] for s in alternative_sample_data) / len(alternative_sample_data)
        assert result is not None, "Should not return None"
        assert abs(result - expected) < 0.01, f"Expected {expected:.4f}, got {result}"

    def test_calculate_total_depth_alternative_data(self, alternative_sample_data):
        """calculate_total_depth on alternative data"""
        from lab3_statistics import calculate_total_depth
        result = calculate_total_depth(alternative_sample_data)
        expected = sum(s['depth'] for s in alternative_sample_data)
        assert result is not None, "Should not return None"
        assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"

    def test_find_depth_range_alternative_data(self, alternative_sample_data):
        """find_depth_range on alternative data"""
        from lab3_statistics import find_depth_range
        result = find_depth_range(alternative_sample_data)
        assert result is not None
        depths = [s['depth'] for s in alternative_sample_data]
        assert result[0] == min(depths), f"Min depth should be {min(depths)}, got {result[0]}"
        assert result[1] == max(depths), f"Max depth should be {max(depths)}, got {result[1]}"

    def test_find_grade_range_alternative_data(self, alternative_sample_data):
        """find_grade_range on alternative data"""
        from lab3_statistics import find_grade_range
        result = find_grade_range(alternative_sample_data)
        assert result is not None
        grades = [s['grade'] for s in alternative_sample_data]
        assert result[0] == min(grades), f"Min grade should be {min(grades)}, got {result[0]}"
        assert result[1] == max(grades), f"Max grade should be {max(grades)}, got {result[1]}"

    def test_count_by_rock_type_alternative_data(self, alternative_sample_data):
        """count_by_rock_type on alternative data"""
        from lab3_statistics import count_by_rock_type
        result = count_by_rock_type(alternative_sample_data)
        assert result is not None
        assert result.get('Diorite') == 2, f"Should have 2 Diorite, got {result.get('Diorite')}"
        assert result.get('Quartzite') == 2, f"Should have 2 Quartzite, got {result.get('Quartzite')}"
        assert result.get('Gneiss') == 2, f"Should have 2 Gneiss, got {result.get('Gneiss')}"

    def test_get_high_grade_samples_alternative_data(self, alternative_sample_data):
        """get_high_grade_samples on alternative data"""
        from lab3_statistics import get_high_grade_samples
        result = get_high_grade_samples(alternative_sample_data, 2.5)
        assert result is not None
        # Grades > 2.5: 3.50, 4.00, 2.80
        assert len(result) == 3, f"Should have 3 samples above 2.5, got {len(result)}"

    def test_calculate_grade_statistics_complete(self, alternative_sample_data):
        """calculate_grade_statistics returns all fields correctly"""
        from lab3_statistics import calculate_grade_statistics
        result = calculate_grade_statistics(alternative_sample_data)
        assert result is not None
        grades = [s['grade'] for s in alternative_sample_data]
        assert result.get('count') == len(grades)
        assert abs(result.get('sum', 0) - sum(grades)) < 0.01
        assert result.get('min') == min(grades)
        assert result.get('max') == max(grades)
        expected_avg = sum(grades) / len(grades)
        assert abs(result.get('average', 0) - expected_avg) < 0.01
        expected_range = max(grades) - min(grades)
        assert abs(result.get('range', 0) - expected_range) < 0.01


# ---------------------------------------------------------------------------
# TestHiddenFilters
# ---------------------------------------------------------------------------
class TestHiddenFilters:
    """Hidden tests for Task 5: Filtering and Sorting (lab3_filters.py)"""

    def test_filter_by_depth_range_alternative(self, alternative_sample_data):
        """filter_by_depth_range on alternative data"""
        from lab3_filters import filter_by_depth_range
        result = filter_by_depth_range(alternative_sample_data, 200, 400)
        assert result is not None
        # Depths in [200,400]: 200, 350, 275, 390
        expected_ids = {'ALT-001', 'ALT-002', 'ALT-005', 'ALT-006'}
        result_ids = {s['sample_id'] for s in result}
        assert result_ids == expected_ids, \
            f"Expected {expected_ids}, got {result_ids}"

    def test_filter_by_grade_range_alternative(self, alternative_sample_data):
        """filter_by_grade_range on alternative data"""
        from lab3_filters import filter_by_grade_range
        result = filter_by_grade_range(alternative_sample_data, 1.0, 3.0)
        assert result is not None
        # Grades in [1.0, 3.0]: 1.10, 2.20, 2.80
        assert len(result) == 3, f"Should have 3 samples, got {len(result)}"

    def test_filter_by_rock_types_alternative(self, alternative_sample_data):
        """filter_by_rock_types on alternative data"""
        from lab3_filters import filter_by_rock_types
        result = filter_by_rock_types(alternative_sample_data, ['Diorite', 'Gneiss'])
        assert result is not None
        assert len(result) == 4, f"Should have 4 samples (2 Diorite + 2 Gneiss), got {len(result)}"

    def test_sort_by_grade_ascending_alternative(self, alternative_sample_data):
        """sort_by_grade ascending on alternative data"""
        from lab3_filters import sort_by_grade
        result = sort_by_grade(alternative_sample_data, descending=False)
        assert result is not None
        grades = [s['grade'] for s in result]
        assert grades == sorted(grades), "Should be sorted ascending"
        assert grades[0] == 0.50, f"First should be 0.50, got {grades[0]}"

    def test_sort_by_grade_descending_alternative(self, alternative_sample_data):
        """sort_by_grade descending on alternative data"""
        from lab3_filters import sort_by_grade
        result = sort_by_grade(alternative_sample_data, descending=True)
        assert result is not None
        grades = [s['grade'] for s in result]
        assert grades == sorted(grades, reverse=True), "Should be sorted descending"
        assert grades[0] == 4.00, f"First should be 4.00, got {grades[0]}"

    def test_get_top_n_by_grade_alternative(self, alternative_sample_data):
        """get_top_n_by_grade on alternative data"""
        from lab3_filters import get_top_n_by_grade
        result = get_top_n_by_grade(alternative_sample_data, 3)
        assert result is not None
        assert len(result) == 3
        grades = [s['grade'] for s in result]
        # Top 3: 4.00, 3.50, 2.80
        assert grades == sorted(grades, reverse=True), "Should be sorted descending"
        assert grades[0] == 4.00

    def test_group_by_rock_type_alternative(self, alternative_sample_data):
        """group_by_rock_type on alternative data"""
        from lab3_filters import group_by_rock_type
        result = group_by_rock_type(alternative_sample_data)
        assert result is not None
        assert len(result) == 3, f"Should have 3 groups, got {len(result)}"
        assert len(result.get('Diorite', [])) == 2
        assert len(result.get('Quartzite', [])) == 2
        assert len(result.get('Gneiss', [])) == 2

    def test_filter_and_sort_combined_alternative(self, alternative_sample_data):
        """filter_and_sort combined on alternative data"""
        from lab3_filters import filter_and_sort
        result = filter_and_sort(
            alternative_sample_data,
            rock_types=['Diorite'],
            min_grade=1.0,
            sort_by='grade',
            descending=True
        )
        assert result is not None
        assert len(result) == 2, f"Should have 2 Diorite with grade>=1.0, got {len(result)}"
        grades = [s['grade'] for s in result]
        assert grades == sorted(grades, reverse=True), "Should be sorted descending"


# ---------------------------------------------------------------------------
# TestHiddenVariantVerification
# ---------------------------------------------------------------------------
class TestHiddenVariantVerification:
    """Verify variant configuration is valid."""

    def test_variant_has_required_keys(self, variant_config):
        """Variant config should have required keys"""
        assert 'parameters' in variant_config, "Config missing 'parameters' key"
        params = variant_config['parameters']
        assert 'sample_count' in params, "Parameters missing 'sample_count'"
        assert 'rock_types' in params, "Parameters missing 'rock_types'"
        assert 'grade_range' in params, "Parameters missing 'grade_range'"

    def test_sample_count_in_range(self, expected_sample_count):
        """sample_count should be between 8 and 15"""
        assert 8 <= expected_sample_count <= 15, \
            f"sample_count {expected_sample_count} not in range [8, 15]"

    def test_rock_types_are_valid(self, expected_rock_types):
        """All rock types should be from the valid pool"""
        assert 3 <= len(expected_rock_types) <= 5, \
            f"Should have 3-5 rock types, got {len(expected_rock_types)}"
        for rt in expected_rock_types:
            assert rt in VALID_ROCK_TYPES, \
                f"'{rt}' is not a valid rock type"

    def test_grade_range_valid(self, expected_grade_range):
        """grade_range min should be less than max"""
        assert expected_grade_range['min'] < expected_grade_range['max'], \
            f"min ({expected_grade_range['min']}) should be < max ({expected_grade_range['max']})"
        assert 0.2 <= expected_grade_range['min'] <= 0.8, \
            f"min ({expected_grade_range['min']}) should be in [0.2, 0.8]"
        diff = expected_grade_range['max'] - expected_grade_range['min']
        assert 3.0 <= diff <= 5.0, \
            f"max - min = {diff}, should be in [3.0, 5.0]"


# ---------------------------------------------------------------------------
# TestHiddenIntegration
# ---------------------------------------------------------------------------
class TestHiddenIntegration:
    """Integration tests combining multiple modules."""

    def test_create_filter_statistics_pipeline(self, alternative_sample_data):
        """Pipeline: create collection -> add samples -> filter -> statistics"""
        from lab3_sample_manager import create_sample_collection, add_sample
        from lab3_filters import filter_by_rock_types
        from lab3_statistics import calculate_average_grade

        coll = create_sample_collection()
        for s in alternative_sample_data:
            add_sample(coll, s['sample_id'], s['rock_type'], s['grade'], s['depth'])

        filtered = filter_by_rock_types(coll, ['Diorite'])
        assert filtered is not None
        assert len(filtered) == 2

        avg = calculate_average_grade(filtered)
        assert avg is not None
        expected = (1.10 + 4.00) / 2
        assert abs(avg - expected) < 0.01, f"Expected {expected}, got {avg}"

    def test_create_sort_top_n_pipeline(self, alternative_sample_data):
        """Pipeline: create samples -> sort -> top N -> verify ordering"""
        from lab3_filters import sort_by_grade, get_top_n_by_grade

        sorted_result = sort_by_grade(alternative_sample_data, descending=True)
        assert sorted_result is not None

        top_3 = get_top_n_by_grade(alternative_sample_data, 3)
        assert top_3 is not None
        assert len(top_3) == 3

        grades = [s['grade'] for s in top_3]
        assert grades == sorted(grades, reverse=True), "Top N should be ordered descending"
        assert grades[0] == 4.00
        assert grades[1] == 3.50
        assert grades[2] == 2.80

    def test_full_crud_plus_statistics(self):
        """Full CRUD + statistics chain"""
        from lab3_sample_manager import (
            create_sample_collection, add_sample, update_grade,
            remove_sample, get_sample_count
        )
        from lab3_statistics import calculate_average_grade, count_by_rock_type

        coll = create_sample_collection()
        add_sample(coll, 'INT-001', 'Granite', 1.0, 100)
        add_sample(coll, 'INT-002', 'Basalt', 2.0, 200)
        add_sample(coll, 'INT-003', 'Granite', 3.0, 300)
        add_sample(coll, 'INT-004', 'Schist', 4.0, 400)

        avg = calculate_average_grade(coll)
        assert avg is not None
        assert abs(avg - 2.5) < 0.01

        update_grade(coll, 'INT-001', 5.0)
        avg = calculate_average_grade(coll)
        assert abs(avg - 3.5) < 0.01

        remove_sample(coll, 'INT-004')
        assert get_sample_count(coll) == 3

        counts = count_by_rock_type(coll)
        assert counts is not None
        assert counts.get('Granite') == 2
        assert counts.get('Basalt') == 1
        assert counts.get('Schist', 0) == 0
