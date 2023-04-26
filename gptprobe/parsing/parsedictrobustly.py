import re
import json


def parse_dict_robustly(text):
    # Search for dictionary-like substrings within the input text
    dict_pattern = r"[{\[].*?[}\]]"
    dict_matches = re.findall(dict_pattern, text)

    if not dict_matches:
        return None

    kv_dict = {}

    for dict_string in dict_matches:
        # Extract substrings that could be key-value pairs
        kv_pattern = r'("[^"]+"\s*:\s*-?\d+(\.\d+)?([eE][-+]?\d+)?)'
        kv_matches = re.findall(kv_pattern, dict_string)

        if not kv_matches:
            continue

        for match in kv_matches:
            # Wrap the key-value pair in curly braces to form a valid JSON string
            kv_json_string = '{' + match[0] + '}'

            try:
                kv_pair = json.loads(kv_json_string)
                kv_dict.update(kv_pair)
            except json.JSONDecodeError:
                continue

    return kv_dict if kv_dict else None




import re
import json


def parse_dict_robustly_singular(text):
    # Search for a dictionary-like substring within the input text
    dict_pattern = r"[{\[].*?[}\]]"
    dict_match = re.search(dict_pattern, text)

    if not dict_match:
        return None

    dict_string = dict_match.group(0)

    # Extract substrings that could be key-value pairs
    kv_pattern = r'("[^"]+"\s*:\s*-?\d+(\.\d+)?([eE][-+]?\d+)?)'
    kv_matches = re.findall(kv_pattern, dict_string)

    if not kv_matches:
        return None

    kv_dict = {}
    for match in kv_matches:
        # Wrap the key-value pair in curly braces to form a valid JSON string
        if len(match):
            kv_json_string = '{' + match[0] + '}'

            try:
                kv_pair = json.loads(kv_json_string)
                kv_dict.update(kv_pair)
            except json.JSONDecodeError:
                continue

    return kv_dict if kv_dict else None



def dict_equal_or_none(dict1, dict2):
    # Check if both dictionaries have the same keys, or both are none

    if not dict1:
        return not dict2

    if not dict2:
        return not dict1

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Compare the values for each key
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False

    return True


if __name__=='__main__':
    text = 'Some unstructured text {"key1": 1.23, "key2": 45.6}, more text {"key3": 7.89} and so on.'
    result = parse_dict_robustly(text)
    print(result)
