
# This can be hit and miss because ChatGPT4 sometimes thinks it has not answered a question well, when it actually has, or vice-versa.

if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    from pprint import pprint
    from gptprobe.askfor.dictfromquestionwithratification import ask_for_dict_from_question_with_ratification

    question = """Return three occupation names, each with a funny joke about the occupation. 
               """
    import os
    os.environ['GPTPROBE_VERBOSITY']="1"

    d = ask_for_dict_from_question_with_ratification(question=question, numeric_values_only=False)
    pprint(d)