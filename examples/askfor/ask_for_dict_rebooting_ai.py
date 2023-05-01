from gptprobe.askfor.dictfromquestionwithretries import ask_for_dict_from_question_with_retries
from getjson import getjson
from gptprobe.utils.equivalence import dict_equal_or_none
from pprint import pprint

# Compute the Artificial Gary Index (AGI)


if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    rebooting = getjson('https://raw.githubusercontent.com/microprediction/gptprobe/main/examples/askfor/rebooting.json')
    question_count = 0
    correct_count = 0

    for title,qa in rebooting.items():
        question = qa['question']
        answer = qa['answer']
        d = ask_for_dict_from_question_with_retries(question=question)
        if not isinstance(d,dict):
            print('Failed to extract dict, fix me!')
            pprint(d)
        else:
            question_count += 1

        try:
           equal = dict_equal_or_none(d, answer)

           if equal:
               pass
               correct_count += 1
           else:
               pprint({"qa": qa, "response": d})
        except Exception as e:
            print(e)
            print('Fix this example! ')

    agi = correct_count/question_count
    print({'question_count':question_count,'correct_count':correct_count,'agi':agi})


