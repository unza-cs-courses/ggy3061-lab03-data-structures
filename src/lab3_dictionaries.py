"""
Lab 3 Task 2: Dictionary Operations
Demonstrates dictionary creation, access, and methods with geological sample records.

Your Name: [YOUR NAME]
Student ID: [YOUR ID]
"""


def create_sample_record(sample_id, rock_type, grade, depth):
    """
    Create a dictionary representing a geological sample.

    Args:
        sample_id: Unique identifier for the sample
        rock_type: Type of rock (e.g., 'Granite', 'Basalt')
        grade: Ore grade value
        depth: Depth at which sample was collected (meters)

    Returns:
        A dictionary with the sample data
    """
    # TODO: Create and return a dictionary with keys:
    # 'sample_id', 'rock_type', 'grade', 'depth'
    pass


def access_sample_values(sample):
    """
    Demonstrate different ways to access dictionary values.

    Args:
        sample: A sample dictionary

    Returns:
        A dictionary showing different access methods
    """
    # TODO: Return a dictionary with:
    # - 'direct_access': value accessed with sample['rock_type']
    # - 'get_method': value accessed with sample.get('grade')
    # - 'get_with_default': sample.get('analyst', 'Unknown')
    # - 'all_keys': list of all keys
    # - 'all_values': list of all values
    pass


def demonstrate_dictionary_methods(sample):
    """
    Demonstrate various dictionary methods.

    Args:
        sample: A sample dictionary

    Returns:
        A dictionary with results of method calls
    """
    # TODO: Return a dictionary with:
    # - 'keys': list(sample.keys())
    # - 'values': list(sample.values())
    # - 'items': list(sample.items())
    # - 'has_grade': 'grade' in sample
    # - 'has_analyst': 'analyst' in sample
    pass


def update_sample(sample, updates):
    """
    Update a sample dictionary with new values.

    Args:
        sample: Original sample dictionary
        updates: Dictionary with updates to apply

    Returns:
        Updated sample dictionary (copy, not modifying original)
    """
    # TODO: Create a copy of sample
    # TODO: Use update() method to apply updates
    # TODO: Return the updated copy
    pass


def create_nested_sample_database():
    """
    Create a nested dictionary structure for multiple samples.

    Returns:
        A dictionary where keys are sample_ids and values are sample records
    """
    # TODO: Create a dictionary with at least 3 samples
    # Each key should be a sample_id (e.g., 'GEO-001')
    # Each value should be a dictionary with rock_type, grade, depth
    #
    # Example structure:
    # {
    #     'GEO-001': {'rock_type': 'Granite', 'grade': 2.5, 'depth': 150},
    #     'GEO-002': {'rock_type': 'Basalt', 'grade': 1.8, 'depth': 280},
    #     ...
    # }
    #
    # Use your assigned rock types from README.md
    pass


def query_sample_database(database, sample_id):
    """
    Query the sample database for a specific sample.

    Args:
        database: The nested sample database
        sample_id: ID of sample to find

    Returns:
        Sample record if found, None otherwise
    """
    # TODO: Use get() to safely retrieve the sample
    pass


def add_sample_to_database(database, sample_id, rock_type, grade, depth):
    """
    Add a new sample to the database.

    Args:
        database: The sample database
        sample_id: ID for the new sample
        rock_type: Rock type
        grade: Grade value
        depth: Depth value

    Returns:
        Updated database (modifies in place and returns)
    """
    # TODO: Add new sample to database
    # Return the updated database
    pass


def get_all_rock_types(database):
    """
    Get a list of unique rock types from the database.

    Args:
        database: The sample database

    Returns:
        List of unique rock types
    """
    # TODO: Extract all rock_type values from the database
    # Return unique values as a list
    pass


def filter_by_minimum_grade(database, min_grade):
    """
    Filter samples by minimum grade threshold.

    Args:
        database: The sample database
        min_grade: Minimum grade threshold

    Returns:
        Dictionary of samples meeting the threshold
    """
    # TODO: Return a new dictionary containing only samples
    # where grade >= min_grade
    # Use dictionary comprehension
    pass


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Lab 3 Task 2: Dictionary Operations")
    print("=" * 50)

    # Create a sample record
    print("\n1. Creating Sample Record")
    print("-" * 30)
    sample = create_sample_record('GEO-001', 'Granite', 2.45, 175)
    if sample:
        print(f"Sample: {sample}")

    # Access values
    print("\n2. Accessing Dictionary Values")
    print("-" * 30)
    if sample:
        access = access_sample_values(sample)
        if access:
            print(f"Direct access (rock_type): {access.get('direct_access')}")
            print(f"Get method (grade): {access.get('get_method')}")
            print(f"Get with default (analyst): {access.get('get_with_default')}")
            print(f"All keys: {access.get('all_keys')}")
            print(f"All values: {access.get('all_values')}")

    # Dictionary methods
    print("\n3. Dictionary Methods")
    print("-" * 30)
    if sample:
        methods = demonstrate_dictionary_methods(sample)
        if methods:
            print(f"Keys: {methods.get('keys')}")
            print(f"Values: {methods.get('values')}")
            print(f"Items: {methods.get('items')}")
            print(f"Has 'grade': {methods.get('has_grade')}")
            print(f"Has 'analyst': {methods.get('has_analyst')}")

    # Update sample
    print("\n4. Updating Sample")
    print("-" * 30)
    if sample:
        updates = {'grade': 2.75, 'analyst': 'Dr. Smith'}
        updated = update_sample(sample, updates)
        if updated:
            print(f"Original: {sample}")
            print(f"Updated: {updated}")

    # Nested database
    print("\n5. Sample Database")
    print("-" * 30)
    database = create_nested_sample_database()
    if database:
        print("Database contents:")
        for sid, data in database.items():
            print(f"  {sid}: {data}")

    # Query database
    print("\n6. Querying Database")
    print("-" * 30)
    if database:
        result = query_sample_database(database, 'GEO-001')
        print(f"Query 'GEO-001': {result}")
        result = query_sample_database(database, 'GEO-999')
        print(f"Query 'GEO-999': {result}")

    # Get rock types
    print("\n7. Unique Rock Types")
    print("-" * 30)
    if database:
        rock_types = get_all_rock_types(database)
        if rock_types:
            print(f"Rock types in database: {rock_types}")

    # Filter by grade
    print("\n8. Filter by Grade")
    print("-" * 30)
    if database:
        # Use a threshold within your assigned grade range
        filtered = filter_by_minimum_grade(database, 2.0)
        if filtered:
            print(f"Samples with grade >= 2.0:")
            for sid, data in filtered.items():
                print(f"  {sid}: grade = {data.get('grade')}")

    print("\n" + "=" * 50)
    print("End of Task 2")
    print("=" * 50)
