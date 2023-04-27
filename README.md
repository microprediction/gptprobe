# gptprobe
Example:

    from gptprobe.private_setenv import NOTHING # See below
    question = """What was the result of the 2018 FIFA World Cup final, as a python dict. Do not include anything
                  except the dict in your answer. One key/value for each team/score."""
    d = ask_for_dict(question=question)
    print(d)

The result is a Python dictionary:

    {'France': 4, 'Croatia': 2}
   
This package contains simple and complex multi-step interrogations intended to yield structured data, including patterns where ChatGPT4 tries to 
help itself out of a rut, rephrases questions, ratifies answers using a different key, tries to reformat its own responses, and so forth. It may help with your own unmanned missions into the galactic brain. 

# Install & environ setup

    pip install gptprobe 
    
Then from [open ai developer](https://platform.openai.com/account/api-keys) help yourself to three keys and inject them as follows:

    import os 
    os.environ['OPEN_AI_KEY_0'] = 'sk-ekOvFjAHKETQYADDAYADDA'
    os.environ['OPEN_AI_KEY_1'] = 'sk-ekOvFjAHKETQYADDAYADDADO'
    os.environ['OPEN_AI_KEY_2'] = 'sk-ekOvFjAHKETQYADDAYADDADOO'

Maybe you want to mimic [gptprobe/public_setenv.py](https://github.com/microprediction/gptprobe/blob/main/gptprobe/public_setenv.py) and import NOTHING from it. 

## User Guide

- See the [README](https://github.com/microprediction/gptprobe/blob/main/gptprobe/askfor/README.md) in the askfor directory. 
- See the [examples](https://github.com/microprediction/gptprobe/tree/main/examples).
     
     
## Troubleshooting
File an [issue](https://github.com/microprediction/gptprobe/issues). Pull requests are welcomed. 
     
![](https://raw.githubusercontent.com/microprediction/gptprobe/main/docs/assets/images/probe.png)
     


    
