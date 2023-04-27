from gptprobe.askfor.dictfromquestion import ask_for_dict

if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    question = """What was the result of the 2018 FIFA World Cup final, as a python dict. Do not include anything
                  except the dict in your answer. One key/value for each team/score."""
    d = ask_for_dict(question=question)
    print(d)