"""
Lab 3 Task 5: Filtering and Sorting Samples
Functions for filtering and sorting geological sample collections.

Your Name: [YOUR NAME]
Student ID: [YOUR ID]
"""


def filter_by_depth_range(samples, min_depth, max_depth):
    """
    Filter samples within the given depth range.

    Args:
        samples: List of sample dictionaries
        min_depth: Minimum depth (inclusive)
        max_depth: Maximum depth (inclusive)

    Returns:
        List of samples where min_depth <= depth <= max_depth
    """
    # TODO: Use list comprehension to filter samples
    pass


def filter_by_grade_range(samples, min_grade, max_grade):
    """
    Filter samples within the given grade range.

    Args:
        samples: List of sample dictionaries
        min_grade: Minimum grade (inclusive)
        max_grade: Maximum grade (inclusive)

    Returns:
        List of samples where min_grade <= grade <= max_grade
    """
    # TODO: Use list comprehension to filter samples
    pass


def filter_by_rock_types(samples, rock_types):
    """
    Filter samples matching any of the given rock types.

    Args:
        samples: List of sample dictionaries
        rock_types: List of rock type strings to match

    Returns:
        List of samples where rock_type is in rock_types list
    """
    # TODO: Use list comprehension with 'in' operator
    pass


def exclude_rock_types(samples, rock_types):
    """
    Filter samples excluding certain rock types.

    Args:
        samples: List of sample dictionaries
        rock_types: List of rock types to exclude

    Returns:
        List of samples where rock_type is NOT in rock_types
    """
    # TODO: Use list comprehension with 'not in' operator
    pass


def sort_by_grade(samples, descending=False):
    """
    Sort samples by grade.

    Args:
        samples: List of sample dictionaries
        descending: If True, sort highest to lowest

    Returns:
        New sorted list (does not modify original)
    """
    # TODO: Use sorted() with key parameter
    # TODO: Use reverse parameter for descending
    pass


def sort_by_depth(samples, descending=False):
    """
    Sort samples by depth.

    Args:
        samples: List of sample dictionaries
        descending: If True, sort deepest first

    Returns:
        New sorted list (does not modify original)
    """
    # TODO: Use sorted() with key parameter
    pass


def sort_by_rock_type(samples):
    """
    Sort samples alphabetically by rock type.

    Args:
        samples: List of sample dictionaries

    Returns:
        New sorted list (does not modify original)
    """
    # TODO: Use sorted() with key parameter
    pass


def sort_by_multiple_fields(samples, primary='grade', secondary='depth', primary_desc=True):
    """
    Sort samples by multiple fields.

    Args:
        samples: List of sample dictionaries
        primary: Primary sort field
        secondary: Secondary sort field
        primary_desc: If True, primary sort is descending

    Returns:
        New sorted list
    """
    # TODO: Use sorted() with tuple key for multiple fields
    # Hint: sorted(samples, key=lambda x: (-x[primary], x[secondary]))
    pass


def get_top_n_by_grade(samples, n):
    """
    Get the top N samples by grade.

    Args:
        samples: List of sample dictionaries
        n: Number of samples to return

    Returns:
        List of top N samples sorted by grade (highest first)
    """
    # TODO: Sort descending by grade
    # TODO: Return first n elements
    pass


def get_bottom_n_by_grade(samples, n):
    """
    Get the bottom N samples by grade.

    Args:
        samples: List of sample dictionaries
        n: Number of samples to return

    Returns:
        List of bottom N samples sorted by grade (lowest first)
    """
    # TODO: Sort ascending by grade
    # TODO: Return first n elements
    pass


def get_deepest_samples(samples, n):
    """
    Get the N deepest samples.

    Args:
        samples: List of sample dictionaries
        n: Number of samples to return

    Returns:
        List of N deepest samples
    """
    # TODO: Sort by depth descending
    # TODO: Return first n elements
    pass


def filter_and_sort(samples, rock_types=None, min_grade=None, max_grade=None,
                    min_depth=None, max_depth=None, sort_by='grade', descending=True):
    """
    Apply multiple filters and sort the results.

    Args:
        samples: List of sample dictionaries
        rock_types: List of rock types to include (None = all)
        min_grade: Minimum grade filter (None = no min)
        max_grade: Maximum grade filter (None = no max)
        min_depth: Minimum depth filter (None = no min)
        max_depth: Maximum depth filter (None = no max)
        sort_by: Field to sort by ('grade' or 'depth')
        descending: Sort direction

    Returns:
        Filtered and sorted list of samples
    """
    # TODO: Start with all samples
    # TODO: Apply each filter if the parameter is not None
    # TODO: Sort by the specified field
    # TODO: Return the result
    pass


def group_by_rock_type(samples):
    """
    Group samples by rock type.

    Args:
        samples: List of sample dictionaries

    Returns:
        Dictionary with rock_type as key and list of samples as value
    """
    # TODO: Create empty dictionary
    # TODO: Iterate through samples
    # TODO: Add each sample to the appropriate list
    # TODO: Return the grouped dictionary
    pass


