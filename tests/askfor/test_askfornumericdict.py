
from gptprobe.keysinenviron import keys_in_environ # Poor man's fixture

if keys_in_environ():
    print('Good to go')
    from gptprobe.askfor.textfrompoorlyformatteddicttext import ask_for_text_from_poorly_formatted_dict_text
    from gptprobe.utils.parsedictrobustly import dict_equal_or_none, parse_dict_robustly

    def test_ask_0():
        text = """ '{"sydney":1234,"adelaide":123}' """
        answer = {'sydney':1234,'adelaide':123}
        response = ask_for_text_from_poorly_formatted_dict_text(text=text)
        d = parse_dict_robustly(text=response)
        assert dict_equal_or_none(d, answer)



if __name__=='__main__':
    test_ask_0()