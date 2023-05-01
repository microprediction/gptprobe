from gptprobe.askfor.textfromquestion import ask_for_text_from_question
from gptprobe.utils.customtypes import DictOrStr


def ask_for_text_from_poorly_formatted_dict_text(text:str, key_choice=0, numeric_values_only=False, as_dict=False)->DictOrStr:
    """
          Request text formatted so it can be consumed as a dict

    :param text:               Unstructured text you hope implies a dictionary with numeric values
    :param key_choice:             References an environment variable like  OPEN_AI_KEY_0
    :param numeric_values_only:    If True, non-numeric key/value pairs will be ignored.
    :return:
    """
    question = """I am going to give you unstructured text delineated in xml-style as <text>...</text> and I would like you to return
        a dictionary, if it is at all possible to interpret the text that way, otherwise return an empty dictionary like '{}'. 
        If there appear to be extraneous lines in the response, just ignore them. 
        Do not respond with any other text. Ensure keys are double quoted.
        Here is the unstructured text <text>""" + text + """</text>"""
    if numeric_values_only:
        question += """ Please make sure all dict values are numeric. 
                    """
    response_text = ask_for_text_from_question(question, key_choice=key_choice)
    return {'success':1,'text':response_text} if as_dict else response_text


ask_for_dict_text = ask_for_text_from_poorly_formatted_dict_text


if __name__=='__main__':
    from gptprobe.askfor.dictfrompoorlyformattedtext import ask_for_dict_from_poorly_formatted_text

    messy_dict_text = """ Final score are 
                              Australia  1 
                              Brazil     2
                                bummer """
    clean_dict_text = ask_for_dict_text(messy_dict_text)
    print(clean_dict_text)



