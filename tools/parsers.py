import math

# Functions needed for processing data
def remove_empty_string_values(data):
    """Remove empty string values from dictionaries before saving to database"""
    for key in list(data.keys()):  # Create a copy of keys to avoid modifying while iterating
        if data[key] == "":
            del data[key]


def remove_nan_values(data):
    """Remove empty values from dictionaries before saving to database"""
    for key in list(data.keys()): # Create a copy of keys to avoid modifying while iterating
        if not isinstance(data[key], str) and math.isnan(data[key]):
            del data[key]