
from gptprobe.goodtogo import good_to_go # Poor man's fixture

if good_to_go():
    from gptprobe.parsing.parsedictrobustly import parse_dict_robustly

    def assert_pdr(text,answer):
        d = parse_dict_robustly(text=text)


    def test_pdr_0():
        text = """ '{"sydney":1234,"adelaide":123}' """
        answer = {'sydney':1234,'adelaide':123}
        assert_pdr(text=text,answer=answer)

