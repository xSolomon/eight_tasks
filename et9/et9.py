''' Generate all correct sequences of brackets. '''

def produce_all_correct_bracket_sequences(brackets_count : int, opening_brackets_number : int,
    closing_brackets_number : int, current_sequence : str, sequences : list[str]) -> list[str]:
    ''' Tries to put brackets until they reach required number. '''
    if opening_brackets_number == brackets_count and closing_brackets_number == brackets_count:
        sequences.append(current_sequence)
        return
    if opening_brackets_number < brackets_count:
        produce_all_correct_bracket_sequences(brackets_count, opening_brackets_number + 1,
            closing_brackets_number, current_sequence + '(', sequences)
    if closing_brackets_number < opening_brackets_number:
        produce_all_correct_bracket_sequences(brackets_count, opening_brackets_number,
            closing_brackets_number + 1, current_sequence + ')', sequences)
    return sequences

def generate_all_correct_bracket_sequences(opening_brackets_number : int) -> list[str]:
    ''' Uses recursive algorithm. '''
    return produce_all_correct_bracket_sequences(opening_brackets_number, 0, 0, "", [])
