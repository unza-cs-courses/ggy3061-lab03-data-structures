"""
Lab 3 Task 1: List Operations
Demonstrates list creation, indexing, slicing, and methods with geological sample data.

Your Name: [YOUR NAME]
Student ID: [YOUR ID]
"""


def create_depth_list(count):
    """
    Create a list of sample depths.

    Args:
        count: Number of depth values to create

    Returns:
        A list of integer depth values
    """
    # TODO: Create a list with 'count' depth values
    # Each depth should be an integer between 100 and 500
    # Example: [150, 275, 320, 180, 420, ...]
    pass


def create_rock_type_list():
    """
    Create a list of rock types.

    Returns:
        A list of rock type strings from your assigned types
    """
    # TODO: Return a list of your assigned rock types
    # Check README.md for your specific rock types
    pass


def demonstrate_indexing(depths):
    """
    Demonstrate list indexing operations.

    Args:
        depths: A list of depth values

    Returns:
        A dictionary with indexed values
    """
    # TODO: Return a dictionary with:
    # - 'first': first element (index 0)
    # - 'last': last element (negative indexing)
    # - 'second': second element
    # - 'second_to_last': second to last element
    pass


def demonstrate_slicing(depths):
    """
    Demonstrate list slicing operations.

    Args:
        depths: A list of depth values

    Returns:
        A dictionary with sliced lists
    """
    # TODO: Return a dictionary with:
    # - 'first_three': first 3 elements
    # - 'last_three': last 3 elements
    # - 'middle': elements from index 2 to 5 (exclusive)
    # - 'every_second': every second element
    # - 'reversed': list in reverse order
    pass


def demonstrate_list_methods(depths, rock_types):
    """
    Demonstrate various list methods.

    Args:
        depths: A list of depth values
        rock_types: A list of rock types

    Returns:
        A dictionary with results of various list operations
    """
    # TODO: Perform the following operations and return results:
    # 1. Append a new depth (550) to a copy of depths
    # 2. Extend rock_types copy with ['Marble', 'Slate']
    # 3. Sort a copy of depths (ascending)
    # 4. Sort a copy of depths (descending)
    # 5. Find the index of the maximum depth
    # 6. Count occurrences of a specific rock type
    # 7. Reverse a copy of depths

    # Return a dictionary with keys:
    # 'appended', 'extended', 'sorted_asc', 'sorted_desc',
    # 'max_index', 'rock_count', 'reversed'
    pass


def calculate_depth_statistics(depths):
    """
    Calculate basic statistics from a list of depths.

    Args:
        depths: A list of depth values

    Returns:
        A dictionary with statistics
    """
    # TODO: Calculate and return:
    # - 'count': number of depths
    # - 'sum': sum of all depths
    # - 'min': minimum depth
    # - 'max': maximum depth
    # - 'average': average depth (sum / count)
    pass


# Main execution
if __name__ == "__main__":
    # Create lists using your assigned values
    # Check README.md for your sample_count and rock_types
    sample_count = 10  # TODO: Replace with your assigned count

    print("=" * 50)
    print("Lab 3 Task 1: List Operations")
    print("=" * 50)

    # Create depth list
    print("\n1. Creating Depth List")
    print("-" * 30)
    depths = create_depth_list(sample_count)
    if depths:
        print(f"Depths: {depths}")
        print(f"Number of depths: {len(depths)}")

    # Create rock type list
    print("\n2. Creating Rock Type List")
    print("-" * 30)
    rock_types = create_rock_type_list()
    if rock_types:
        print(f"Rock Types: {rock_types}")

    # Demonstrate indexing
    print("\n3. List Indexing")
    print("-" * 30)
    if depths:
        indexed = demonstrate_indexing(depths)
        if indexed:
            print(f"First depth: {indexed.get('first')}")
            print(f"Last depth: {indexed.get('last')}")
            print(f"Second depth: {indexed.get('second')}")
            print(f"Second to last: {indexed.get('second_to_last')}")

    # Demonstrate slicing
    print("\n4. List Slicing")
    print("-" * 30)
    if depths:
        sliced = demonstrate_slicing(depths)
        if sliced:
            print(f"First three: {sliced.get('first_three')}")
            print(f"Last three: {sliced.get('last_three')}")
            print(f"Middle (2:5): {sliced.get('middle')}")
            print(f"Every second: {sliced.get('every_second')}")
            print(f"Reversed: {sliced.get('reversed')}")

    # Demonstrate methods
    print("\n5. List Methods")
    print("-" * 30)
    if depths and rock_types:
        methods = demonstrate_list_methods(depths, rock_types)
        if methods:
            print(f"After append(550): {methods.get('appended')}")
            print(f"After extend: {methods.get('extended')}")
            print(f"Sorted (asc): {methods.get('sorted_asc')}")
            print(f"Sorted (desc): {methods.get('sorted_desc')}")
            print(f"Index of max: {methods.get('max_index')}")

    # Calculate statistics
    print("\n6. Depth Statistics")
    print("-" * 30)
    if depths:
        stats = calculate_depth_statistics(depths)
        if stats:
            print(f"Count: {stats.get('count')}")
            print(f"Sum: {stats.get('sum')}")
            print(f"Min: {stats.get('min')}")
            print(f"Max: {stats.get('max')}")
            print(f"Average: {stats.get('average'):.2f}" if stats.get('average') else "")

    print("\n" + "=" * 50)
    print("End of Task 1")
    print("=" * 50)
