from unittest import TestCase
from unittest.mock import Mock

import pytest

from pigeonhole import pigeonhole_matching

@pytest.fixture(scope='class')
def provide_index(request):
    index = Mock()
    index.k = 3
    request.cls.index = index

@pytest.mark.usefixtures('provide_index')
class MyTestCase(TestCase):

    def test_pigeonhole_one_match(self):
        index = self.index
        index.query.return_value = [3]


        test_sequence = 'AAACCCTTTAAAA'
        test_pattern = 'CCCTTT'

        ph = pigeonhole_matching(index)

        self.assertIsNotNone(ph)
        matches = ph.match_pattern_one_mm(test_sequence, test_pattern)
        self.assertEqual(len(matches), 1)

    def test_pigeonhole_matching_no_match(self):
        index = self.index
        index.query.return_value = []

        test_sequence = 'AAAAAAAAAAAA'
        test_pattern = 'CCCTTT'

        ph = pigeonhole_matching(index)

        matches = ph.match_pattern_one_mm(test_sequence, test_pattern)
        self.assertEqual(len(matches), 0)

    def test_pigeonhole_matching_one_match_with_mm(self):
        test_sequence = 'AAACCCATTAAAA'
        test_pattern = 'CCCTTT'
        
        
        def side_effect_index(kmer):
            if kmer == 'CCC':
                return [3]
            else:
                return []

        index = self.index
        index.query.side_effect = side_effect_index

        ph = pigeonhole_matching(index)

        matches = ph.match_pattern_one_mm(test_sequence, test_pattern)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], 3)

    def test_naive_matching_w_mm(self):
        index = self.index
        ph = pigeonhole_matching(index)

        is_match, mm_number = ph.match_naive_1mm("AAAT", "AAAA")
        self.assertEqual(is_match, True)
        self.assertEqual(mm_number, 1)

        is_match, mm_number = ph.match_naive_1mm("AAAA", "AAAA")
        self.assertEqual(is_match, True)
        self.assertEqual(mm_number, 0)

        is_match, mm_number = ph.match_naive_1mm("AAAA", "TAAT")
        self.assertEqual(is_match, False)
        self.assertEqual(mm_number, 2)

    def test_left_matching(self):
        index = self.index
        ph = pigeonhole_matching(index)
        kmer = 'CCC'
        sequence = 'AAACCCTTTAAACCC'
        offsets_right = [6, 12]

        expected_result = [3]
        hits = ph.check_left_mm(kmer, offsets_right, sequence)

        self.assertEqual(hits, expected_result)

        kmer = 'CCC'
        sequence = 'AAACCCTTTAAACCCTTT'
        offsets_right = [6, 16]
        expected_result = [3, 13]
        hits = ph.check_left_mm(kmer, offsets_right, sequence)
        self.assertEqual(hits, expected_result)


if __name__ == '__main__':
    unittest.main()
