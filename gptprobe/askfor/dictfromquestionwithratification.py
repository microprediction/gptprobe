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
    key_1 = (key_choice + 1) % 3  # Probably silly future-proofing
    key_2 = (key_choice + 2) % 3

    # Ask the question (or prompt if given) and see if the result is successfully parsed
    # After this step we will have a ratification dict {'success': int, 'ratification': str }
    # where the value in ratification is a hint for rephrasing the question

    if prompt is None:
        prompt = question
    answer = ask_for_text_from_question(prompt, key_choice=key_choice)
    first_dict = ask_for_dict_from_poorly_formatted_text(text=answer, key_choice=key_2,
                                                       numeric_values_only=numeric_values_only)

    ratification_dict = ask_for_ratification_from_question_and_answer(question=question,
                                                              answer=answer,
                                                              key_choice=key_1)

    if ratification_dict['success']:
        if first_dict:
            return first_dict
        else:
            from gptprobe.utils.parsedictrobustly import dict_parsing_error
            ratification_dict['ratification'] = 'There was a parsing error: '+dict_parsing_error(answer)

    # We are not ratified, or the ratified result could not be parsed.
    # We split the search tree:
    #     1. Ask the same question again
    #     2. Ask the rephrased question
    #     3. Append a clarification to the original thread

    flaw = ratification_dict.get('ratification')
    rephrasing = ask_for_rephrasing_from_question_answer_and_flaw(question=question, answer=answer, flaw=flaw, as_dict=False )
    clarification = ask_for_clarification_from_question_and_answer(question=question, answer=answer, flaw=flaw, as_dict=False)
    if os.environ.get('GPTPROBE_VERBOSITY'):
        from pprint import pprint
        print('----- INFO: void GPTPROBE_VERBOSITY env to suppress ---- ')
        pprint({'question':question,'answer':answer,'flaw':flaw,'rephrasing':rephrasing,'clarification':clarification})

    # Now try all the possibilities
    # If short_circuit, we return as soon as we have a non-empty dict
    d = first_dict
    from gptprobe.askfor.dictfromquestionanswerandclarification import contextual_question_from_answer_and_clarification
    contextual_clarification = contextual_question_from_answer_and_clarification(question=question, answer=answer, clarification=clarification)
    prompts     = [ contextual_clarification, rephrasing, question ]
    key_choices = [ key_choice, key_1, key_2 ]  # Future proofing for when state comes in
    for prompt, ky in zip(prompts,key_choices):
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
