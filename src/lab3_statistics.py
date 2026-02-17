"""
Lab 3 Task 4: Computing Statistics from Lists
Functions to compute statistics from geological sample collections.

Your Name: [YOUR NAME]
Student ID: [YOUR ID]
"""


def calculate_average_grade(samples):
    """
    Calculate the average grade from a list of sample dictionaries.

    Args:
        samples: List of sample dictionaries with 'grade' key

    Returns:
        Average grade as a float, or None if list is empty
    """
    # TODO: Handle empty list case
    # TODO: Extract all grades using list comprehension
    # TODO: Calculate and return the average
    pass


def calculate_total_depth(samples):
    """
    Calculate the total (sum) of all sample depths.

    Args:
        samples: List of sample dictionaries with 'depth' key

    Returns:
        Sum of all depths
    """
    # TODO: Use list comprehension to extract depths
    # TODO: Return the sum
    pass


def find_depth_range(samples):
    """
    Find the minimum and maximum depths.

    Args:
        samples: List of sample dictionaries with 'depth' key

    Returns:
        Tuple (min_depth, max_depth), or (None, None) if empty
    """
    # TODO: Handle empty list case
    # TODO: Extract depths
    # TODO: Return tuple with min and max
    pass


def find_grade_range(samples):
    """
    Find the minimum and maximum grades.

    Args:
        samples: List of sample dictionaries with 'grade' key

    Returns:
        Tuple (min_grade, max_grade), or (None, None) if empty
    """
    # TODO: Similar to find_depth_range but for grades
    pass


def count_by_rock_type(samples):
    """
    Count samples for each rock type.

    Args:
        samples: List of sample dictionaries with 'rock_type' key

    Returns:
        Dictionary with rock_type as key and count as value
    """
    # TODO: Create an empty dictionary for counts
    # TODO: Iterate through samples
    # TODO: Increment count for each rock type
    # TODO: Return the counts dictionary
    pass


def get_high_grade_samples(samples, threshold):
    """
    Return samples with grade above threshold.

    Args:
        samples: List of sample dictionaries
        threshold: Minimum grade threshold

    Returns:
        List of samples with grade > threshold
    """
    # TODO: Use list comprehension with condition
    pass


def get_low_grade_samples(samples, threshold):
    """
    Return samples with grade below threshold.

    Args:
        samples: List of sample dictionaries
        threshold: Maximum grade threshold

    Returns:
        List of samples with grade < threshold
    """
    # TODO: Use list comprehension with condition
    pass


def calculate_grade_statistics(samples):
    """
    Calculate comprehensive grade statistics.

    Args:
        samples: List of sample dictionaries

    Returns:
        Dictionary with statistics: count, sum, min, max, average, range
    """
    # TODO: Calculate all statistics and return as dictionary
    # Handle empty list case
    pass


def calculate_average_by_rock_type(samples):
    """
    Calculate average grade for each rock type.

    Args:
        samples: List of sample dictionaries

    Returns:
        Dictionary with rock_type as key and average grade as value
    """
    # TODO: Group samples by rock type
    # TODO: Calculate average grade for each group
    # TODO: Return dictionary of averages
    pass


def get_grade_distribution(samples, bins=None):
    """
    Get distribution of grades across bins.

    Args:
        samples: List of sample dictionaries
        bins: List of bin edges (default: [0, 1, 2, 3, 4, 5])

    Returns:
        Dictionary with bin labels as keys and counts as values
    """
    if bins is None:
        bins = [0, 1, 2, 3, 4, 5]

    # TODO: Create bins like '0-1', '1-2', etc.
    # TODO: Count samples in each bin
    # TODO: Return distribution dictionary
    pass


def find_samples_above_average(samples):
    """
    Find samples with grade above the collection average.

    Args:
        samples: List of sample dictionaries

    Returns:
        List of samples with above-average grades
    """
    # TODO: Calculate average grade
    # TODO: Filter samples above average
    # TODO: Return the filtered list
    pass


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Lab 3 Task 4: Computing Statistics")
    print("=" * 50)

    # Create sample data - use your assigned rock types and grade range
    # Check README.md for your values
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

    # Average grade
    print("\n1. Average Grade")
    print("-" * 30)
    avg = calculate_average_grade(samples)
    print(f"Average grade: {avg:.2f}" if avg else "No samples")

    # Total depth
    print("\n2. Total Depth")
    print("-" * 30)
    total = calculate_total_depth(samples)
    print(f"Total depth: {total} meters" if total else "No samples")

    # Depth range
    print("\n3. Depth Range")
    print("-" * 30)
    depth_range = find_depth_range(samples)
    if depth_range and depth_range[0] is not None:
        print(f"Min depth: {depth_range[0]} m")
        print(f"Max depth: {depth_range[1]} m")
        print(f"Range: {depth_range[1] - depth_range[0]} m")

    # Grade range
    print("\n4. Grade Range")
    print("-" * 30)
    grade_range = find_grade_range(samples)
    if grade_range and grade_range[0] is not None:
        print(f"Min grade: {grade_range[0]}")
        print(f"Max grade: {grade_range[1]}")

    # Count by rock type
    print("\n5. Count by Rock Type")
    print("-" * 30)
    counts = count_by_rock_type(samples)
    if counts:
        for rock, count in counts.items():
            print(f"  {rock}: {count}")

    # High grade samples
    print("\n6. High Grade Samples (> 2.0)")
    print("-" * 30)
    high_grade = get_high_grade_samples(samples, 2.0)
    if high_grade:
        for s in high_grade:
            print(f"  {s['sample_id']}: {s['grade']}")
    else:
        print("  No samples above threshold")

    # Grade statistics
    print("\n7. Grade Statistics")
    print("-" * 30)
    stats = calculate_grade_statistics(samples)
    if stats:
        print(f"  Count: {stats.get('count')}")
        print(f"  Sum: {stats.get('sum'):.2f}" if stats.get('sum') else "")
        print(f"  Min: {stats.get('min')}")
        print(f"  Max: {stats.get('max')}")
        print(f"  Average: {stats.get('average'):.2f}" if stats.get('average') else "")
        print(f"  Range: {stats.get('range'):.2f}" if stats.get('range') else "")

    # Average by rock type
    print("\n8. Average Grade by Rock Type")
    print("-" * 30)
    avg_by_type = calculate_average_by_rock_type(samples)
    if avg_by_type:
        for rock, avg in sorted(avg_by_type.items()):
            print(f"  {rock}: {avg:.2f}")

    # Grade distribution
    print("\n9. Grade Distribution")
    print("-" * 30)
    distribution = get_grade_distribution(samples)
    if distribution:
        for bin_label, count in distribution.items():
            bar = '*' * count
            print(f"  {bin_label}: {bar} ({count})")

    # Above average samples
    print("\n10. Above Average Samples")
    print("-" * 30)
    above_avg = find_samples_above_average(samples)
    if above_avg:
        print(f"  {len(above_avg)} samples above average:")
        for s in above_avg:
            print(f"    {s['sample_id']}: {s['grade']}")

    print("\n" + "=" * 50)
    print("End of Task 4")
    print("=" * 50)
