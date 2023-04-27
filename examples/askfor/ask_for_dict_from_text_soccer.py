if __name__=='__main__':
    from gptprobe.askfor.dictfromquestion import _prompt_for_dict_from_text

    messy_dict_text = """ Final score are 
                                      Australia  1 
                                      Brazil     2
                                        bummer """
    d = _prompt_for_dict_from_text(text = messy_dict_text)
    print(d)




