'''A3. Tester for the function common_words in tweets.
'''

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    '''Tester for the function common_words in tweets.
    '''

    def test_empty(self):
        '''Empty dictionary.'''

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        '''Dictionary with one word limit is 1.'''

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_one_word_limit_greater_than_one(self):
        '''Dictionary with one word limit greater than one'''

        arg1 = {'hello': 2}
        arg2 = 2
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)   
        
    def test_multiple_words_limit_equal_to_num_words(self):
        '''Dictionary with many words where the limit is equal to num words'''

        arg1 = {'hello': 2, 'hi': 3, 'hey': 4}
        arg2 = 3
        exp_arg1 = {'hello': 2, 'hi': 3, 'hey': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg) 
        
    def test_multiple_words_limit_greater_than_num_words(self):
        '''Dictionary with many words where the limit is greater to num words'''

        arg1 = {'hello': 2, 'hi': 3, 'hey': 4}
        arg2 = 4
        exp_arg1 = {'hello': 2, 'hi': 3, 'hey': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        
    def test_multiple_words_limit_less_than_num_words_some_valid_words(self):
        '''Dictionary with many words where the limit is less then the num words 
        where some of the words remain'''

        arg1 = {'hello': 2, 'hi': 3, 'hey': 4, 'sup': 3}
        arg2 = 2
        exp_arg1 = {'hey': 4}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg) 
        
    def test_multiple_words_limit_less_than_num_words_no_valid_words(self):
        '''Dictionary with many words where n is less to num words where none
        of the words remain'''

        arg1 = {'hello': 4, 'hi': 4}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)        
        

    

if __name__ == '__main__':
    unittest.main(exit=False)
