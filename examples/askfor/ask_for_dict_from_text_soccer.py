if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING # Sets environ['OPEN_AI_KEY_0'] ... environ['OPEN_AI_KEY_2']
    from gptprobe.askfor.textfrompoorlyformatteddicttext import ask_for_text_from_poorly_formatted_dict_text
    messy_dict_text = """ Final score are 
                                      Australia  1 
                                      Brazil     2
                                        bummer """
    print(ask_for_text_from_poorly_formatted_dict_text(text = messy_dict_text))

# Result is  {"Australia": "1", "Brazil": "2"}


