my_symbols = {
    'X': 1,  # strategy / lose
    'Y': 2,  # strategy / tie
    'Z': 3  # strategy / win
}

their_symbols = {
    'A': 1,
    'B': 2,
    'C': 3
}

winning_symbols = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

losing_symbols = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}


def get_score(plays):
    score = 0
    for play in plays:
        them, me = play.split()
        score += my_symbols[me]
        if their_symbols[them] == my_symbols[me]:
            score += 3
        defeated_number: int = my_symbols[me] - 1
        if defeated_number == 0:
            defeated_number = 3
        if their_symbols[them] == defeated_number:
            score += 6
    return score


def get_scores_harder(plays):
    score = 0
    for play in plays:
        them, strategy = play.split()
        if strategy == 'X':  # we need to lose
            score += their_symbols[losing_symbols[them]]
        if strategy == 'Y':  # we need to tie
            score += 3
            score += their_symbols[them]
        if strategy == 'Z':
            score += 6
            score += their_symbols[winning_symbols[them]]

    return score
