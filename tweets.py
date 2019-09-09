"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def alnum_prefix(text: str) -> str:
    """Return the alphanumeric prefix of text, converted to
    lowercase. That is, return all characters in text from the
    beginning until the first non-alphanumeric character or until the
    end of text, if text does not contain any non-alphanumeric
    characters.

    >>> alnum_prefix('')
    ''
    >>> alnum_prefix('IamIamIam')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!andMore')
    'iamiamiam'
    >>> alnum_prefix('$$$money')
    ''

    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'

    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats @CATS$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    >>> extract_mentions('No valid @!mentions! here?@')
    []

    """
    
    mentions = []
    
    for index in range(len(text)):        
        if text[index] == MENTION_SYMBOL and index + 1 != len(text) and \
           text[index + 1].isalnum():
            mentions.append(alnum_prefix(text[index + 1:]).lower())

    return mentions


###### TODO: Add the remaining Assignment 3 functions below.

def extract_hashtags(text: str) -> List[str]:
    """ Return the valid hashtags present in the text without any duplicates 
    and the # symbol removed. Valid hashtags start with the '#' symbol, start 
    with an alphanumeric character and go on until the first non-aphanumeric 
    character or until the end of the string.

    >>> extract_hashtags('Hi #UofT do you like #cats #CATS #meowmeow')
    []
    >>> extract_hashtags('@cats are #cute #cat #cat meow @meow')
    []
    >>> extract_hashtags('@many @cats$extra @meow?!')
    []
    >>> extract_hashtags('No valid hashtags @! here?')
    []
    >>> extract_hashtags('No valid #!hashtags @! here?#')
    []
    """
    
    #collect all of the valid hashtags present in the text of the tweet
    all_hashtags = []
    
    for index in range(len(text)):
        if (text[index] == HASH_SYMBOL and index + 1 != len(text) and \
            text[index + 1].isalnum()):
            all_hashtags.append(alnum_prefix(text[index + 1:]).lower())
            
    
    #remove all duplicates from the list of hashtags
    new_hashtags = []
            
    for hashtag in all_hashtags:
        if hashtag not in new_hashtags:
            new_hashtags.append(hashtag)
             
    return new_hashtags


def count_words(text: str, words_to_count: Dict[str, int]) -> None:
    """ Modify the words_to_count dictionary to incrementally count each word 
    in the text. Each word is lowercased and only alphanumeric.
    
    >>> y = {'a': 3}
    >>> count_words('#UofT Nick Frosst: Google Brain re-searcher by day, \
    singer @goodkidband by night!', y)
    >>> y == {'a': 3, 'nick': 1, 'frosst': 1, 'google': 1, 'brain': 1, 
    'researcher': 1, 'by': 2, 'day': 1, 'singer': 1, 'night': 1}
    True
    
    >>> y = {'a': 3}
    >>> count_words('a! AA A, a b', y)
    >>> y == {'a': 6, 'aa': 1, 'b': 1}
    True
    
    """
    
    words = text.split()
            
    for word in words:
        
        hashtag = extract_hashtags(word)
        mention = extract_mentions(word)

        if not word.startswith(URL_START) and mention == [] and hashtag == []:
            
            w = clean_word(word)
            
            if w in words_to_count:
                words_to_count[w] += 1
            else:
                words_to_count[w] = 1              
        

def common_words(words_to_counts: Dict[str, int], max_words: int) -> None:
    ''' Modifies the words_to_counts dictionary to only include the max_words
    number of common words. If at max_words the words are tied remove them all
    
    >>> d = {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 3}
    >>> common_words(d, 2)
    >>> d == {'b': 2, 'e': 3}
    True 
    
    >>> d = {'a': 5, 'b': 6, 'c': 3, 'd': 5}
    >>> common_words(d, 2)
    >>> d == {'b': 6}
    True 
    
    >>> d = {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1}
    >>> common_words(d, 4)
    >>> d == {'a': 2, 'b': 2, 'c': 2}
    True 
    '''
    
    temp = {}
    
    if max_words > len(words_to_counts):
        max_words = len(words_to_counts)
    
    for _ in range(max_words):

        max_value = max(words_to_counts.values(), default=0)
        
        count = list(words_to_counts.values()).count(max_value)  
                
        if len(temp) + count > max_words:
            break 
        
        for word in words_to_counts.copy():
            
            if words_to_counts[word] == max_value:
                temp[word] = max_value
                words_to_counts.pop(word) 
             
    words_to_counts.clear()
    
    words_to_counts.update(temp)
    
    

