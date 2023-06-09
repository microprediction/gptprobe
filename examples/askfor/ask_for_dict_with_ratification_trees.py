
# This can be hit and miss because ChatGPT4 sometimes thinks it has not answered a question well, when it actually has, or vice-versa.

if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    from pprint import pprint
    from gptprobe.askfor.dictfromquestionwithratification import ask_for_dict_from_question_with_ratification

    question = """Return a dictionary with double-quoted keys comprising five tree names and numeric values
                  indicating the month of the year when they are most likely to bloom. 
               """
    import os
    os.environ['GPTPROBE_VERBOSITY']="1"

    d = ask_for_dict_from_question_with_ratification(question=question)
    pprint(d)