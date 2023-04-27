from gptprobe.askfor.dictfromquestion import ask_for_dict_from_question
from gptprobe.utils.customtypes import DictOrStr


# Ask why an answer to a question is inadequate


def ask_for_flaw_from_question_and_answer(question:str, answer:str, key_choice=0, as_dict:bool=True)->DictOrStr:
    """
        Ask for an explanation of why an answer to a question is not satisfactory
        (c.f. ask_for_ratification which leads the witness less)

       :param question:       Previously asked question
       :param answer:         An answer that wasn't acceptable
       :return:         {"flaw": "a dog is not a town",
                         "success":1}
    """
    meta_question = """ I will provide now in xml-delimited style, a question, and a previously given but unsatisfactory answer, 
                        Please return a dictionary where the double quoted key is "flaw" and the value is
                        an explanation of why the answer might not be considered satisfactory. Pay special attention
                        to any formatting instructions that were given in the question and not followed to the letter
                        in the answer. Here, in xml-style delimitation, are the question and answer:
                         <question>"""+question+"""</question>
                         <answer>"""+answer+"""</answer>"""
    d = ask_for_dict_from_question(question=meta_question, key_choice=key_choice, numeric_values_only=False)
    d['success'] = 0
    DEFAULT_FLAW = 'I am not sure why the answer does not cut it'
    if (d.get('flaw') is None) or (len(d.get('flaw')) < 0.5 * len(question)):
        d['flaw'] = DEFAULT_FLAW
    d['success'] = int(d['flaw'] != DEFAULT_FLAW)
    return d if as_dict else d['flaw']


ask_for_flaw = ask_for_flaw_from_question_and_answer