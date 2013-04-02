from nose.tools import *
from ex48 import parser
from ex48.parser import ParserError
from ex48.parser import Sentence


def test_sentence():
   result = Sentence(('noun', 'princess'), ('verb', 'throws'), ('object', 'coins'))
   assert_equal(result.subject, "princess")

def test_peek():
   word_list = parser.peek([('noun', 'princess'), ('verb', 'throws'), ('object', 'coins')])
   assert_equal(word_list, 'noun')

def test_peek_empty_list():
   empty_list = parser.peek(())
   assert_equal(empty_list, None)

def test_match_no_word_list():
   no_word_list = parser.peek(())
   assert_equal(no_word_list, None)

def test_match():
   word_list = [('noun', 'princess'), ('verb', 'throws'), ('object', 'coins')]
   match_working = parser.match(word_list, ('noun'))
   assert_equal(match_working, ('noun', 'princess'))

def test_match_not_equal():
   word_list = [('noun', 'princess'), ('verb', 'throws'), ('object', 'coins')]
   match_not_equal = parser.match(word_list, ('foo'))
   assert_equal(match_not_equal, None)

def test_match_empty_word_list():
   empty_word_list = []
   assert_equal(parser.match(empty_word_list, 'noun'), None)

def test_skip():
   word_list = [('noun', 'princess'), ('verb', 'throws'), ('object', 'coins')]
   skip_working = parser.skip(word_list, 'noun')

def test_parse_verb():
   word_list = [('stop', 'the'), ('verb', 'throws'), ('object', 'coins')]
   parse_verb_working = parser.parse_verb(word_list)
   assert_equal(parse_verb_working, ('verb', 'throws')) 

def test_parse_verb_not_verb():
   word_list = [('stop', 'the'), ('direction', 'left'), ('object', 'coins')]
   assert_raises(ParserError, parser.parse_verb, word_list)

def test_parse_object_noun_next():
   word_list = [('stop', 'the'), ('noun', 'hammer'), ('object', 'coins')]
   noun_next = parser.parse_object(word_list) 
   assert_equal(noun_next, ('noun', 'hammer'))

def test_parse_object_direction_next():
   word_list = [('stop', 'the'), ('direction', 'north'), ('object', 'coins')]
   direction_next = parser.parse_object(word_list)
   assert_equal(direction_next, ('direction', 'north'))

def test_parse_object_noun_and_direction_not_next():
   word_list = [('stop', 'the'), ('object', 'coins')]
   assert_raises(ParserError, parser.parse_object, word_list)

def test_parse_subject():
   subject = ('noun', 'princess')
   verb = ('verb', 'go')
   obj = ('direction', 'left')
   word_list = [verb, obj]
   s1 = parser.parse_subject(word_list, subject)
   s2 = Sentence(subject, verb, obj)
   assert_equal(s1.subject, s2.subject)
   assert_equal(s1.verb, s2.verb)
   assert_equal(s1.object, s2.object)

def test_parse_sentence():
   subject = ('noun', 'princess')
   verb = ('verb', 'go')
   obj = ('direction', 'left')
   word_list = [('stop', 'the'), ('noun', 'princess'), ('verb', 'go'), ('direction', 'left')]
   s1 = parser.parse_sentence(word_list)
   s2 = Sentence(subject, verb, obj)
   assert_equal(s1.subject, s2.subject)
   assert_equal(s1.verb, s2.verb)
   assert_equal(s1.object, s2.object)

def test_parse_sentence():
   subject = ('noun', 'player')
   verb = ('verb', 'go')
   obj = ('direction', 'left')
   word_list = [('stop', 'the'), ('verb', 'go'), ('direction', 'left')]
   s1 = parser.parse_sentence(word_list)
   s2 = Sentence(subject, verb, obj)
   assert_equal(s1.subject, s2.subject)
   assert_equal(s1.verb, s2.verb)
   assert_equal(s1.object, s2.object)


