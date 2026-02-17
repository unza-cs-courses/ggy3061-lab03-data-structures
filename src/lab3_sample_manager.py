"""
Lab 3 Task 3: Sample Collection Manager
Functions to manage a collection of geological samples.

Your Name: [YOUR NAME]
Student ID: [YOUR ID]
"""


def create_sample_collection():
    """
    Create and return an empty sample collection.

    Returns:
        An empty list to store sample dictionaries
    """
    # TODO: Return an empty list
    pass


def add_sample(collection, sample_id, rock_type, grade, depth):
    """
    Add a new sample to the collection.

    Args:
        collection: The sample collection (list)
        sample_id: Unique identifier for the sample
        rock_type: Type of rock
        grade: Ore grade value
        depth: Sample depth in meters

    Returns:
        The updated collection
    """
    # TODO: Create a sample dictionary with the given values
    # TODO: Append it to the collection
    # TODO: Return the updated collection
    pass


def get_sample_count(collection):
    """
    Get the number of samples in the collection.

    Args:
        collection: The sample collection

    Returns:
        Integer count of samples
    """
    # TODO: Return the length of the collection
    pass


def find_sample_by_id(collection, sample_id):
    """
    Find a sample by its ID.

    Args:
        collection: The sample collection
        sample_id: ID to search for

    Returns:
        The sample dictionary if found, None otherwise
    """
    # TODO: Iterate through collection
    # TODO: Return the sample if sample_id matches
    # TODO: Return None if not found
    pass


def find_by_rock_type(collection, rock_type):
    """
    Find all samples matching the given rock type.

    Args:
        collection: The sample collection
        rock_type: Rock type to search for

    Returns:
        List of matching sample dictionaries
    """
    # TODO: Use list comprehension to filter samples
    # TODO: Return all samples where rock_type matches
    pass


def find_by_depth_range(collection, min_depth, max_depth):
    """
    Find samples within a depth range.

    Args:
        collection: The sample collection
        min_depth: Minimum depth (inclusive)
        max_depth: Maximum depth (inclusive)

    Returns:
        List of samples within the depth range
    """
    # TODO: Return samples where min_depth <= depth <= max_depth
    pass


def update_grade(collection, sample_id, new_grade):
    """
    Update the grade of a sample by its ID.

    Args:
        collection: The sample collection
        sample_id: ID of sample to update
        new_grade: New grade value

    Returns:
        True if found and updated, False otherwise
    """
    # TODO: Find the sample by ID
    # TODO: Update its grade if found
    # TODO: Return True if updated, False if not found
    pass


def update_sample(collection, sample_id, **updates):
    """
    Update multiple fields of a sample.

    Args:
        collection: The sample collection
        sample_id: ID of sample to update
        **updates: Keyword arguments with fields to update

    Returns:
        True if found and updated, False otherwise
    """
    # TODO: Find the sample by ID
    # TODO: Update all provided fields using the updates dict
    # TODO: Return True if updated, False if not found
    pass


def remove_sample(collection, sample_id):
    """
    Remove a sample from the collection by ID.

    Args:
        collection: The sample collection
        sample_id: ID of sample to remove

    Returns:
        True if removed, False if not found
    """
    # TODO: Find the sample by ID
    # TODO: Remove it from the collection if found
    # TODO: Return True if removed, False if not found
    pass


def get_all_sample_ids(collection):
    """
    Get a list of all sample IDs.

    Args:
        collection: The sample collection

    Returns:
        List of sample ID strings
    """
    # TODO: Use list comprehension to extract all sample_ids
    pass


def get_unique_rock_types(collection):
    """
    Get unique rock types in the collection.

    Args:
        collection: The sample collection

    Returns:
        List of unique rock type strings
    """
    # TODO: Extract all rock types
    # TODO: Convert to set and back to list to get unique values
    pass


def bulk_add_samples(collection, samples_data):
    """
    Add multiple samples at once.

    Args:
        collection: The sample collection
        samples_data: List of tuples (sample_id, rock_type, grade, depth)

    Returns:
        Number of samples added
    """
    # TODO: Iterate through samples_data
    # TODO: Add each sample to collection
    # TODO: Return count of samples added
    pass


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Lab 3 Task 3: Sample Collection Manager")
    print("=" * 50)

    # Create collection
    print("\n1. Creating Collection")
    print("-" * 30)
    collection = create_sample_collection()
    print(f"Empty collection created: {collection}")

    # Add samples - use your assigned rock types from README.md
    print("\n2. Adding Samples")
    print("-" * 30)
    # TODO: Add samples using your assigned rock types
    # Example:
    add_sample(collection, 'GEO-001', 'Granite', 2.45, 150)
    add_sample(collection, 'GEO-002', 'Basalt', 1.80, 280)
    add_sample(collection, 'GEO-003', 'Granite', 3.20, 175)
    add_sample(collection, 'GEO-004', 'Sandstone', 0.95, 320)
    add_sample(collection, 'GEO-005', 'Basalt', 2.10, 410)

    count = get_sample_count(collection)
    print(f"Total samples: {count}")

    # Display all samples
    print("\nAll samples:")
    if collection:
        for sample in collection:
            print(f"  {sample}")
    else:
        print("  No samples yet")

    # Find by ID
    print("\n3. Finding Sample by ID")
    print("-" * 30)
    sample = find_sample_by_id(collection, 'GEO-002')
    print(f"Found GEO-002: {sample}")
    sample = find_sample_by_id(collection, 'GEO-999')
    print(f"Found GEO-999: {sample}")

    # Find by rock type
    print("\n4. Finding by Rock Type")
    print("-" * 30)
    granite_samples = find_by_rock_type(collection, 'Granite')
    print(f"Granite samples: {len(granite_samples) if granite_samples else 0}")
    if granite_samples:
        for s in granite_samples:
            print(f"  {s['sample_id']}: grade={s['grade']}")

    # Find by depth range
    print("\n5. Finding by Depth Range")
    print("-" * 30)
    deep_samples = find_by_depth_range(collection, 200, 400)
    print(f"Samples between 200-400m: {len(deep_samples) if deep_samples else 0}")

    # Update grade
    print("\n6. Updating Grade")
    print("-" * 30)
    original = find_sample_by_id(collection, 'GEO-001')
    print(f"Before update: {original}")
    updated = update_grade(collection, 'GEO-001', 2.85)
    print(f"Update successful: {updated}")
    after = find_sample_by_id(collection, 'GEO-001')
    print(f"After update: {after}")

    # Remove sample
    print("\n7. Removing Sample")
    print("-" * 30)
    print(f"Before removal: {get_sample_count(collection)} samples")
    removed = remove_sample(collection, 'GEO-004')
    print(f"Removed GEO-004: {removed}")
    print(f"After removal: {get_sample_count(collection)} samples")

    # Get unique rock types
    print("\n8. Unique Rock Types")
    print("-" * 30)
    rock_types = get_unique_rock_types(collection)
    print(f"Rock types in collection: {rock_types}")

    # Get all IDs
    print("\n9. All Sample IDs")
    print("-" * 30)
    ids = get_all_sample_ids(collection)
    print(f"Sample IDs: {ids}")

    print("\n" + "=" * 50)
    print("End of Task 3")
    print("=" * 50)
