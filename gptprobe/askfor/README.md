# User Guide 

See also the colab [tutorial](https://github.com/microprediction/gptprobe/blob/main/colab/gptprobe_tutorial.ipynb).


### Finding what you want
This package provides simple self-contained functions. 
It is intended to be auto-complete friendly and self-descriptive, but there are
shorthands provided. For example these are equivalent

    from gptprobe.askfor.clarificationfromquestionandanswer import ask_for_clarification_from_question_and_answer
    from gptprobe.askfor.clarification import ask_for_clarification 




### Terminology
In addition to pretty obvious conventions like `question`, `answer`, `text`, `dict` etc the following may
help you interpret the code: 

    | Term          | Description                                                    |
    |---------------|----------------------------------------------------------------|
    | flaw          | A reason why an answer to a question is inadequate             |
    | ratification  | A reason why an answer is either inadequate or adequate        |
    | clarification | A short follow-up prompt intended to provoke a better answer   |
    | rephrasing    | A longer, self-contained version of the original question      |



### Return conventions 
If a function is called `ask_for_blah` then it can usually return either
a string or a dictionary that wraps the result and provides a success flag:

      {'success':1,'blah':'this reponse is great'}

Use the `as_dict` argument to toggle. 

