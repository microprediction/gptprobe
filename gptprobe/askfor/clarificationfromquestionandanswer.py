from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.askfor.flawfromquestionandanswer import ask_for_flaw_from_question_and_answer
from gptprobe.utils.customtypes import DictOrStr


def ask_for_clarification_from_question_and_answer(question: str, answer: str, reason=None, key_choice=0,
                                                   min_clarification_len=15, as_dict=False) -> DictOrStr:
    """
          Ask for a suggested follow-up prompt to encourage a better answer to a previous question

    :param question:       Previously asked question
    :param answer:         An answer that wasn't acceptable
    :param reason:         (Optional) reason given for why it isn't acceptable
    :param key_choice:
    :param open_kwargs:
    :return:         {"clarification": "The question asked for lowercase and you provided uppercase",
                      "success":1}
    """
    DEFAULT_CLARIFICATION = 'Please try again to answer the previous question precisely as asked, taking ' \
                            'into account formatting instructions, if any'
    if reason is None:
        d = ask_for_flaw_from_question_and_answer(question=question, answer=answer)
        if d.get('success') != 1:
            # If we don't know what's wrong, might be best to keep the followup simple
            return {'success' :0 ,'clarification' :DEFAULT_CLARIFICATION}
        reason = d['reason']

    meta_question = """ I will provide now in xml-delimited style, a question, a previously given but unsatisfactory answer, 
                        and a reason why it was not a good or well-formatted answer. 

                        Return a dictionary where the single double-quoted key is "clarification" and the value is 
                    a short clarification or the reason. The clarification should not repeat the question. The clarification
                    should include the reason, albeit paraphrased as you see fit. 

                    Just return this dictionary and nothing else. Ensure the 
                    key is double quoted. Here is the question, answer and reason why it was not satisfactory:
                       <question>""" + question + """</question>
                       <answer>""" + answer + """</answer>
                       <reason>""" + reason + """</reason>
                    Let me emphasize that you should reply with a dict only and no other text"""
    d = ask_for_dict_from_question(question=meta_question, key_choice=key_choice, numeric_values_only=False)
    d['success'] = 0
    if (d.get('clarification') is None) or (len(d.get('clarification')) < min_clarification_len):
        d['clarification'] = DEFAULT_CLARIFICATION
    d['success'] = int(d['clarification'] != DEFAULT_CLARIFICATION)
    return d if as_dict else d['clarification']


ask_for_clarification = ask_for_clarification_from_question_and_answer

if __name__=='__main__':
    from gptprobe.askfor.rephrasingfromquestionandanswer import ask_for_rephrasing_from_question_and_answer
    question = """ Please provide a dictionary where keys are town names and values are prime numbers 
              """
    answer = """ The dictionary is {'Dog':12312,'sydney':17} """

    d1 = ask_for_flaw_from_question_and_answer(question=question, answer=answer, as_dict=True)
    print(d1)

    d2 = ask_for_rephrasing_from_question_and_answer(question=question, answer=answer, reason=d1['reason'])
    print(d2)

    d3 = ask_for_rephrasing_from_question_and_answer(question=question, answer=answer, reason=None)
    print(d3)

    d4 = ask_for_clarification_from_question_and_answer(question=question, answer=answer, reason=d1['reason'])
    print(d4)

    d5 = ask_for_clarification_from_question_and_answer(question=question, answer=answer, reason=None)
    print(d5)

    # Does it help?