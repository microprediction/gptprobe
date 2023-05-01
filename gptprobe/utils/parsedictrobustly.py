import re
import json
from gptprobe.utils.equivalence import dict_equal_or_none

def dict_parsing_error(text):
    try:
        d = json.loads(text)
        return ' ... or maybe not'
    except Exception as e:
        return str(e)


def switch_quotes(s: str) -> str:
    # Use a temporary placeholder that is unlikely to appear in the original string
    placeholder = '\uFFFF'
    # Replace double quotes with placeholder
    s = s.replace('"', placeholder)
    # Replace single quotes with double quotes
    s = s.replace('\'', '"')
    # Replace placeholder with single quotes
    s = s.replace(placeholder, '\'')
    return s


def parse_dict_robustly(text, numeric_values_only=False):
    """
    :param text:
    :param numeric_values_only:  If True,
    :return:
    """
    try:
        d = json.loads(text)
        return d
    except:
        pass
    text = text.replace("\n", " ")
    d1 = parse_dict_disjoint(text, numeric_values_only=numeric_values_only) or {}
    d2 = parse_dict_disjoint(switch_quotes(text), numeric_values_only=numeric_values_only) or {}
    d1.update(d2)
    if numeric_values_only:
        d = dict()
        for k,v in d1.items():
            try:
                val = float(v)
                d.update({k,val})
            except TypeError:
                pass
        return d
    return d1


def parse_dict_disjoint(text, numeric_values_only=False):
    """ Tries to parse a dictionary interspersed with extraneous text
    :param text:
    :param numeric_only:
    :return:
    """


    # Search for dictionary-like substrings within the input text
    dict_pattern = r"[{\[].*?[}\]]"
    dict_matches = re.findall(dict_pattern, text)

    if not dict_matches:
        return {}

    kv_dict = {}

    for dict_string in dict_matches:

        # Extract substrings that could be key-value pairs
        kv_pattern_numeric = r'("[^"]+"\s*:\s*-?\d+(\.\d+)?([eE][-+]?\d+)?)'
        kv_pattern_general = r'("[^"]+"\s*:\s*(("[^"]*")|(-?\d+(\.\d+)?([eE][-+]?\d+)?)))'
        kv_pattern = kv_pattern_numeric if numeric_values_only else kv_pattern_general
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





if __name__=='__main__':
    text = 'Some unstructured text {"key1": 1.23, "key2": 45.6}, more text {"key3": 7.89} and so on.'
    result = parse_dict_robustly(text)
    print(result)
