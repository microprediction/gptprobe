def good_to_go():
    """ Checks that OPEN_AI_KEY_0 etc are in env
    :return:
    """
    import os
    try:
        from gptprobe.private_setenv import NOTHING
    except ImportError:
        pass
    checks  = [ os.environ.get(f'OPEN_AI_KEY_{key_choice}') for key_choice in range(3) ]
    return all(checks)