from fuzzywuzzy import fuzz


class Q16:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "Employment",
            2: "Education",
            3: "Income and Asset Building",
            4: "Housing",
            5: "Health",
            6: "Civic Engagement",
            7: "Support Services (supporting multiple domains)"
        }
        self.selections_keys_pairs = {
            "Employment": 1,
            "Education": 2,
            "Income and Asset Building": 3,
            "Housing": 4,
            "Health": 5,
            "Civic Engagement": 6,
            "Support Services (supporting multiple domains)": 7
        }
        self.selections_set = set([1, 2, 3, 4, 5, 6, 7])

    def find_most_similar_sentence(self, sentence, sentence_list):
        max_similarity = 0
        most_similar_sentence = ""

        for s in sentence_list:
            similarity = fuzz.ratio(str(s), sentence)
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
        res = [0] * 7
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res
