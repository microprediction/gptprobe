
from gptprobe.goodtogo import good_to_go # Poor man's fixture

if good_to_go():
    print('Good to go')
    from gptprobe.parsing.askfornumericdict import ask_for_numeric_dict
    from gptprobe.parsing.parsedictrobustly import dict_equal_or_none, parse_dict_robustly

    def test_ask_0():
        text = """ '{"sydney":1234,"adelaide":123}' """
        answer = {'sydney':1234,'adelaide':123}
        response = ask_for_numeric_dict(text=text)
        d = parse_dict_robustly(text=response)
        assert dict_equal_or_none(d, answer)