def read_tweets(text: TextIO) -> Dict[str, List[tuple]]:
    ''' Reads in an open .txt file and stores the data in a dictionary from 
    users to thier tweets and relevent info in tuples.  
    '''
    
    users_to_tweets = {}
    
    #tracks position in file. (1 - tweet info, 2 - tweet text)
    position = -1
    
    for line in text:
        
        #records username
        if line.endswith(':\n'):
            username = line[:-2].lower()
            users_to_tweets[username] = []
            position = 1
        
        #collect tweet info
        elif position == 1:
            
            tweet_info = line.split(',')
            
            tweet_date = int(tweet_info[FILE_DATE_INDEX])
            tweet_source = tweet_info[FILE_SOURCE_INDEX]
            favourite_count = int(tweet_info[FILE_FAVOURITE_INDEX])
            retweet_count = int(tweet_info[FILE_RETWEET_INDEX]) 
            
            position = 2
            tweet_text = ''      
        
        #collect enitre tweet text      
        elif position == 2:
        
            if line == '<<<EOT\n':
                
                tweet_text = tweet_text.strip()
                users_to_tweets[username].append((tweet_text, tweet_date, 
                                                  tweet_source, favourite_count,
                                                  retweet_count))
                
                position = 1
                
            else:
                tweet_text = tweet_text + line
            
    return users_to_tweets       
         

def most_popular(users_to_tweets: Dict[str, List[tuple]], start_date: int, 
                 end_date: int) -> str:
    '''Return the most popular user based on thier retweets and favourite count
    in users_to_tweets, in between the start_date and end_date
    
    >>> file = open('tweets_small.txt', 'r')
    >>> most_popular(read_tweets(file), 20010911104335, 20500911104335)
    'uoftcompsci'
    
    >>> file = open('tweets_big.txt', 'r')
    >>> most_popular(read_tweets(file), 20010911104335, 20500911104335)
    'uoftcompsci'
    
    >>> file = open('tweets_big.txt', 'r')
    >>> most_popular(read_tweets(file), 20181109220100, 20181109220110)
    'uoftnews'
    '''
    
    users_to_score = {}
    
    for user in users_to_tweets:
        
        users_to_score[user] = -1
        
        for tweet in users_to_tweets[user]:
            
            if tweet[TWEET_DATE_INDEX] <= end_date and tweet[TWEET_DATE_INDEX] \
               >= start_date:
                
                if users_to_score[user] == -1:
                    users_to_score[user] = 0
                
                users_to_score[user] += tweet[TWEET_FAVOURITE_INDEX]
                users_to_score[user] += tweet[TWEET_RETWEET_INDEX]
    
    winner = max(users_to_score.values())
    
    if winner == -1:
        return 'tie'
    elif list(users_to_score.values()).count(winner) > 1:
        return 'tie'
    else:
        for user in users_to_tweets:
            if users_to_score[user] == winner:
                return user


def detect_author(users_to_tweets: Dict[str, List[tuple]], text: str) -> str:
    '''Return the most likely author of a tweets text based on the hashtags 
    they use in users_to_tweets.
    
    >>> file = open('tweets_small.txt', 'r')
    >>> detect_author(read_tweets(file), '#uoftalumni #UofT')
    'uoftcompsci'
    
    >>> file = open('tweets_big.txt', 'r')
    >>> detect_author(read_tweets(file), 'im indifferent towards #UofT')
    'unknown'
    '''
    
    hashtags = extract_hashtags(text)
    
    author = ''
    
    #find the user who used all of the hashtags
    for user in users_to_tweets:
        
        used_hashtags = get_hashtags(users_to_tweets, user)
        
        if set(hashtags).issubset(used_hashtags):
            author = user 
    
    if author == '':
        return 'unknown'
    
    #check if the hashtags used are unique
    for h in hashtags:
        
        for user in users_to_tweets:
            
            used_hashtags = get_hashtags(users_to_tweets, user)
            
            if h in used_hashtags and user != author:
                return 'unknown'
        
    return author

def get_hashtags(users_to_tweets: Dict[str, List[tuple]], user: str) \
    -> List[str]:
    '''Return a list of all of the hashtags that a user has used throughout 
    thier tweet history. Duplicate hashtags exist but only once per tweet.
    
    Precondition: the user's name is lowercase
    
    >>> file = open('tweets_big.txt', 'r')
    >>> get_hashtags(read_tweets(file), 'utsc')
    ['utsc']
    
    >>> file = open('tweets_big.txt', 'r')
    >>> get_hashtags(read_tweets(file), 'uoftnews')
    ['uoft', 'uoftremembers', 'uoft', 'uoftremembers', 'uoft', 'uoft', 
    'uoftgrad18']
    '''
    
    hashtags = []
    
    for tweet in users_to_tweets[user]:
        hashtags.extend(extract_hashtags(tweet[TWEET_TEXT_INDEX]))
        
    return hashtags   



if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
