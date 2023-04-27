from gptprobe.utils.parsedictrobustly import parse_dict_robustly
from gptprobe.utils.customtypes import DictOrStr
from gptprobe.askfor.textfrompoorlyformatteddicttext import ask_for_text_from_poorly_formatted_dict_text


def ask_for_dict_from_poorly_formatted_text(text, numeric_values_only=False, key_choice=0)->DictOrStr:
    """
          Ask GPT to pre-parse some text that (vaguely) represents a dictionary

    :param text:
    :param numeric_values_only:
    :param key_choice:
    :param open_kwargs:
    :return:
    """
    try:
        return parse_dict_robustly(text, numeric_values_only=numeric_values_only)
    except Exception as e:
        reformatted_response = ask_for_text_from_poorly_formatted_dict_text(text=text, key_choice=key_choice)
        try:
            return parse_dict_robustly(reformatted_response, numeric_values_only=numeric_values_only)
        except Exception as e:
            return {}


ask_for_dict_from_text = ask_for_dict_from_poorly_formatted_text