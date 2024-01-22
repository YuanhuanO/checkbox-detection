from fuzzywuzzy import fuzz


class Q12:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "monthly rental assistance programs",
            2: "Increased availability of security/utility deposit programs",
            3: "counseling resources for homeowners",
            4: "grants to make home ownership and home rehab affordable",
            5: "grants to provide services that reduce energy cost",
            6: "programs to provide free home repair",
            7: "income based rental housing for disabled and seniors",
            8: "community supports for homeless families",
            9: "Other (please specify):"

        }
        self.selections_keys_pairs = {
            "monthly rental assistance programs": 1,
            "Increased availability of security/utility deposit programs": 2,
            "counseling resources for homeowners": 3,
            "grants to make home ownership and home rehab affordable": 4,
            "grants to provide services that reduce energy cost": 5,
            "programs to provide free home repair": 6,
            "income based rental housing for disabled and seniors": 7,
            "community supports for homeless families": 8,
            "Other (please specify):": 9
        }
        self.selections_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

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
        res = [0] * 9
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res