def extract_field(samples, field):
    """
    Extract a single field from all samples.

    Args:
        samples: List of sample dictionaries
        field: Field name to extract

    Returns:
        List of values for the specified field
    """
    # TODO: Use list comprehension to extract values
    pass


def transform_grades(samples, multiplier):
    """
    Create new list with transformed grades.

    Args:
        samples: List of sample dictionaries
        multiplier: Value to multiply all grades by

    Returns:
        New list of samples with transformed grades
    """
    # TODO: Create new samples with modified grades
    # TODO: Don't modify the original samples
    pass


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Lab 3 Task 5: Filtering and Sorting")
    print("=" * 50)

    # Create sample data - use your assigned values from README.md
    samples = [
        {'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.45, 'depth': 150},
        {'sample_id': 'GEO-002', 'rock_type': 'Basalt', 'grade': 1.80, 'depth': 280},
        {'sample_id': 'GEO-003', 'rock_type': 'Granite', 'grade': 3.20, 'depth': 175},
        {'sample_id': 'GEO-004', 'rock_type': 'Sandstone', 'grade': 0.95, 'depth': 320},
        {'sample_id': 'GEO-005', 'rock_type': 'Basalt', 'grade': 2.10, 'depth': 410},
        {'sample_id': 'GEO-006', 'rock_type': 'Granite', 'grade': 1.55, 'depth': 225},
        {'sample_id': 'GEO-007', 'rock_type': 'Schist', 'grade': 2.80, 'depth': 195},
        {'sample_id': 'GEO-008', 'rock_type': 'Basalt', 'grade': 0.75, 'depth': 485},
        {'sample_id': 'GEO-009', 'rock_type': 'Sandstone', 'grade': 1.25, 'depth': 350},
        {'sample_id': 'GEO-010', 'rock_type': 'Granite', 'grade': 4.10, 'depth': 165},
    ]

    # Filter by depth range
    print("\n1. Filter by Depth Range (200-400m)")
    print("-" * 30)
    filtered = filter_by_depth_range(samples, 200, 400)
    if filtered:
        for s in filtered:
            print(f"  {s['sample_id']}: depth={s['depth']}m")
    else:
        print("  No samples in range")

    # Filter by grade range
    print("\n2. Filter by Grade Range (1.5-3.0)")
    print("-" * 30)
    filtered = filter_by_grade_range(samples, 1.5, 3.0)
    if filtered:
        for s in filtered:
            print(f"  {s['sample_id']}: grade={s['grade']}")

    # Filter by rock types
    print("\n3. Filter by Rock Types (Granite, Basalt)")
    print("-" * 30)
    filtered = filter_by_rock_types(samples, ['Granite', 'Basalt'])
    if filtered:
        for s in filtered:
            print(f"  {s['sample_id']}: {s['rock_type']}")

    # Sort by grade
    print("\n4. Sort by Grade (Descending)")
    print("-" * 30)
    sorted_samples = sort_by_grade(samples, descending=True)
    if sorted_samples:
        for s in sorted_samples:
            print(f"  {s['sample_id']}: grade={s['grade']}")

    # Sort by depth
    print("\n5. Sort by Depth (Ascending)")
    print("-" * 30)
    sorted_samples = sort_by_depth(samples, descending=False)
    if sorted_samples:
        for s in sorted_samples[:5]:  # Show first 5
            print(f"  {s['sample_id']}: depth={s['depth']}m")

    # Top N by grade
    print("\n6. Top 3 by Grade")
    print("-" * 30)
    top_samples = get_top_n_by_grade(samples, 3)
    if top_samples:
        for i, s in enumerate(top_samples, 1):
            print(f"  #{i}: {s['sample_id']} - grade={s['grade']}")

    # Bottom N by grade
    print("\n7. Bottom 3 by Grade")
    print("-" * 30)
    bottom_samples = get_bottom_n_by_grade(samples, 3)
    if bottom_samples:
        for i, s in enumerate(bottom_samples, 1):
            print(f"  #{i}: {s['sample_id']} - grade={s['grade']}")

    # Deepest samples
    print("\n8. 3 Deepest Samples")
    print("-" * 30)
    deepest = get_deepest_samples(samples, 3)
    if deepest:
        for s in deepest:
            print(f"  {s['sample_id']}: depth={s['depth']}m")

    # Combined filter and sort
    print("\n9. Filter and Sort Combined")
    print("-" * 30)
    print("  (Granite only, grade > 1.5, sorted by grade desc)")
    result = filter_and_sort(
        samples,
        rock_types=['Granite'],
        min_grade=1.5,
        sort_by='grade',
        descending=True
    )
    if result:
        for s in result:
            print(f"  {s['sample_id']}: {s['rock_type']}, grade={s['grade']}")

    # Group by rock type
    print("\n10. Group by Rock Type")
    print("-" * 30)
    groups = group_by_rock_type(samples)
    if groups:
        for rock_type, group_samples in groups.items():
            print(f"  {rock_type}: {len(group_samples)} samples")

    # Extract field
    print("\n11. Extract Grades")
    print("-" * 30)
    grades = extract_field(samples, 'grade')
    if grades:
        print(f"  Grades: {grades}")

    print("\n" + "=" * 50)
    print("End of Task 5")
    print("=" * 50)
