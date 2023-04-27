def keys_in_environ():
    """ Checks that OPEN_AI_KEY_0 are in environment variables, which is
    a prerequisite to using /openapiwrappers
    :return:
    """
    import os
    try:
        from gptprobe.private_setenv import NOTHING
    except ImportError:
        pass
    checks  = [ os.environ.get(f'OPEN_AI_KEY_{key_choice}') for key_choice in range(3) ]
    return all(checks)