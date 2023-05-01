

# Example dictionary with mixed-case keys, string values, and numeric values
example_dict = {
    "HeLLo": "WorlD",
    "KEY1": "Value1",
    123: "ValuE2",
    "KeY2": 456,
}


def lowercase_dict(d):
    """
    Create a new dictionary with lowercase keys and values (if they are strings).

    :param d: The input dictionary.
    :return: A new dictionary with lowercase keys and values (if they are strings).
    """
    new_dict = {}
    for key, value in d.items():
        new_key = key.lower() if isinstance(key, str) else key
        new_value = value.lower() if isinstance(value, str) else value
        new_dict[new_key] = new_value
    return new_dict


def dict_equal_or_none(dict1, dict2, case_insensitive=False):
    # Check if both dictionaries have the same keys, or both are none

    if not dict1:
        return not dict2

    if not dict2:
        return not dict1

    if case_insensitive:
        d1 = lowercase_dict(dict1)
        d2 = lowercase_dict(dict2)
        return dict_equal_or_none(d1,d2, case_insensitive=False)

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Compare the values for each key
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False

    return True


if __name__=='__main__':
    # Example dictionary with mixed-case keys and values
    example_dict = {
        "HeLLo": "WorlD",
        "KEY1": "Value1",
        "KeY2": "ValuE2",
        1:"Banana",
        "pijamas":0
    }
    print(lowercase_dict(example_dict))

