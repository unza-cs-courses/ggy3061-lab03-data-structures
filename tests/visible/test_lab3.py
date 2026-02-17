"""
Lab 3 Visible Tests - Data Structures: Lists & Dictionaries
These tests verify basic functionality of list and dictionary operations.
"""

import sys
from pathlib import Path

# Add src directory to path
SRC_DIR = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))


class TestTask1Lists:
    """Tests for Task 1: List Operations (lab3_lists.py)"""

    def test_lists_file_exists(self):
        """lab3_lists.py file should exist"""
        assert (SRC_DIR / "lab3_lists.py").exists(), "lab3_lists.py not found in src/"

    def test_create_depth_list_function_exists(self):
        """create_depth_list function should be defined"""
        from lab3_lists import create_depth_list
        assert callable(create_depth_list), "create_depth_list should be a function"

    def test_create_depth_list_returns_list(self):
        """create_depth_list should return a list"""
        from lab3_lists import create_depth_list
        result = create_depth_list(5)
        assert result is not None, "Function should not return None"
        assert isinstance(result, list), "Should return a list"

    def test_create_depth_list_correct_count(self):
        """create_depth_list should return correct number of items"""
        from lab3_lists import create_depth_list
        result = create_depth_list(8)
        if result is not None:
            assert len(result) == 8, f"Should return 8 items, got {len(result)}"

    def test_create_rock_type_list_function_exists(self):
        """create_rock_type_list function should be defined"""
        from lab3_lists import create_rock_type_list
        assert callable(create_rock_type_list), "create_rock_type_list should be a function"

    def test_create_rock_type_list_returns_list(self):
        """create_rock_type_list should return a list"""
        from lab3_lists import create_rock_type_list
        result = create_rock_type_list()
        assert result is not None, "Function should not return None"
        assert isinstance(result, list), "Should return a list"

    def test_demonstrate_indexing_function_exists(self):
        """demonstrate_indexing function should be defined"""
        from lab3_lists import demonstrate_indexing
        assert callable(demonstrate_indexing), "demonstrate_indexing should be a function"

    def test_demonstrate_indexing_returns_dict(self):
        """demonstrate_indexing should return a dictionary"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_demonstrate_indexing_has_required_keys(self):
        """demonstrate_indexing should have required keys"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        if result:
            required_keys = ['first', 'last', 'second', 'second_to_last']
            for key in required_keys:
                assert key in result, f"Result should have '{key}' key"

    def test_demonstrate_indexing_first_element(self):
        """demonstrate_indexing should correctly get first element"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        if result:
            assert result.get('first') == 100, "First element should be 100"

    def test_demonstrate_indexing_last_element(self):
        """demonstrate_indexing should correctly get last element"""
        from lab3_lists import demonstrate_indexing
        test_list = [100, 200, 300, 400, 500]
        result = demonstrate_indexing(test_list)
        if result:
            assert result.get('last') == 500, "Last element should be 500"

    def test_demonstrate_slicing_function_exists(self):
        """demonstrate_slicing function should be defined"""
        from lab3_lists import demonstrate_slicing
        assert callable(demonstrate_slicing), "demonstrate_slicing should be a function"

    def test_demonstrate_slicing_returns_dict(self):
        """demonstrate_slicing should return a dictionary"""
        from lab3_lists import demonstrate_slicing
        test_list = [100, 200, 300, 400, 500, 600]
        result = demonstrate_slicing(test_list)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_calculate_depth_statistics_function_exists(self):
        """calculate_depth_statistics function should be defined"""
        from lab3_lists import calculate_depth_statistics
        assert callable(calculate_depth_statistics)

    def test_calculate_depth_statistics_returns_dict(self):
        """calculate_depth_statistics should return a dictionary"""
        from lab3_lists import calculate_depth_statistics
        test_list = [100, 200, 300, 400, 500]
        result = calculate_depth_statistics(test_list)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_calculate_depth_statistics_correct_values(self):
        """calculate_depth_statistics should compute correct values"""
        from lab3_lists import calculate_depth_statistics
        test_list = [100, 200, 300]
        result = calculate_depth_statistics(test_list)
        if result:
            assert result.get('count') == 3, "Count should be 3"
            assert result.get('sum') == 600, "Sum should be 600"
            assert result.get('min') == 100, "Min should be 100"
            assert result.get('max') == 300, "Max should be 300"
            assert abs(result.get('average', 0) - 200.0) < 0.01, "Average should be 200"

    def test_demonstrate_list_methods_function_exists(self):
        """demonstrate_list_methods function should be defined"""
        from lab3_lists import demonstrate_list_methods
        assert callable(demonstrate_list_methods)

    def test_demonstrate_list_methods_returns_dict(self):
        """demonstrate_list_methods should return a dictionary"""
        from lab3_lists import demonstrate_list_methods
        result = demonstrate_list_methods([100, 200, 300], ['Granite', 'Basalt'])
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"


class TestTask2Dictionaries:
    """Tests for Task 2: Dictionary Operations (lab3_dictionaries.py)"""

    def test_dictionaries_file_exists(self):
        """lab3_dictionaries.py file should exist"""
        assert (SRC_DIR / "lab3_dictionaries.py").exists(), "lab3_dictionaries.py not found"

    def test_create_sample_record_function_exists(self):
        """create_sample_record function should be defined"""
        from lab3_dictionaries import create_sample_record
        assert callable(create_sample_record)

    def test_create_sample_record_returns_dict(self):
        """create_sample_record should return a dictionary"""
        from lab3_dictionaries import create_sample_record
        result = create_sample_record('GEO-001', 'Granite', 2.5, 150)
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_create_sample_record_has_required_keys(self):
        """create_sample_record should have required keys"""
        from lab3_dictionaries import create_sample_record
        result = create_sample_record('GEO-001', 'Granite', 2.5, 150)
        if result:
            for key in ['sample_id', 'rock_type', 'grade', 'depth']:
                assert key in result, f"Missing key: {key}"

    def test_create_sample_record_correct_values(self):
        """create_sample_record should store correct values"""
        from lab3_dictionaries import create_sample_record
        result = create_sample_record('GEO-001', 'Granite', 2.5, 150)
        if result:
            assert result['sample_id'] == 'GEO-001'
            assert result['rock_type'] == 'Granite'
            assert result['grade'] == 2.5
            assert result['depth'] == 150

    def test_access_sample_values_function_exists(self):
        """access_sample_values function should be defined"""
        from lab3_dictionaries import access_sample_values
        assert callable(access_sample_values)

    def test_demonstrate_dictionary_methods_function_exists(self):
        """demonstrate_dictionary_methods function should be defined"""
        from lab3_dictionaries import demonstrate_dictionary_methods
        assert callable(demonstrate_dictionary_methods)

    def test_update_sample_function_exists(self):
        """update_sample function should be defined"""
        from lab3_dictionaries import update_sample
        assert callable(update_sample)

    def test_update_sample_creates_copy(self):
        """update_sample should not modify original"""
        from lab3_dictionaries import update_sample
        original = {'sample_id': 'GEO-001', 'grade': 2.0}
        result = update_sample(original, {'grade': 3.0})
        if result:
            assert original['grade'] == 2.0, "Original should not be modified"

    def test_create_nested_sample_database_function_exists(self):
        """create_nested_sample_database function should be defined"""
        from lab3_dictionaries import create_nested_sample_database
        assert callable(create_nested_sample_database)

    def test_create_nested_sample_database_returns_dict(self):
        """create_nested_sample_database should return a dictionary"""
        from lab3_dictionaries import create_nested_sample_database
        result = create_nested_sample_database()
        assert result is not None, "Function should not return None"
        assert isinstance(result, dict), "Should return a dictionary"

    def test_query_sample_database_function_exists(self):
        """query_sample_database function should be defined"""
        from lab3_dictionaries import query_sample_database
        assert callable(query_sample_database)

    def test_query_sample_database_finds_existing(self):
        """query_sample_database should find existing sample"""
        from lab3_dictionaries import query_sample_database
        db = {'GEO-001': {'rock_type': 'Granite', 'grade': 2.5, 'depth': 150}}
        result = query_sample_database(db, 'GEO-001')
        assert result is not None, "Should find existing sample"

    def test_query_sample_database_returns_none_for_missing(self):
        """query_sample_database should return None for missing ID"""
        from lab3_dictionaries import query_sample_database
        db = {'GEO-001': {'rock_type': 'Granite', 'grade': 2.5, 'depth': 150}}
        result = query_sample_database(db, 'GEO-999')
        assert result is None, "Should return None for missing sample"

    def test_add_sample_to_database_function_exists(self):
        """add_sample_to_database function should be defined"""
        from lab3_dictionaries import add_sample_to_database
        assert callable(add_sample_to_database)

    def test_add_sample_to_database_adds_entry(self):
        """add_sample_to_database should add a new entry"""
        from lab3_dictionaries import add_sample_to_database
        db = {}
        result = add_sample_to_database(db, 'GEO-001', 'Granite', 2.5, 150)
        if result is not None:
            assert 'GEO-001' in result, "Should contain the new sample ID"

    def test_get_all_rock_types_function_exists(self):
        """get_all_rock_types function should be defined"""
        from lab3_dictionaries import get_all_rock_types
        assert callable(get_all_rock_types)

    def test_get_all_rock_types_returns_list(self):
        """get_all_rock_types should return a list"""
        from lab3_dictionaries import get_all_rock_types
        db = {
            'GEO-001': {'rock_type': 'Granite', 'grade': 2.5, 'depth': 150},
            'GEO-002': {'rock_type': 'Basalt', 'grade': 1.8, 'depth': 280},
        }
        result = get_all_rock_types(db)
        assert result is not None, "Should return a value"
        assert isinstance(result, list), "Should return a list"

    def test_filter_by_minimum_grade_function_exists(self):
        """filter_by_minimum_grade function should be defined"""
        from lab3_dictionaries import filter_by_minimum_grade
        assert callable(filter_by_minimum_grade)

    def test_filter_by_minimum_grade_correct_filtering(self):
        """filter_by_minimum_grade should filter correctly"""
        from lab3_dictionaries import filter_by_minimum_grade
        db = {
            'GEO-001': {'rock_type': 'Granite', 'grade': 3.5, 'depth': 150},
            'GEO-002': {'rock_type': 'Basalt', 'grade': 1.0, 'depth': 280},
            'GEO-003': {'rock_type': 'Schist', 'grade': 2.5, 'depth': 200},
        }
        result = filter_by_minimum_grade(db, 2.0)
        if result is not None:
            assert 'GEO-001' in result, "Should include grade 3.5"
            assert 'GEO-003' in result, "Should include grade 2.5"
            assert 'GEO-002' not in result, "Should exclude grade 1.0"


class TestTask3SampleManager:
    """Tests for Task 3: Sample Collection Manager (lab3_sample_manager.py)"""

    def test_sample_manager_file_exists(self):
        """lab3_sample_manager.py file should exist"""
        assert (SRC_DIR / "lab3_sample_manager.py").exists()

    def test_create_sample_collection_function_exists(self):
        """create_sample_collection function should be defined"""
        from lab3_sample_manager import create_sample_collection
        assert callable(create_sample_collection)

    def test_create_sample_collection_returns_list(self):
        """create_sample_collection should return an empty list"""
        from lab3_sample_manager import create_sample_collection
        result = create_sample_collection()
        assert result is not None, "Function should not return None"
        assert isinstance(result, list), "Should return a list"
        assert len(result) == 0, "Should return empty list"

    def test_add_sample_function_exists(self):
        """add_sample function should be defined"""
        from lab3_sample_manager import add_sample
        assert callable(add_sample)

    def test_add_sample_adds_to_collection(self):
        """add_sample should add a sample to the collection"""
        from lab3_sample_manager import create_sample_collection, add_sample
        collection = create_sample_collection()
        if collection is not None:
            result = add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            if result is not None:
                assert len(result) == 1, "Collection should have 1 sample"

    def test_find_sample_by_id_function_exists(self):
        """find_sample_by_id function should be defined"""
        from lab3_sample_manager import find_sample_by_id
        assert callable(find_sample_by_id)

    def test_find_sample_by_id_returns_correct_sample(self):
        """find_sample_by_id should return the correct sample"""
        from lab3_sample_manager import create_sample_collection, add_sample, find_sample_by_id
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            result = find_sample_by_id(collection, 'GEO-001')
            if result is not None:
                assert result['sample_id'] == 'GEO-001'

    def test_find_sample_by_id_returns_none_when_not_found(self):
        """find_sample_by_id should return None for non-existent ID"""
        from lab3_sample_manager import create_sample_collection, find_sample_by_id
        collection = create_sample_collection()
        if collection is not None:
            result = find_sample_by_id(collection, 'NON-EXISTENT')
            assert result is None, "Should return None for non-existent ID"

    def test_find_by_rock_type_function_exists(self):
        """find_by_rock_type function should be defined"""
        from lab3_sample_manager import find_by_rock_type
        assert callable(find_by_rock_type)

    def test_update_grade_function_exists(self):
        """update_grade function should be defined"""
        from lab3_sample_manager import update_grade
        assert callable(update_grade)

    def test_remove_sample_function_exists(self):
        """remove_sample function should be defined"""
        from lab3_sample_manager import remove_sample
        assert callable(remove_sample)

    def test_get_sample_count_correct(self):
        """get_sample_count should return correct count"""
        from lab3_sample_manager import create_sample_collection, add_sample, get_sample_count
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            add_sample(collection, 'GEO-002', 'Basalt', 1.8, 280)
            count = get_sample_count(collection)
            if count is not None:
                assert count == 2, f"Should have 2 samples, got {count}"

    def test_find_by_rock_type_correct_filtering(self):
        """find_by_rock_type should return matching samples"""
        from lab3_sample_manager import create_sample_collection, add_sample, find_by_rock_type
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            add_sample(collection, 'GEO-002', 'Basalt', 1.8, 280)
            add_sample(collection, 'GEO-003', 'Granite', 3.2, 175)
            result = find_by_rock_type(collection, 'Granite')
            if result is not None:
                assert len(result) == 2, f"Should find 2 Granite samples, got {len(result)}"

    def test_update_grade_updates_value(self):
        """update_grade should change the grade"""
        from lab3_sample_manager import create_sample_collection, add_sample, update_grade, find_sample_by_id
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            result = update_grade(collection, 'GEO-001', 3.0)
            if result is not None:
                assert result == True, "Should return True for successful update"
            sample = find_sample_by_id(collection, 'GEO-001')
            if sample:
                assert sample['grade'] == 3.0, "Grade should be updated to 3.0"

    def test_remove_sample_removes_from_collection(self):
        """remove_sample should remove the sample"""
        from lab3_sample_manager import create_sample_collection, add_sample, remove_sample, get_sample_count
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            add_sample(collection, 'GEO-002', 'Basalt', 1.8, 280)
            result = remove_sample(collection, 'GEO-001')
            if result is not None:
                assert result == True, "Should return True for successful removal"
            count = get_sample_count(collection)
            if count is not None:
                assert count == 1, "Should have 1 sample after removal"

    def test_get_unique_rock_types_function_exists(self):
        """get_unique_rock_types function should be defined"""
        from lab3_sample_manager import get_unique_rock_types
        assert callable(get_unique_rock_types)

    def test_find_by_depth_range_function_exists(self):
        """find_by_depth_range function should be defined"""
        from lab3_sample_manager import find_by_depth_range
        assert callable(find_by_depth_range)

    def test_find_by_depth_range_correct_filtering(self):
        """find_by_depth_range should return samples in range"""
        from lab3_sample_manager import create_sample_collection, add_sample, find_by_depth_range
        collection = create_sample_collection()
        if collection is not None:
            add_sample(collection, 'GEO-001', 'Granite', 2.5, 150)
            add_sample(collection, 'GEO-002', 'Basalt', 1.8, 280)
            add_sample(collection, 'GEO-003', 'Schist', 3.2, 450)
            result = find_by_depth_range(collection, 200, 400)
            if result is not None:
                assert len(result) == 1, f"Should find 1 sample in 200-400m, got {len(result)}"

    def test_bulk_add_samples_function_exists(self):
        """bulk_add_samples function should be defined"""
        from lab3_sample_manager import bulk_add_samples
        assert callable(bulk_add_samples)

    def test_bulk_add_samples_adds_all(self):
        """bulk_add_samples should add all samples"""
        from lab3_sample_manager import create_sample_collection, bulk_add_samples, get_sample_count
        collection = create_sample_collection()
        if collection is not None:
            data = [
                ('GEO-001', 'Granite', 2.5, 150),
                ('GEO-002', 'Basalt', 1.8, 280),
                ('GEO-003', 'Schist', 3.2, 175),
            ]
            result = bulk_add_samples(collection, data)
            if result is not None:
                assert result == 3, f"Should return 3 samples added, got {result}"


class TestTask4Statistics:
    """Tests for Task 4: Computing Statistics (lab3_statistics.py)"""

    def test_statistics_file_exists(self):
        """lab3_statistics.py file should exist"""
        assert (SRC_DIR / "lab3_statistics.py").exists()

    def test_calculate_average_grade_function_exists(self):
        """calculate_average_grade function should be defined"""
        from lab3_statistics import calculate_average_grade
        assert callable(calculate_average_grade)

    def test_calculate_average_grade_correct_result(self, sample_data):
        """calculate_average_grade should return correct average"""
        from lab3_statistics import calculate_average_grade
        result = calculate_average_grade(sample_data)
        if result is not None:
            expected = (2.45 + 1.80 + 3.20 + 0.95 + 2.10) / 5
            assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"

    def test_calculate_average_grade_empty_list(self, empty_sample_list):
        """calculate_average_grade should handle empty list"""
        from lab3_statistics import calculate_average_grade
        result = calculate_average_grade(empty_sample_list)
        assert result is None, "Should return None for empty list"

    def test_find_depth_range_function_exists(self):
        """find_depth_range function should be defined"""
        from lab3_statistics import find_depth_range
        assert callable(find_depth_range)

    def test_find_depth_range_correct_result(self, sample_data):
        """find_depth_range should return correct min and max"""
        from lab3_statistics import find_depth_range
        result = find_depth_range(sample_data)
        if result is not None:
            assert result[0] == 150, f"Min depth should be 150, got {result[0]}"
            assert result[1] == 410, f"Max depth should be 410, got {result[1]}"

    def test_count_by_rock_type_function_exists(self):
        """count_by_rock_type function should be defined"""
        from lab3_statistics import count_by_rock_type
        assert callable(count_by_rock_type)

    def test_count_by_rock_type_correct_counts(self, sample_data):
        """count_by_rock_type should return correct counts"""
        from lab3_statistics import count_by_rock_type
        result = count_by_rock_type(sample_data)
        if result is not None:
            assert result.get('Granite') == 2, "Should have 2 Granite samples"
            assert result.get('Basalt') == 2, "Should have 2 Basalt samples"
            assert result.get('Sandstone') == 1, "Should have 1 Sandstone sample"

    def test_get_high_grade_samples_function_exists(self):
        """get_high_grade_samples function should be defined"""
        from lab3_statistics import get_high_grade_samples
        assert callable(get_high_grade_samples)

    def test_get_high_grade_samples_correct_filtering(self, sample_data):
        """get_high_grade_samples should filter correctly"""
        from lab3_statistics import get_high_grade_samples
        result = get_high_grade_samples(sample_data, 2.0)
        if result is not None:
            # Grades above 2.0: 2.45, 3.20, 2.10
            assert len(result) == 3, f"Should have 3 samples above 2.0, got {len(result)}"

    def test_calculate_total_depth_function_exists(self):
        """calculate_total_depth function should be defined"""
        from lab3_statistics import calculate_total_depth
        assert callable(calculate_total_depth)

    def test_calculate_total_depth_correct(self, sample_data):
        """calculate_total_depth should return correct sum"""
        from lab3_statistics import calculate_total_depth
        result = calculate_total_depth(sample_data)
        if result is not None:
            expected = 150 + 280 + 175 + 320 + 410
            assert abs(result - expected) < 0.01, f"Expected {expected}, got {result}"

    def test_find_grade_range_function_exists(self):
        """find_grade_range function should be defined"""
        from lab3_statistics import find_grade_range
        assert callable(find_grade_range)

    def test_find_grade_range_correct_result(self, sample_data):
        """find_grade_range should return correct min and max"""
        from lab3_statistics import find_grade_range
        result = find_grade_range(sample_data)
        if result is not None:
            assert result[0] == 0.95, f"Min grade should be 0.95, got {result[0]}"
            assert result[1] == 3.20, f"Max grade should be 3.20, got {result[1]}"

    def test_get_low_grade_samples_function_exists(self):
        """get_low_grade_samples function should be defined"""
        from lab3_statistics import get_low_grade_samples
        assert callable(get_low_grade_samples)

    def test_get_low_grade_samples_correct_filtering(self, sample_data):
        """get_low_grade_samples should filter correctly"""
        from lab3_statistics import get_low_grade_samples
        result = get_low_grade_samples(sample_data, 2.0)
        if result is not None:
            # Grades below 2.0: 1.80, 0.95
            assert len(result) == 2, f"Should have 2 samples below 2.0, got {len(result)}"

    def test_calculate_grade_statistics_function_exists(self):
        """calculate_grade_statistics function should be defined"""
        from lab3_statistics import calculate_grade_statistics
        assert callable(calculate_grade_statistics)

    def test_calculate_grade_statistics_returns_dict(self, sample_data):
        """calculate_grade_statistics should return a dictionary"""
        from lab3_statistics import calculate_grade_statistics
        result = calculate_grade_statistics(sample_data)
        assert result is not None, "Should return a value"
        assert isinstance(result, dict), "Should return a dict"

    def test_get_grade_distribution_function_exists(self):
        """get_grade_distribution function should be defined"""
        from lab3_statistics import get_grade_distribution
        assert callable(get_grade_distribution)

    def test_get_grade_distribution_returns_dict(self, sample_data):
        """get_grade_distribution should return a dictionary"""
        from lab3_statistics import get_grade_distribution
        result = get_grade_distribution(sample_data)
        if result is not None:
            assert isinstance(result, dict), "Should return a dict"

    def test_find_samples_above_average_function_exists(self):
        """find_samples_above_average function should be defined"""
        from lab3_statistics import find_samples_above_average
        assert callable(find_samples_above_average)

    def test_find_samples_above_average_returns_list(self, sample_data):
        """find_samples_above_average should return a list"""
        from lab3_statistics import find_samples_above_average
        result = find_samples_above_average(sample_data)
        if result is not None:
            assert isinstance(result, list), "Should return a list"

    def test_calculate_average_by_rock_type_function_exists(self):
        """calculate_average_by_rock_type function should be defined"""
        from lab3_statistics import calculate_average_by_rock_type
        assert callable(calculate_average_by_rock_type)

    def test_calculate_average_by_rock_type_correct(self, sample_data):
        """calculate_average_by_rock_type should return correct averages"""
        from lab3_statistics import calculate_average_by_rock_type
        result = calculate_average_by_rock_type(sample_data)
        if result is not None:
            granite_avg = result.get('Granite')
            if granite_avg is not None:
                expected = (2.45 + 3.20) / 2
                assert abs(granite_avg - expected) < 0.01, \
                    f"Granite average should be {expected}, got {granite_avg}"


class TestTask5Filters:
    """Tests for Task 5: Filtering and Sorting (lab3_filters.py)"""

    def test_filters_file_exists(self):
        """lab3_filters.py file should exist"""
        assert (SRC_DIR / "lab3_filters.py").exists()

    def test_filter_by_depth_range_function_exists(self):
        """filter_by_depth_range function should be defined"""
        from lab3_filters import filter_by_depth_range
        assert callable(filter_by_depth_range)

    def test_filter_by_depth_range_correct_filtering(self, sample_data):
        """filter_by_depth_range should filter correctly"""
        from lab3_filters import filter_by_depth_range
        result = filter_by_depth_range(sample_data, 200, 350)
        if result is not None:
            # Depths in range [200, 350]: 280, 320
            assert len(result) == 2, f"Should have 2 samples, got {len(result)}"

    def test_filter_by_rock_types_function_exists(self):
        """filter_by_rock_types function should be defined"""
        from lab3_filters import filter_by_rock_types
        assert callable(filter_by_rock_types)

    def test_filter_by_rock_types_correct_filtering(self, sample_data):
        """filter_by_rock_types should filter correctly"""
        from lab3_filters import filter_by_rock_types
        result = filter_by_rock_types(sample_data, ['Granite', 'Basalt'])
        if result is not None:
            assert len(result) == 4, f"Should have 4 samples, got {len(result)}"

    def test_sort_by_grade_function_exists(self):
        """sort_by_grade function should be defined"""
        from lab3_filters import sort_by_grade
        assert callable(sort_by_grade)

    def test_sort_by_grade_ascending(self, sample_data):
        """sort_by_grade should sort ascending correctly"""
        from lab3_filters import sort_by_grade
        result = sort_by_grade(sample_data, descending=False)
        if result is not None:
            grades = [s['grade'] for s in result]
            assert grades == sorted(grades), "Should be sorted ascending"

    def test_sort_by_grade_descending(self, sample_data):
        """sort_by_grade should sort descending correctly"""
        from lab3_filters import sort_by_grade
        result = sort_by_grade(sample_data, descending=True)
        if result is not None:
            grades = [s['grade'] for s in result]
            assert grades == sorted(grades, reverse=True), "Should be sorted descending"

    def test_sort_by_grade_does_not_modify_original(self, sample_data):
        """sort_by_grade should not modify original list"""
        from lab3_filters import sort_by_grade
        original_first = sample_data[0]['grade']
        sort_by_grade(sample_data, descending=True)
        assert sample_data[0]['grade'] == original_first, "Should not modify original"

    def test_get_top_n_by_grade_function_exists(self):
        """get_top_n_by_grade function should be defined"""
        from lab3_filters import get_top_n_by_grade
        assert callable(get_top_n_by_grade)

    def test_get_top_n_by_grade_correct_result(self, sample_data):
        """get_top_n_by_grade should return top N samples"""
        from lab3_filters import get_top_n_by_grade
        result = get_top_n_by_grade(sample_data, 2)
        if result is not None:
            assert len(result) == 2, "Should return 2 samples"
            # Top 2 grades should be 3.20 and 2.45
            grades = [s['grade'] for s in result]
            assert 3.20 in grades, "Should include highest grade (3.20)"
            assert 2.45 in grades, "Should include second highest grade (2.45)"

    def test_group_by_rock_type_function_exists(self):
        """group_by_rock_type function should be defined"""
        from lab3_filters import group_by_rock_type
        assert callable(group_by_rock_type)

    def test_group_by_rock_type_correct_grouping(self, sample_data):
        """group_by_rock_type should group samples correctly"""
        from lab3_filters import group_by_rock_type
        result = group_by_rock_type(sample_data)
        if result is not None:
            assert 'Granite' in result, "Should have Granite group"
            assert len(result['Granite']) == 2, "Should have 2 Granite samples"

    def test_extract_field_function_exists(self):
        """extract_field function should be defined"""
        from lab3_filters import extract_field
        assert callable(extract_field)

    def test_extract_field_correct_values(self, sample_data):
        """extract_field should extract correct values"""
        from lab3_filters import extract_field
        result = extract_field(sample_data, 'grade')
        if result is not None:
            expected = [2.45, 1.80, 3.20, 0.95, 2.10]
            assert result == expected, f"Expected {expected}, got {result}"

    def test_filter_by_grade_range_function_exists(self):
        """filter_by_grade_range function should be defined"""
        from lab3_filters import filter_by_grade_range
        assert callable(filter_by_grade_range)

    def test_filter_by_grade_range_correct_filtering(self, sample_data):
        """filter_by_grade_range should filter correctly"""
        from lab3_filters import filter_by_grade_range
        result = filter_by_grade_range(sample_data, 1.5, 3.0)
        if result is not None:
            # Grades in [1.5, 3.0]: 2.45, 1.80, 2.10
            assert len(result) == 3, f"Should have 3 samples in range 1.5-3.0, got {len(result)}"

    def test_exclude_rock_types_function_exists(self):
        """exclude_rock_types function should be defined"""
        from lab3_filters import exclude_rock_types
        assert callable(exclude_rock_types)

    def test_exclude_rock_types_correct_filtering(self, sample_data):
        """exclude_rock_types should exclude specified types"""
        from lab3_filters import exclude_rock_types
        result = exclude_rock_types(sample_data, ['Granite'])
        if result is not None:
            # Non-Granite: Basalt(1.80), Sandstone(0.95), Basalt(2.10) = 3
            assert len(result) == 3, f"Should have 3 non-Granite samples, got {len(result)}"
            rock_types = [s['rock_type'] for s in result]
            assert 'Granite' not in rock_types, "Should not contain Granite"

    def test_sort_by_depth_function_exists(self):
        """sort_by_depth function should be defined"""
        from lab3_filters import sort_by_depth
        assert callable(sort_by_depth)

    def test_sort_by_depth_ascending(self, sample_data):
        """sort_by_depth should sort ascending correctly"""
        from lab3_filters import sort_by_depth
        result = sort_by_depth(sample_data, descending=False)
        if result is not None:
            depths = [s['depth'] for s in result]
            assert depths == sorted(depths), "Should be sorted ascending by depth"

    def test_get_bottom_n_by_grade_function_exists(self):
        """get_bottom_n_by_grade function should be defined"""
        from lab3_filters import get_bottom_n_by_grade
        assert callable(get_bottom_n_by_grade)

    def test_get_bottom_n_by_grade_correct(self, sample_data):
        """get_bottom_n_by_grade should return lowest N samples"""
        from lab3_filters import get_bottom_n_by_grade
        result = get_bottom_n_by_grade(sample_data, 2)
        if result is not None:
            assert len(result) == 2, "Should return 2 samples"
            grades = [s['grade'] for s in result]
            assert 0.95 in grades, "Should include lowest grade (0.95)"

    def test_get_deepest_samples_function_exists(self):
        """get_deepest_samples function should be defined"""
        from lab3_filters import get_deepest_samples
        assert callable(get_deepest_samples)

    def test_get_deepest_samples_correct(self, sample_data):
        """get_deepest_samples should return N deepest samples"""
        from lab3_filters import get_deepest_samples
        result = get_deepest_samples(sample_data, 2)
        if result is not None:
            assert len(result) == 2, "Should return 2 samples"
            depths = [s['depth'] for s in result]
            assert 410 in depths, "Should include deepest sample (410m)"

    def test_filter_and_sort_function_exists(self):
        """filter_and_sort function should be defined"""
        from lab3_filters import filter_and_sort
        assert callable(filter_and_sort)

    def test_filter_and_sort_with_rock_type(self, sample_data):
        """filter_and_sort should filter by rock type and sort"""
        from lab3_filters import filter_and_sort
        result = filter_and_sort(sample_data, rock_types=['Granite'], sort_by='grade', descending=True)
        if result is not None:
            assert len(result) == 2, "Should have 2 Granite samples"
            grades = [s['grade'] for s in result]
            assert grades == sorted(grades, reverse=True), "Should be sorted descending"

    def test_transform_grades_function_exists(self):
        """transform_grades function should be defined"""
        from lab3_filters import transform_grades
        assert callable(transform_grades)

    def test_transform_grades_correct(self, sample_data):
        """transform_grades should multiply all grades"""
        from lab3_filters import transform_grades
        result = transform_grades(sample_data, 2.0)
        if result is not None:
            assert len(result) == len(sample_data), "Should have same number of samples"
            assert abs(result[0]['grade'] - 4.90) < 0.01, "First grade should be 2.45 * 2.0 = 4.90"
            # Check original not modified
            assert sample_data[0]['grade'] == 2.45, "Original should not be modified"
