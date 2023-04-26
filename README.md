# gptprobe
Extracting information from ChatGPT 



### Install 

    pip install gptprobe 
    
### Keys 
From [open ai developer](https://platform.openai.com/account/api-keys) help yourself to three keys and inject them as follows:

    import os 
    os.environ['OPEN_AI_KEY_0'] = 'sk-ekOvFjAHKETQYADDAYADDA'
    os.environ['OPEN_AI_KEY_1'] = 'sk-ekOvFjAHKETQYADDAYADDADO'
    os.environ['OPEN_AI_KEY_2'] = 'sk-ekOvFjAHKETQYADDAYADDADOO'


### Usage 
Simple one-line commands 

     from gptprobe 
     to_dict("""dog  17 , cat 133, dance 1388 
                yadda badoodle -----""")
     


    