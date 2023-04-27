from gptprobe.askfor.dictfromquestion import ask_for_dict


def contextual_question_from_answer_and_clarification(question:str, answer:str, clarification:str):
    return """I will provide, in xml-style delimitation, a question, a previous 
                             answer to said question that is inadequate in some way, and a clarification.
                             Please try to answer the question tersely with a Python dictionary. 
                             
                             <question>"""+question+"""</question>
                             <answer>"""+answer+"""</answer>
                             <clarification>"""+clarification+"""</clarification>
                             
                             Respond only with a Python dictionary, with double-quoted keys. 
                             """

def ask_for_dict_from_question_answer_and_clarification(question:str, answer:str, clarification:str,
                                                       key_choice=0, numeric_values_only=False)->dict:
    """
         Ask any question hoping for a dictionary response
         Do so in a way that packages a previous failed attempt

    :param question:
    :param answer:         Previously supplied inadequate answer
    :param clarification:  Further clarification of the question
    :param key_choice:
    :param numeric_values_only:
    :return:
    """
    contextual_question = contextual_question_from_answer_and_clarification(question=question, answer=answer, clarification=clarification)
    return ask_for_dict(contextual_question, key_choice=key_choice, numeric_values_only=numeric_values_only)


if __name__=='__main__':
    from pprint import pprint
    from gptprobe.private_setenv import NOTHING
    question = """Please list ten U.S. presidents and how old they would be if they were all still alive"""
    answer = """ Hawke   89 
                 Menzies 133 """
    clarification = """The answer should take the form of a python dictionary to be easily consumed. 
                       Australians are not welcome on the list. 
                    """
    d = ask_for_dict_from_question_answer_and_clarification(question=question, answer=answer,
                                                            clarification=clarification, numeric_values_only=True)
    pprint(d)
