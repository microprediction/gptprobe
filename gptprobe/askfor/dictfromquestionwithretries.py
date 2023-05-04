from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.askfor.dictfrompoorlyformattedtext import ask_for_dict_from_poorly_formatted_text
from gptprobe.askfor.textfromquestion import ask_for_text_from_question
from gptprobe.askfor.ratificationfromquestionandanswer import ask_for_ratification_from_question_and_answer
from gptprobe.askfor.flawfromquestionandanswer import ask_for_flaw_from_question_and_answer
from gptprobe.askfor.rephrasingfromquestionanswerandflaw import ask_for_rephrasing_from_question_answer_and_flaw
from gptprobe.askfor.clarificationfromquestionandanswer import ask_for_clarification_from_question_and_answer
import os
from gptprobe.utils.parsedictrobustly import dict_parsing_error
from gptprobe.askfor.dictfromquestionanswerandclarification import contextual_question_from_answer_and_clarification


# Ask for a dict response that has been independently ratified by another API call


def ask_for_dict_from_question_with_retries(question: str,
                                            key_choice=0,
                                            numeric_values_only=False,
                                            retries=3)->dict:
    """
           Persistently ask for a dict, following up with parsing error information

    :param question:    Any question that asks for a dictionary, or something that might be so interpreted
    :param key_choice:
    :param depth:
    :param open_kwargs:
    :return:
    """

    prompt = question
    rotated_key = key_choice

    for attempt in range(retries):
        rotated_key = ( rotated_key + 1 ) % 3
        answer = ask_for_text_from_question(question=prompt, key_choice=key_choice)
        answer_dict = ask_for_dict_from_poorly_formatted_text(text=answer, key_choice=rotated_key,
                                                       numeric_values_only=numeric_values_only)
        if isinstance(answer_dict,dict) and answer_dict:
            return answer_dict

        parsing_error = 'The answer given could not be parsed as a Python dict. The error was '+ dict_parsing_error(answer)
        prompt = contextual_question_from_answer_and_clarification(question=question, answer=answer, clarification=parsing_error)

    return {}


if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    question = """Return a dictionary with double-quoted keys given by trees and numeric values
                  indicating the month of the year when they are most likely to bloom.
               """
    import os
    os.environ['GPTPROBE_VERBOSITY']="1"
    d = ask_for_dict_from_question_with_retries(question=question)
    print(d)
