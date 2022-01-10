# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U`
    """
    bp_dict={'A':'T','T':'A','C':'G','G':'C'}
    seq="".join([bp_dict[x] for x in list(seq)])
    return seq.replace('T','U')

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by replacing
    all `T` to `U` then reverses the sequence
    """
    return transcribe(seq)[::-1]
    
