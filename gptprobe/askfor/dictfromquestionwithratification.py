from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.askfor.dictfrompoorlyformattedtext import ask_for_dict_from_poorly_formatted_text
from gptprobe.askfor.textfromquestion import ask_for_text_from_question
from gptprobe.askfor.ratificationfromquestionandanswer import ask_for_ratification_from_question_and_answer
from gptprobe.askfor.flawfromquestionandanswer import ask_for_flaw_from_question_and_answer
from gptprobe.askfor.rephrasingfromquestionanswerandflaw import ask_for_rephrasing_from_question_answer_and_flaw
from gptprobe.askfor.clarificationfromquestionandanswer import ask_for_clarification_from_question_and_answer
import os

# Ask for a dict response that has been independently ratified by another API call


def ask_for_dict_from_question_with_ratification(question: str, prompt=None, key_choice=0, numeric_values_only=False,
                                                 depth=2, short_ciruit=True)->dict:
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
    key_1 = (key_choice + 1) % 3
    key_2 = (key_choice + 2) % 3

    # Ask the question (or prompt if given) and see if the result is successfully parsed
    # After this step we will have a ratification dict {'success': int, 'ratification': str }
    # where the value in ratification is a hint for rephrasing the question

    if prompt is None:
        prompt = question
    first_answer = ask_for_text_from_question(prompt, key_choice=key_choice)
    first_dict = ask_for_dict_from_poorly_formatted_text(text=first_answer, key_choice=key_2,
                                                       numeric_values_only=numeric_values_only)
    if first_dict:
        ratification_dict = ask_for_ratification_from_question_and_answer(question=question,
                                                              answer=first_answer,
                                                              key_choice=key_1)
    else:
        ratification_dict = {'success':0}
        flaw = ask_for_flaw_from_question_and_answer(question=question, answer=first_answer, key_choice=key_2, as_dict=False)
        ratification_dict['ratification'] = flaw

    if ratification_dict['success']:
        return first_dict

    # We are not ratified, or the ratified result could not be parsed.
    #
    # We split the search tree;z
    #     1. Ask the same question again
    #     2. Ask the rephrased question
    #     3. Supply a clarification on the original thread

    flaw = ratification_dict['ratification']
    rephrasing = ask_for_rephrasing_from_question_answer_and_flaw(question=question, answer=first_answer, flaw=flaw, as_dict=False )
    clarification = ask_for_clarification_from_question_and_answer(question=question, answer=first_answer, flaw=flaw, as_dict=False)
    if os.environ.get('GPTPROBE_VERBOSITY'):
        from pprint import pprint
        pprint({'question':question,'answer':first_answer,'flaw':flaw,'rephrasing':rephrasing,'clarification':clarification})

    # Now try all the possibilities
    # If short_circuit, we return as soon as we have a non-empty dict
    d = first_dict
    questions = [ clarification, rephrasing, question ]
    key_choices = [ key_choice, key_1, key_2 ]
    for prompt, ky in zip(questions,key_choices):
        d_ = ask_for_dict_from_question_with_ratification(question=question, key_choice=ky,
                                                          numeric_values_only=numeric_values_only,
                                                          depth=depth-1, prompt=prompt)
        if d_:
            d.update(d_)
            if short_ciruit:
                return d
    return d



if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    question = """Return a dictionary with double-quoted keys given by trees and numeric values
                  indicating the month of the year when they are most likely to bloom.
               """
    import os
    os.environ['GPTPROBE_VERBOSITY']="1"
    d = ask_for_dict_from_question_with_ratification(question=question)
    print(d)
