from gptprobe.askfor.dictfromquestionwithretries import ask_for_dict_from_question_with_retries
from getjson import getjson
from gptprobe.utils.equivalence import dict_equal_or_none
from pprint import pprint
import time

# Compute the Artificial Gary Index (AGI)
# ---------------------------------------
#
# Runs through examples of machine failure in "Rebooting AI" by Gary Marcus
# Computes the fraction of answers that are correct


if __name__ == '__main__':
    from gptprobe.private_setenv import NOTHING

    rebooting = getjson(
        'https://raw.githubusercontent.com/microprediction/gptprobe/main/examples/askfor/rebooting.json')
    question_count = 0
    correct_count = 0

    for title, qa in rebooting.items():
        question = qa['question']
        answer = qa['answer']
        d = ask_for_dict_from_question_with_retries(question=question)
        if not isinstance(d, dict):
            print('Failed to extract dict, fix me!')
            pprint(d)
        else:
            question_count += 1
        time.sleep(0.2)

        try:
            d = dict([(k,int(v)) for k,v in d.items()])
            is_right = dict_equal_or_none(d, answer, case_insensitive=True)

            if is_right:
                pass
                correct_count += 1
            else:
                pprint({"qa": qa, "response": d})
        except Exception as e:
            print(e)
            print('This should not happen')

    agi = correct_count / question_count
    print({'question_count': question_count, 'correct_count': correct_count, 'agi': agi})
