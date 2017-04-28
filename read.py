def transcribe(strand: str, target_type):
    if target_type == 'dna':
        target_type = 'DNA'
    if target_type == 'rna':
        target_type = 'RNA'
    assert target_type in ('RNA', 'DNA')
    transcribed_chars = []
    for char in strand:
        if char in ('A', 'a'):
            transcribed_chars.append('T') if target_type == 'DNA' else 'U'
        elif char in ('T', 't'):
            if target_type == 'RNA':
                transcribed_chars.append('A')
            else:
                raise ValueError("Got T character in RNA strand")
        elif char in ('U', 'u'):
            if target_type == 'DNA':
                transcribed_chars.append('A')
            else:
                raise ValueError("Got U character in DNA strand")
        elif char in ('C', 'c'):
            transcribed_chars.append('G')
        elif char in ('G', 'g'):
            transcribed_chars.append('C')
        else:
            raise ValueError("got unexpected character: %s" % char)
    return ''.join(transcribed_chars)


if __name__ == '__main__':
    strand_ = input('enter strand: ')
    target_type_ = input('is strand being converted to RNA or DNA: ')
    print(transcribe(strand_, target_type_))
