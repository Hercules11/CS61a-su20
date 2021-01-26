"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime
# refer to https://github.com/zhou0220/cs61a-su20/blob/master/project/cats/cats.py


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    value = 0
    for e in paragraphs:
        if select(e):
            if value == k:
                return e
            value += 1
    return ''
    # END PROBLEM 1

# import re
def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(element):
        list_el = remove_punctuation(element).lower().split()
        # wuwuwu, not notice the note
        #  list_el = re.split(r'[^(A-Za-z)]',element.lower().replace(r'[^(\sA-Za-z)]',''))
        for e in topic:
            for x in list_el:
                if e == x:
                    return True
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    len_typed = len(typed_words)
    len_ref = len(reference_words)
    boundary = min(len_ref, len_typed)
    correct_num = 0
    for x in range(0, boundary):
        if typed_words[x] == reference_words[x]:
            correct_num += 1
    if len_typed == 0:
        return 0.0
    else :
        result = correct_num*100.0 / len_typed
        return result
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    len_typed = len(typed)
    wpm = (len_typed/5.0) / (elapsed/60)
    return wpm
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    diff_dict = {}
    if user_word in valid_words:
        return user_word
    for e in valid_words:
        diff_value = diff_function(user_word, e, limit)
        if  diff_value <= limit:
            diff_dict[e] = diff_value
    if diff_dict:
        return min(diff_dict, key=diff_dict.get) # 神来之笔，抄别人的
    return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'
    # recursivion can recursive itself:
    if start == goal:
        return 0
    if limit == 0:
        return 1
    len_start = len(start)
    len_goal = len(goal)
    boundary = min(len_start, len_goal)
    if boundary == 0:
        return len_start + len_goal
    if start[0] != goal[0]:
        return 1 + shifty_shifts(start[1:], goal[1:], limit-1)
    return shifty_shifts(start[1:], goal[1:], limit)
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, 'Remove this line'

    if limit < 0 or len(start)==0 or len(goal)==0 : # Fill in the condition
        # 分情况讨论，确定边界条件
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start) + len(goal)
        # END

    elif start[0] == goal[0]: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return meowstake_matches(start[1:], goal[1:], limit)
        # END
    else :
        add_diff = 1 + meowstake_matches(start, goal[1:], limit-1)  # Fill in these lines
        remove_diff = 1 + meowstake_matches(start[1:], goal, limit-1)
        substitute_diff = 1 + meowstake_matches(start[1:], goal[1:], limit-1)
        # BEGIN
        return min(add_diff, remove_diff, substitute_diff)
        "*** YOUR CODE HERE ***"
        # END

# def ways(num):
#     left_step = num
#     if left_step == 1:
#         return 1
#     elif left_step == 2:
#         return 2
#     return ways(left_step -1)+ ways(left_step -2)

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    # assert False, 'Remove this line to use your final_diff function'
    return False


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    if len(typed) == 0:
        send({ 'id':id,'progress': 0.0})
        return 0.0
    else :
        i = 0
        value = 0
        for e in range(0, len(typed)):
            if typed[i] == prompt[i]:
                value += 1
                i += 1
            else :
                break
    progress = value / len(prompt)
    send({'id': id, 'progress': progress})
    return progress

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for el in times_per_player:
        index = 1
        s = []
        while index < len(el):
            s.append(el[index] - el[index -1])
            index += 1
        times.append(s)
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # s.index(x[, i[, j]])   list.index(min(list))
    # x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前）
    word_list = []
    for el in players:
        word_list.append([])
    for w in words:
        time_list = []
        for t in players:
            time_list.append(time(game, t , w))
        min_index = time_list.index(min(time_list))
        word_list[min_index].append(word_at(game, w))
    return word_list
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you

##########################
# Extra Credit #
##########################
import math
key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase
    # fighting fighting fighting for future
    # BEGIN PROBLEM EC1
    "*** YOUR CODE HERE ***"
    if limit < 0 :
        return math.inf
    elif len(start)==0 or len(goal)==0:
        return len(start) + len(goal)
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else :
        distance = key_distance[start[0], goal[0]]
        if distance > 2:
            distance = 2
        add_diff = 1 + key_distance_diff(start, goal[1:], limit -1)
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit -1)
        substitute_diff = distance + key_distance_diff(start[1:], goal[1:], limit -distance)
        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized
key_distance_diff = memo(key_distance_diff)
key_distance_diff = count(key_distance_diff)

found_dict = {}
# https://www.youtube.com/watch?v=IB8VSP9EZQs&list=PL6BsET-8jgYXsQ35_ZS1e_tX5LZf5PPrS&index=3
def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"
    diff_dict = {}
    if user_word in valid_words:
        return user_word
    if (user_word, diff_function) in found_dict:
        # TypeError: unhashable type: 'list'
        # unable add the valid_words
        return found_dict[(user_word, diff_function)]
    for e in valid_words:
        diff_value = diff_function(user_word, e, limit)
        if  diff_value <= limit:
            diff_dict[e] = diff_value
    if diff_dict:
        result = min(diff_dict, key=diff_dict.get)
        found_dict[(user_word, diff_function)] = result
        return result
    return user_word
    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)