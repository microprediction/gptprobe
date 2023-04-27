# gptprobe
Extracting information from ChatGPT 



# Step 0: Install 

    pip install gptprobe 
    
# Step 1: Inject three OpenAI keys
From [open ai developer](https://platform.openai.com/account/api-keys) help yourself to three keys and inject them as follows:

    import os 
    os.environ['OPEN_AI_KEY_0'] = 'sk-ekOvFjAHKETQYADDAYADDA'
    os.environ['OPEN_AI_KEY_1'] = 'sk-ekOvFjAHKETQYADDAYADDADO'
    os.environ['OPEN_AI_KEY_2'] = 'sk-ekOvFjAHKETQYADDAYADDADOO'


# Step 2: Using it
The package provides utility functions for getting better, more programmatically useful
answers categorized by the complexity of the interaction. The more complex, the more it
will cost you, of course. 

  | Verb   | Explanation                                                | Output   |
  |------------------------------------------------------------|----------------------------------------------|----------|
  | Prompt | A single question, with raw text response                  | text     |
  | Ask    | A small number of prompts with a stuctured response        | dict     |
  | Inquire| A more involved exploration (recursion depth param needed) | dict     |
     
### Examples of prompts (text output)

     from gptprobe.promptfor.dictformat import prompt_for_dict_format
     messy_dict_text = """ Final score are 
                           Australia  1 
                           Brazil     2
                             bummer """
     clean_dict_text = prompt_for_dict_format(messy_dict_text)



     


    