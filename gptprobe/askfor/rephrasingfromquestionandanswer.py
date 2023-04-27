from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.utils.customtypes import DictOrStr


def ask_why_answer_is_wrong(question:str, answer:str,  key_choice=0)->DictOrStr:
    """
             Ask for an explanation of why an answer to a question is not satisfactory

       :param question:       Previously asked question
       :param answer:         An answer that wasn't acceptable
       :return:         {"reason": "a dog is not a town",
                         "success":1}
    """
    meta_question = """ I will provide now in xml-delimited style, a question, and a previously given but unsatisfactory answer, 
                        Please return a dictionary where the double quoted key is "reason" and the value is
                        an explanation of why the answer might not be considered satisfactory. Pay special attention
                        to any formatting instructions that were given in the question and not followed to the letter
                        in the answer. Here, in xml-style delimitation, are the question and answer:
                         <question>"""+question+"""</question>
                         <answer>"""+answer+"""</answer>"""
    d = ask_for_dict_from_question(question=meta_question, key_choice=key_choice, numeric_values_only=False)
    d['success'] = 0
    DEFAULT_REASON = 'no reason'
    if (d.get('reason') is None) or (len(d.get('reason')) < 0.5 * len(question)):
        d['reason'] = DEFAULT_REASON
    d['success'] = int(d['reason'] != DEFAULT_REASON)
    return d


def ask_for_rephrasing_from_question_and_answer(question:str, 
                                                answer:str, 
                                                reason=None, 
                                                key_choice=0,
                                                as_dict=False)->DictOrStr:
    """
          Ask for a different but complete version of a question

    :param question:       Previously asked question
    :param answer:         An answer that wasn't acceptable
    :param reason:         (Optional) reason given for why it isn't acceptable
    :param key_choice:
    :param open_kwargs:
    :return:         {"question": "rephrasing question",
                      "success":1}
    """
    if reason:
        meta_question = """ I will provide now in xml-delimited style, a question, a previously given but unsatisfactory answer, 
                        and a reason why it was not a good or well-formatted answer. With these three things
                    in mind I would like you think about why the answer was unsatisfactory, and I would ask you 
                    to return a dictionary with one entry whose key is  "rephrasing" and whose value is 
                    a better rephrasing of the original question. This can include extra guidance and/or and 
                    explanation of the reason given for why the previous question was not acceptable. 
                     
                    Just return this dictionary and nothing else. Ensure the 
                    key is double quoted. If you can't think of a way to rephrase the question that will make
                    a better answer more likely, then simply make the value the same as the original question. Here is 
                    the question, answer and reason given: 
                       <question>"""+question+"""</question>
                       <answer>"""+answer+"""</answer>
                       <reason>"""+reason+"""</reason>"""
    else:
        meta_question = """ I will provide now in xml-delimited style, a question, and an unsatisfactory answer previously
        provided by an LLM. Please consider why the LLM might have answered in an unsatisfactory way, and 
        design a new rephrasing question that might be more clear. If there is formatting
        instruction in the question, that should be included in the new question also. If the format was wrong,
        instruction to fix it should be included in the rephrasing question along with a reason why the previous answer
        was not good enough. 
        
        Please return a dictionary with one entry whose key is  "rephrasing" and whose value is the new rephrasing question. 
        Just return this dictionary and nothing else. Ensure the dict key is double quoted. 
        Here is the original question and answer delimited in the style of XML 
                              <question>""" + question + """</question>
                              <answer>""" + answer + """</answer>"""

    d = ask_for_dict_from_question(question=meta_question, key_choice=key_choice, numeric_values_only=False)
    d['success'] = 0
    if (d.get('rephrasing') is None) or (len(d.get('rephrasing'))<0.5*len(question)):
        d['rephrasing'] = question
    d['success'] = int(d['rephrasing'] != question )
    return d if as_dict else d['rephrasing']


ask_for_rephrasing = ask_for_rephrasing_from_question_and_answer

if __name__=='__main__':
    question = """ Please provide a dictionary where keys are town names and values are prime numbers 
              """
    answer = """ The dictionary is {'Dog':12312,'sydney':17} """

    d1 = ask_why_answer_is_wrong(question=question, answer=answer)
    print(d1)

    d2 = ask_for_rephrasing_from_question_and_answer(question=question, answer=answer, reason=d1['reason'])
    print(d2)

    d3 = ask_for_rephrasing_from_question_and_answer(question=question, answer=answer, reason=None)
    print(d3)

