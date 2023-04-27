# gptprobe
Example:

    from gptprobe.private_setenv import NOTHING # Sets environ['OPEN_AI_KEY_0'], environ['OPEN_AI_KEY_1'], environ['OPEN_AI_KEY_2']
    from gptprobe.askfor.dictfromquestion import ask_for_text_from_poorly_formatted_dict_text
    messy_dict_text = """ Final scores are 
                                      Australia  1 
                                      Brazil     2
                                        bummer """
    print(ask_for_text_from_poorly_formatted_dict_text(text = messy_dict_text))
    
The result is

    {"Australia": "1", "Brazil": "2"}
   
This package contains simple and complex multi-step interrogations intended to yield structured data. 

# Install & environ setup

    pip install gptprobe 
    
Then from [open ai developer](https://platform.openai.com/account/api-keys) help yourself to three keys and inject them as follows:

    import os 
    os.environ['OPEN_AI_KEY_0'] = 'sk-ekOvFjAHKETQYADDAYADDA'
    os.environ['OPEN_AI_KEY_1'] = 'sk-ekOvFjAHKETQYADDAYADDADO'
    os.environ['OPEN_AI_KEY_2'] = 'sk-ekOvFjAHKETQYADDAYADDADOO'

Maybe you want to mimic [gptprobe/public_setenv.py](https://github.com/microprediction/gptprobe/blob/main/gptprobe/public_setenv.py) 

## User Guide

- See the [README](https://github.com/microprediction/gptprobe/blob/main/gptprobe/askfor/README.md) in the askfor directory. 
- See the [examples](https://github.com/microprediction/gptprobe/tree/main/examples).
     
     


    
