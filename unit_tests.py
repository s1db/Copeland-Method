import unittest
import iterative_copeland as ic

class TestIterativeCopelandMethods(unittest.TestCase):
    
    def test_example(self):
        wiki_rankings = [[0,  0,  3,  3,  1],   # C_0
                         [1,  1,  0,  0,  2],    # C_1
                         [2,  2,  1,  1,  3],    # C_2
                         [3,  3,  2,  2,  0]]    # C_3 <-- candidates
        wiki_pairwise_scores = [2, 2, 0, 3, 1, 1]
        wiki_copeland_scores = [2, 2, 1, 1]

        example_score_list = ic.pairwiseScoreCalcListFull(wiki_rankings, len(wiki_rankings), len(wiki_rankings[0]))
        self.assertEqual(example_score_list, wiki_pairwise_scores)
        final_copeland_score = ic.copelandScoreFull(example_score_list, len(wiki_rankings), len(wiki_rankings[0]))
        self.assertEqual(final_copeland_score, wiki_copeland_scores)
        
    # https://courses.lumenlearning.com/waymakermath4libarts/chapter/copelands-method/
    # Only the first part, without D deleted.
    def test_wiki(self):
        example_rankings = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],
                           [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                           [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3],
                           [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]]
        example_pairwise_scores = [10, 6, 16, 15, 5, 9]
        example_copeland_scores = [1.5, 1.5, 2, 1]

        example_score_list = ic.pairwiseScoreCalcListFull(example_rankings, len(example_rankings), len(example_rankings[0]))
        self.assertEqual(example_score_list, example_pairwise_scores)
        final_copeland_score = ic.copelandScoreFull(example_score_list, 4, 20)
        self.assertEqual(final_copeland_score, example_copeland_scores)
    

if __name__ == '__main__':
    unittest.main()