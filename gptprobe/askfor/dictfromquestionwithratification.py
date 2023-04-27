from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.askfor.dictfrompoorlyformattedtext import ask_for_dict_from_poorly_formatted_text
from gptprobe.askfor.textfromquestion import ask_for_text_from_question
from gptprobe.askfor.rephrasingfromquestionandanswer import ask_for_rephrasing_from_question_and_answer
from gptprobe.askfor.ratificationfromquestionandanswer import ask_for_ratification_from_question_and_answer

# Ask for a dict response that has been independently ratified by another API call


def ask_for_dict_from_question_with_ratification(question: str, key_choice=0, numeric_values_only=False, depth=3)->dict:
    """

         Ask a question
         Seek independent confirmation that the response answers the question
         If this fails, we begin a fanout into modified questions
         Warning: this can be expensive

    :param question:    Any question that asks for a dictionary, or something that might be so interpreted
    :param key_choice:
    :param depth:
    :param open_kwargs:
    :return:
    """
    ratification_key_choice = (key_choice + 1) % 3
    rephrasing_key_choice = (key_choice + 2) % 3
    first_answer = ask_for_text_from_question(question, key_choice=key_choice)
    ratification_dict = ask_for_ratification_from_question_and_answer(question=question,
                                                              answer=first_answer,
                                                              key_choice=ratification_key_choice)
    if (ratification_dict.get('success') == 1) or (depth <= 0):
        d_result = ask_for_dict_from_poorly_formatted_text(text=first_answer, key_choice=rephrasing_key_choice,
                                                           numeric_values_only=numeric_values_only)
        if d_result or (depth <= 0):
            return d_result

    ratification = ratification_dict.get('reason')
    rephrasing = ask_for_rephrasing_from_question_and_answer(question=question, answer=first_answer,
                                                    reason=ratification, key_choice=rephrasing_key_choice,
                                                    as_dict=False)
    d1 = ask_for_dict_from_question_with_ratification(question=rephrasing, depth=depth - 1, key_choice=key_choice)
    d2 = ask_for_dict_from_question_with_ratification(question=question, depth=depth - 1, key_choice=key_choice)
    d1.update(d2)
    return d1





if __name__=='__main__':
    question = """Return a dictionary with double-quoted keys given by trees and numeric values
                  indicating the month of the year when they are most likely to bloom.
               """
    d = ask_for_dict_from_question_with_ratification(question=question)
    print(d)
