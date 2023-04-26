import openai
import os
from gptprobe.openaiwrappers.opendefaults import DEFAULT_ENGINE, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS


def ask_using_environ(question, key_choice:int=0,
                      engine=None,
                      max_tokens=None,
                      temperature=None, **kwargs):
    """ Use open ai keys in environment variables like OPEN_AI_KEY_0 to ask a question
    :param key_choice  0, 1, or 2  typically
    :return:
    """
    if engine is None:
        engine = os.environ.get('OPEN_AI_ENGINE') or DEFAULT_ENGINE

    if temperature is None:
        try:
            temperature = float(os.environ.get('OPEN_AI_TEMPERATURE'))
        except TypeError:
            temperature = DEFAULT_TEMPERATURE

    if max_tokens is None:
        try:
            max_tokens = int(os.environ.get('OPEN_AI_MAX_TOKENS'))
        except TypeError:
            max_tokens = DEFAULT_MAX_TOKENS


    # Creds
    api_env = f"OPEN_AI_KEY_{key_choice}"
    api_key = os.environ.get(api_env)
    if api_key is None:
        raise ValueError(f'The environment variable {api_env} must be set)')
    openai.api_key = api_key

    response = openai.Completion.create(
        engine=engine,
        prompt=question,
        max_tokens=max_tokens,
        stop=None,
        temperature=temperature,
        **kwargs
    )
    return response.choices[0].text.strip()


if __name__=='__main__':
    from gptprobe.private_setenv import NOTHING
    print(ask_using_environ(question="Is this a good question?"))