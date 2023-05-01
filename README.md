# gptprobe
Simple example:

    from gptprobe.askfor.dictfrompoorlyformattedtext import ask_for_text_from_poorly_formatted_dict_text
    messy_dict_text = """ Final score are 
                                      Australia  1 
                                      Brazil     2
                                        bummer """
    print(ask_for_text_from_poorly_formatted_dict_text(text = messy_dict_text))

The result is:

    {"Australia": "1", "Brazil": "2"}
   
This package contains simple and complex multi-step interrogations intended to yield structured data, including patterns where ChatGPT4 tries to 
help itself out of a rut, rephrases questions, ratifies answers using a different key, tries to reformat its own responses, and so forth. It may help with your own unmanned missions into the galactic brain. 

# Install & environ setup

    pip install gptprobe 
    
Then from [open ai developer](https://platform.openai.com/account/api-keys) help yourself to a key and inject into environment somehow. E.g.

    import os 
    os.environ['OPEN_AI_KEY'] = 'sk-ekOvFjAHKETQYABBADABBADDAYADDA'

Maybe you want to mimic [gptprobe/public_setenv.py](https://github.com/microprediction/gptprobe/blob/main/gptprobe/public_setenv.py) and import NOTHING from it in your scripts. 

## User Guide

- See the [README](https://github.com/microprediction/gptprobe/blob/main/gptprobe/askfor/README.md) in the askfor directory. 
- See the [examples](https://github.com/microprediction/gptprobe/tree/main/examples).
     
     
## Troubleshooting
File an [issue](https://github.com/microprediction/gptprobe/issues). Pull requests are welcomed. 
     
![](https://raw.githubusercontent.com/microprediction/gptprobe/main/docs/assets/images/probe.png)
     


    
