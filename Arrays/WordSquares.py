class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])

        results = []
        word_squares = []
        for word in words:
            # try with every word as the starting word
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):

        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        # find out all words that start with the given prefix
        for candidate in self.getWordsWithPrefix(prefix):
            # iterate row by row
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word