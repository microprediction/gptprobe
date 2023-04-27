from gptprobe.utils.parsedictrobustly import parse_dict_robustly, dict_equal_or_none



def assert_pdr(text,answer:dict):
    d = parse_dict_robustly(text=text)
    assert dict_equal_or_none(d, answer)



def test_pdr_0():
    text = """{"sydney":1234,"adelaide":123}"""
    answer = {'sydney': 1234, 'adelaide': 123}
    assert_pdr(text=text, answer=answer)


# New test case
def test_pdr_6():
    text = """Text before {"key1": 3.5, "key2": 1.7} some irrelevant text {"key3": 9.6} text after."""
    answer = {'key1': 3.5, 'key2': 1.7, 'key3': 9.6}
    assert_pdr(text=text, answer=answer)



