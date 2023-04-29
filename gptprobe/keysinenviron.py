def keys_in_environ()->bool:
    """

      1. Check that OPEN_AI_KEY_0, OPEN_AI_KEY__1,OPEN_AI_KEY_2 are in environment variables, which is
                                                         a prerequisite to using /openapiwrappers
    
      2.Side effect: If it finds just OPEN_AI_KEY instead, this will be copied to
                     OPEN_AI_KEY_0, OPEN_AI_KEY__1,OPEN_AI_KEY_2
    
    :return:
    """
    import os
    try:
        from gptprobe.private_setenv import NOTHING
    except ImportError:
        pass
    checks  = [ os.environ.get(f'OPEN_AI_KEY_{key_choice}') for key_choice in range(3) ]
    if all(checks):
        return True
    else:
        single_key = os.environ.get('OPEN_AI_KEY')
        if single_key:
            for key_choice in range(3):
                os.environ[f'OPEN_AI_KEY_{key_choice}'] = single_key
            return True
        else:
            return False 
                 
                           
