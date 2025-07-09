import kmer_index


class pigeonhole_matching:
    def __init__(self, index: kmer_index):
        self.index = index

    """def match_pattern_one_mm(self, test_sequence, test_pattern): 
        return [1]"""

    """def match_pattern_one_mm(self, test_sequence, test_pattern):
        return self.index.query(test_pattern)"""

    def match_pattern_one_mm(self, test_sequence, test_pattern):

        kmer_1, kmer_2 = test_pattern[0:self.index.k], test_pattern[self.index.k:2*self.index.k]
        first_matches = self.index.query(kmer_1)
        second_matches = self.index.query(kmer_2)
        return first_matches


    def match_naive_1mm(self, test_sequence, test_pattern) -> (bool, int):
        mm = 0
        for i in range(len(test_pattern)):
            if test_pattern[i] != test_sequence[i]:
                mm += 1
                if mm > 1:
                    return False, mm
        return True, mm

    def check_left_mm(self, kmer:str, offsets: list[int], sequence: str) -> list[int]:
        hits = []
        for index in offsets:
            match, _ = self.match_naive_1mm(kmer, sequence[index-len(kmer):index])
            if match:
                hits.append(index-len(kmer))

        return hits


