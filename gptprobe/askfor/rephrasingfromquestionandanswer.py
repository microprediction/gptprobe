from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.utils.customtypes import DictOrStr
from gptprobe.askfor.flawfromquestionandanswer import ask_for_flaw_from_question_and_answer


def ask_for_rephrasing_from_question_and_answer(question:str,
                                                answer:str,
                                                key_choice=0,
                                                as_dict=False,
                                                ask_for_flaw=False)->DictOrStr:
    """
         A rephrasing of a question given only the question and the answer, presumed to be flawed.

    :param question:
    :param answer:
    :param key_choice:
    :param ask_for_flaw:   If True, a separate call will first ask for a flaw
    :param as_dict:
    :return:
    """
    if ask_for_flaw:
        from gptprobe.askfor.flawfromquestionandanswer import ask_for_flaw_from_question_and_answer
        flaw_dict = ask_for_flaw_from_question_and_answer(question=question, answer=answer, as_dict=True)
        if flaw_dict.get('success') and flaw_dict.get('flaw'):
             flaw = flaw_dict['flaw']
             rotated_key = (key_choice + 1 ) % 3
             from gptprobe.askfor.rephrasingfromquestionanswerandflaw import ask_for_rephrasing_from_question_answer_and_flaw
             return ask_for_rephrasing_from_question_answer_and_flaw(question=question, answer=answer,
                                                                     flaw=flaw, key_choice=rotated_key,
                                                                     as_dict=as_dict)
        else:
            return ask_for_flaw_from_question_and_answer(question=question,
                                                         answer=answer,
                                                         key_choice=key_choice,
                                                         as_dict=as_dict)
    # Having reached this point we assume no flaw can be provided to help.
    rephrasing_prompt = """ I will provide now in xml-delimited style, a question, and an unsatisfactory answer previously
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
    d = ask_for_dict_from_question(question=rephrasing_prompt, key_choice=key_choice, numeric_values_only=False)

    # Before returning, re-evaluate success if the rephrasing leaves the question unchanged.
    d['success'] = 0
    if (d.get('rephrasing') is None) or (len(d.get('rephrasing')) < 0.5 * len(question)):
        d['rephrasing'] = question
    d['success'] = int(d['rephrasing'] != question)
    return d if as_dict else d['rephrasing']



if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    question = """ Please provide a dictionary where keys are town names and values are prime numbers 
              """
    answer = """ The dictionary is {'Dog':12312,'sydney':17} """



    d3 = ask_for_flaw_from_question_and_answer(question=question, answer=answer)
    print(d3)

