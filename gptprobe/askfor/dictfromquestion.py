from gptprobe.askfor.textfromquestion import ask_for_text_from_question
from gptprobe.askfor.textfrompoorlyformatteddicttext import ask_for_text_from_poorly_formatted_dict_text

# The workhorse function ask_for_dict is used by most other functions. It will:
#
#     0. Pose the question
#     1. Try to immediately parse the response
#     2. If needed, ask GPT for pre-parsing help on a separate thread


def ask_for_dict_from_question(question:str, key_choice=0, numeric_values_only=False)->dict:
    """
         Ask any question hoping for a dictionary response
         If it cannot be parsed, ask for help reformatting and try again

    :param question:
    :param key_choice:
    :param numeric_values_only:
    :param open_kwargs:
    :return:
    """
    from gptprobe.askfor.dictfrompoorlyformattedtext import ask_for_dict_from_poorly_formatted_text
    response = ask_for_text_from_question(question, key_choice=key_choice)
    rotated_key_choice = (key_choice + 1) % 3
    return ask_for_dict_from_poorly_formatted_text(text=response, numeric_values_only=numeric_values_only, key_choice=rotated_key_choice)


ask_for_dict = ask_for_dict_from_question



if __name__=='__main__':
    from pprint import pprint

    text = """ dog | 1563,  sydney | 1
               cow | 1765"""
    d3_txt = ask_for_text_from_poorly_formatted_dict_text(text=text)
    d2_txt = ask_for_text_from_poorly_formatted_dict_text(text=text, numeric_values_only=True)
    pprint({'d3':d3_txt,
            'd2':d2_txt})
    from gptprobe.utils.parsedictrobustly import dict_equal_or_none, parse_dict_robustly
    d3 = parse_dict_robustly(d3_txt)
    d2 = parse_dict_robustly(d2_txt)
    if not dict_equal_or_none(d2, d3):
        print('They are not the same')
