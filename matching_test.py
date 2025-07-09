from unittest import TestCase

from matcher import SequencePatternMatcher


#Todo: 
# please implement several matching algorithms using test-driven development.
# Write the test first and elet the expected results guide your code
# Try to not code more functionality than your test requires.
# If you want new functionality, define a new test-case
# Implement:

# 1: A naive pattern mathcing algorithm that compares each character of the pattern against each character of the sequence
# 2: A naive matching algorithm that does the same as above, and also looks for the reverse complement
# 3: A naive matching, with or without reverse complement, that allows up to one mismatch
# 4: The pigeonhole principle as discussed during the workshop. Use a combination of exact (like the naive matching algorithm you wrote) and inexact (like the algorithm in part 3).
# Tip: You may also use the Index class in the file kmer_index.py to query for the position of the first kmer in a search-pattern for a text.
# Tip: This is a complex class, so study it carefully. Courtesy of Ben Langmead, JHU, USA

class MyTestCase(TestCase):
    def test_exact_matching_simple(self):
        #Given
        sequence = "AAAGGGAAA"
        pattern = "GGG"

        #When
        matcher = SequencePatternMatcher(sequence)
        start_positions_matches = matcher.exact_matching_naive(pattern)

        #Then
        self.assertEqual(start_positions_matches, [3])

    def test_exact_matching_not_present(self):
        # Given
        sequence = "AAAGGGAAA"
        pattern = "TCT"

        # When
        matcher = SequencePatternMatcher(sequence)
        start_positions_matches = matcher.exact_matching_naive(pattern)

        # Then
        self.assertEqual(start_positions_matches, [])

    def test_exact_matching_reverse_complement(self):
        # Given
        sequence = "" # Task: Think about a good sequence to find the original pattern, as well as the reverse complement of it
        pattern = "TCA" # Task: A good reverse-complement pattern matching algorithm should be able to find occurences of both this, and its reverse complement

        #Example: If the pattern is ACC, its reverse complement if GGT, and the search should give both their starting positions, if they are present in the pattern

        # When
        matcher = SequencePatternMatcher(sequence)
        start_positions_matches = matcher.exact_matching_reverse_complement(pattern) # Hint: Use the exact_matching_naive function to implement this

        # Then

        expected = [] # change this to the expected result of your test
        self.assertEqual(start_positions_matches, expected)
        
    def test_approximate_matching_one_mismatch(self):
        # Given
        sequence = ""
        pattern = ""
        matcher = SequencePatternMatcher(sequence)
        
        # When
        matcher = SequencePatternMatcher(sequence)
        #start_positions_matches = matcher.approximate_matching_one_mismatch(pattern)  # Hint: Use the exact_matching_naive function to implement this

        expected = []  # change this to the expected result of your test
        #self.assertEqual(start_positions_matches, expected)
        

    def test_pigeonhole_one_match(self):
        pass



