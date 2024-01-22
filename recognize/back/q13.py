from fuzzywuzzy import fuzz


class Q13:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "Anonymous and confidential budget counseling",
            2: "education on how to build assets",
            3: "Information on how to access free credit counseling",
            4: "Anonymous and confidential savings counseling",
            5: "access to low interest loans",
            6: "information on how to access financial resources",
            7: "Increasing the community's knowledge of available mainstream financial resources",
            8: "Other (please specify):"
        }
        self.selections_keys_pairs = {
            "Anonymous and confidential budget counseling": 1,
            "education on how to build assets": 2,
            "Information on how to access free credit counseling": 3,
            "Anonymous and confidential savings counseling": 4,
            "access to low interest loans": 5,
            "information on how to access financial resources": 6,
            "Increasing the community's knowledge of available mainstream financial resources": 7,
            "Other (please specify):": 8
        }
        self.selections_set = set([1, 2, 3, 4, 5, 6, 7, 8])

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
        res = [0] * 8
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res
