'''A3. Tester for the function extract_mentions in tweets.
'''

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    '''Tester for the function extract_mentions in tweets.
    '''

    def test_empty(self):
        '''Empty tweet.'''

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        '''Non-empty tweet with no mentions.'''

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_nonempty_no_mention_with_hash_character(self):
        '''Non-empty tweet with no mentions but with mention symbol before a
        non-alphanum character.'''

        arg = 'tweet @! test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_nonempty_no_mention_with_final_character_hash(self):
        '''Non-empty tweet with no mentions but with a mention symbol at the 
        end of tweet'''

        arg = 'tweet test case @'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_nonempty_one_mention_all_lowercase_ends_with_non_alpha(self):
        '''Non-empty tweet with one mention which ends with a non-alphanum
        character '''

        arg = 'tweet @test case'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)          
          
    def test_nonempty_one_mention_all_lowercase_end_of_string(self):
        '''Non-empty tweet with one mention which ends with the end of the 
        string '''

        arg = 'tweet test @case'
        actual = tweets.extract_mentions(arg)
        expected = ['case']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_one_mention_all_uppercase(self):
        '''Non-empty tweet with one mention which is uppercase'''

        arg = 'tweet @TEST case'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_nonempty_many_mentions_all_different(self):
        '''Non-empty tweet with many mentions of different cases and endings'''

        arg = '@tweet! @TEST @Case'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'test', 'case']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
    def test_nonempty_many_mentions_all_same(self):
        '''Non-empty tweet with many identical mentions'''

        arg = '@tweet @tweet'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'tweet']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)            

    def test_nonempty_many_mentions_all_same_different_cases(self):
        '''Non-empty tweet with many identical mentions of different cases'''

        arg = '@tweet @TWEET'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'tweet']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  

if __name__ == '__main__':
    unittest.main(exit=False)
