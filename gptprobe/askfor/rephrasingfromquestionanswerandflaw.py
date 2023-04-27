from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.utils.customtypes import DictOrStr


def ask_for_rephrasing_from_question_answer_and_flaw(question: str,
                                                     answer: str,
                                                     flaw=None,
                                                     key_choice=0,
                                                     as_dict=False) -> DictOrStr:
    """
          Ask for a different but complete version of a question

    :param question:       Previously asked question
    :param answer:         An answer that wasn't acceptable
    :param flaw:         (Optional) reason given for why it isn't acceptable
    :param key_choice:
    :param open_kwargs:
    :return:         {"question": "rephrasing question",
                      "success":1}
    """
    if flaw is None:
        from gptprobe.askfor.rephrasingfromquestionandanswer import ask_for_rephrasing_from_question_and_answer
        return ask_for_rephrasing_from_question_and_answer(question=question, answer=answer, key_choice=key_choice,
                                                           as_dict=as_dict)
    meta_question = """ I will provide now in xml-delimited style, a question, a previously given but unsatisfactory answer, 
                        and an exaplanation of a flaw with the answer (why it was not a good or well-formatted answer). 
                        With these three things in mind I would like you think about why the answer was unsatisfactory, and I would ask you 
                    to return a dictionary with one entry whose key is  "rephrasing" and whose value is 
                    a better rephrasing of the original question. This can include extra guidance and/or and 
                    explanation of the reason given for why the previous question had a flaw.  

                    Just return this dictionary and nothing else. Ensure the 
                    key is double quoted. If you can't think of a way to rephrase the question that will make
                    a better answer more likely, then simply make the value the same as the original question. Here is 
                    the question, answer and reason given: 
                       <question>""" + question + """</question>
                       <answer>""" + answer + """</answer>
                       <flaw>""" + flaw + """</flaw>"""

    d = ask_for_dict_from_question(question=meta_question, key_choice=key_choice, numeric_values_only=False)
    d['success'] = 0
    if (d.get('rephrasing') is None) or (len(d.get('rephrasing')) < 0.5 * len(question)):
        d['rephrasing'] = question
    d['success'] = int(d['rephrasing'] != question)
    return d if as_dict else d['rephrasing']


ask_for_rephrasing = ask_for_rephrasing_from_question_answer_and_flaw
