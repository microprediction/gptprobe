from gptprobe.openaiwrappers.openapi import ask_using_environ


def ask_for_numeric_dict(text:str, key_choice=0, **open_kwargs):
    """ Try to turn any text into a dictionary
    :param text:         Unstructured text you hope implies a dictionary with numeric values
    :param key_choice:   References an env variable like  OPEN_AI_KEY_0
    :return:
    """
    question = """I am going to give you unstructured text delineated in xml-style as <text>...</text> and I would like you to return
     a dictionary with numeric keys, if it is at all possible to interpret the text that way, otherwise return an empty dictionary like '{}'. 
     If there appear to be extraneous lines in the response, just ignore them. 
     Do not respond with any other text. Here is the unstructured text <text>"""+text+"""</text>"""
    response = ask_using_environ(question, key_choice=key_choice, **open_kwargs)
    return response


if __name__=='__main__':
    import json
    from gptprobe.private_setenv import NOTHING
    from pprint import pprint

    text = """ dog: 1563,  sydney: 1
               cow: 1765"""
    d3_txt = ask_for_numeric_dict(text=text,engine='text-davinci-003', temperature=0.2)
    d2_txt = ask_for_numeric_dict(text=text, engine='text-davinci-003')
    pprint({'d3':d3_txt,
            'd2':d2_txt})
    from gptprobe.parsing.parsedictrobustly import dict_equal_or_none, parse_dict_robustly
    d3 = parse_dict_robustly(d3_txt)
    d2 = parse_dict_robustly(d2_txt)
    dict_equal_or_none(d2, d3)
