from gptprobe.openaiwrappers.openapi import ask_using_environ


def ask_for_numeric_dict(text:str, key_choice=0):
    """ Try to turn any text into a dictionary
    :param text:         Unstructured text you hope implies a dictionary with numeric values
    :param key_choice:   References an env variable like  OPEN_AI_KEY_0
    :return:
    """
    question = """I am going to give you unstructured text delineated in xml-style as <text>...</text> and I would like you to return
     a dictionary with numeric keys, if it is at all possible to interpret the text that way, otherwise return an empty dictionary like '{}'. 
     If there appear to be extraneous lines in the response, just ignore them. 
     Do not respond with any other text. Here is the unstructured text <text>{text}</text>
              """
    response = ask_using_environ(question)
    return response


if __name__=='__main__':
    import json
    from gptprobe.private_setenv import
    text = """ dog 1563,  sydney 17
               extranous garbage--
               
               cow 1765"""
    d_txt = ask_for_numeric_dict(text=text)
    print(d_txt)