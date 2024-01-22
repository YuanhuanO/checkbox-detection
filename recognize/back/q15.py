from fuzzywuzzy import fuzz


class Q15:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "Child Support",
            2: "Legal",
            3: "Youth",
            4: "Meal Programs",
            5: "Life Skill Programs",
            6: "Substance Abuse Resources",
            7: "Emotional Abuse",
            8: "Sexual Abuse",
            9: "Physical Abuse",
            10: "Transportation",
            11: "Other (please specify):"
        }
        self.selections_keys_pairs = {
            "Child Support": 1,
            "Legal ": 2,
            "Youth ": 3,
            "Meal Programs": 4,
            "Life Skills Programs and ": 5,
            "Substance Abuse Resources": 6,
            "Emotional Abuse ": 7,
            "Sexual Abuse ": 8,
            "Physical Abuse ": 9,
            "Transportation ": 10,
            "Other (please specify):": 11
        }
        self.selections_set = set([i for i in range(1, 12)])

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
        res = [0] * 11
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res
