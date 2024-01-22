from fuzzywuzzy import fuzz
class Q6:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "Hispanic, Latino or Spanish Origins",
            2: "Not Hispanic, Latino or Spanish Origins"
        }
        self.selections_keys_pairs = {
            "Hispanic, Latino or Spanish Origins": 1,
            "Not Hispanic, Latino or Spanish Origins": 2
        }
        self.selections_set = set([1, 2])

    def find_most_similar_sentence(self, sentence, sentence_list):
        max_similarity = 0
        most_similar_sentence = ""

        for s in sentence_list:
            similarity = fuzz.ratio(s, sentence)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_sentence = s

        return most_similar_sentence

    def get_checked_sentences(self, input_sentences, target_sentences):
        for sentence in input_sentences:
            remove_key = self.selections_keys_pairs.get(self.find_most_similar_sentence(sentence, target_sentences), None)
            if remove_key in self.selections_set:
                self.selections_set.remove(remove_key)
        return self.selections_set

    def get_checked(self, input_sentences):
        res = [0] * 2
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res