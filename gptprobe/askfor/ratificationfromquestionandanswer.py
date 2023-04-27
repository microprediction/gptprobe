from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question


def ask_for_ratification_from_question_and_answer(question:str, answer:str,
                                                  key_choice:int)->dict:
    """ Ask ChatGPT if a previous response answers a question

    Returns one of the following possibilities:

             {'success':1,'ratification':'Answer met all the requirements of the question'}
             {'success':0,'ratification':'That is not something Plato would say'}

    """
    ratification_question = """I will provide you a question and a solution delineated xml-style. I would
                                like you to respond with a dictionary with a key "success" (double quotes) and 
                                         a value equal to 1 if you think the question was answered well, otherwise 0. 
                                          Also return a key "ratification" with value equal to a text explanation of why
                                          the response does not seem to answer the question, or why it does. Here is the question and
                                          answer pair <question>""" + question + """</question>
                                                      <answer>""" + answer + """</answer>. 
                                        Remember to respond only with a dictionary and no other text. """
    ratification_dict = ask_for_dict_from_question(question=ratification_question,
                                              key_choice=key_choice, numeric_values_only=False)
    DEFAULT_FAILURE_RATIFICATION = 'response did not answer the question'
    if (not ratification_dict) or ((ratification_dict.get('success') != 1) and not ratification_dict.get('ratification')):
        ratification_dict = {'success':0,'ratification':DEFAULT_FAILURE_RATIFICATION}
    else:
        ratification_dict['success'] = int(ratification_dict['success'])
    return ratification_dict


ask_for_ratification = ask_for_ratification_from_question_and_answer