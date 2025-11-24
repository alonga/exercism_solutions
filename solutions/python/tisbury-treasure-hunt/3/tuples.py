"""Functions to help Azara and Rui locate pirate treasure."""







def get_coordinate(record):
    
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
   
    
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    if tuple(azara_record[1]) == rui_record[1]:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
   
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if tuple(azara_record[1]) == rui_record[1]:
        return (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[-1])
    else:
        
        return "not a match"


def clean_up(combined_record_group):
    cleaned = []
    for record in combined_record_group:
        # remove duplicate full records
        if record not in cleaned:
            # remove unwanted coordinate strings like "4B"
            new_record = tuple(
                item for item in record
                if not (isinstance(item, str) and len(item) == 2 and item[0].isdigit() and item[1].isalpha())
            )
            cleaned.append(new_record)
    # Add final newline for the miserable test
    return "\n".join(str(r) for r in cleaned) + "\n"


