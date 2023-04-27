
if __name__=='__main__':
    from gptprobe.askfor.textfrompoorlyformatteddicttext import ask_for_text_from_poorly_formatted_dict_text

    messy_dict_text = """ Final score are 
                                  Australia  1 
                                  Brazil     2
                                    bummer """
    clean_dict_text = ask_for_text_from_poorly_formatted_dict_text(messy_dict_text)
    print(clean_dict_text)
    # {"Australia": "1", "Brazil": "2"}

