from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question


def ask_for_ratification_from_question_and_answer(question:str, answer:str,
                                                  key_choice:int)->dict:
    """ Ask ChatGPT if a previous response answers a question

    Returns one of the following possibilities:

             {'success':1,'ratification':'Answer met all the requirements of the question'}
             {'success':0,'ratification':'That is not something Plato would say'}

    """
    ratification_question = """I will provide you a question and an answer delineated xml-style. The answer may be 
                               quite terse - such as a string representation of a dictionary. 
    
                                I would like you to respond with a dictionary with a key "success" (double quotes) and 
                                a numeric value. The value should be 0 only if you can determine that the format
                                of the answer does not meet the specifications of the question, and thus you can 
                                determine that the question was definitely answered improperly.
                                  
                                 Otherwise make this value 1. If you are not sure whether the answer could possibly
                                  be interpreted as an approximate answer to the question, even an imperfect answer, 
                                   make the value 1. 
                                   
                                  Do not make the success value 0 just because the answer might have been better. Do not make the success value 0 just because the 
                                  answer could have included more details or rationale. Only make it 0 if it clearly violates a 
                                  stated requirement in the question. For example if the question asks for a dictionary
                                  with five keys and only three are returned, the success value should be 0. 
                                  
                                  But - and this is important - do not make the success value 0 just because 
                                  the answer does not include a full explanation. Do not make the success value 0 just because
                                  the answer might have been more complete, or better in some way. 
                                  
                                  If you are not sure, err on the side of making the success value 1, not 0. 
                                
                                Also return a key "ratification" with value equal to a text explanation of your 
                                decision. Here is the question and
                                          answer pair <question>""" + question + """</question>
                                                      <answer>""" + answer + """</answer>. 
                                        Remember to respond only with a dictionary and no other text. """
    ratification_dict = ask_for_dict_from_question(question=ratification_question,
                                              key_choice=key_choice, numeric_values_only=False)
    DEFAULT_FAILURE_RATIFICATION = 'response did not answer the question'
    if not ratification_dict:
        ratification_dict = {'success':1,'ratification':'only formatting might prevent this being a good answer'}

    if (ratification_dict.get('success') != 1) and not ratification_dict.get('ratification'):
        ratification_dict = {'success':0,'ratification':DEFAULT_FAILURE_RATIFICATION}
    else:
        ratification_dict['success'] = int(ratification_dict['success'])

    # Override
    invalid_rejections = ['include a reason','information']
    if any([ inv_rej in ratification_dict['ratification'] for inv_rej in invalid_rejections ]):
        ratification_dict['success'] = 1
        ratification_dict['ratification'] += ' ... but this was overridden  '

    return ratification_dict


ask_for_ratification = ask_for_ratification_from_question_and_answer