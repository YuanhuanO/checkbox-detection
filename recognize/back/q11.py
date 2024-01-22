from fuzzywuzzy import fuzz


class Q11:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "community focus on preventative healthcare",
            2: "Provide more education on maintaining personal hygiene",
            3: "more payment programs for adult dental and or hearing services",
            4: "vision assistance programs for adults",
            5: "Increasing the community's knowledge of available health resources",
            6: "emphasis on earl childhood nutrition education",
            7: "emphasis on reinforcing healthy eating , habits",
            8: "nutritional counseling (one on one and free)",
            9: "knowledge of available food resources",
            10: "assistance and resources for victims of domestic violence",
            11: "Other (please specify):"

        }
        self.selections_keys_pairs = {
            "community focus on preventative healthcare": 1,
            "Provide more education on maintaining personal hygiene": 2,
            "more payment programs for adult dental and or hearing services": 3,
            "vision assistance programs for adults": 4,
            "Increasing the community's knowledge of available health resources": 5,
            "emphasis on earl childhood nutrition education": 6,
            "emphasis on reinforcing healthy eating , habits": 7,
            "nutritional counseling (one on one and free)": 8,
            "knowledge of available food resources": 9,
            "assistance and resources for victims of domestic violence": 10,
            "Other (please specify):": 11
        }
        self.selections_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

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
            most_similar_sentence = self.find_most_similar_sentence(sentence, target_sentences)
            remove_key = self.selections_keys_pairs.get(most_similar_sentence, None)
            if remove_key in self.selections_set:
                self.selections_set.remove(remove_key)
        return self.selections_set

    def get_checked(self, input_sentences):
        res = [0] * 11
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res
