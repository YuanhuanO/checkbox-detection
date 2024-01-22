from fuzzywuzzy import fuzz


class Q17:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "Allergies",
            2: "Arthritis",
            3: "Asthma",
            4: "Cancer",
            5: "Dental disease",
            6: "Depression/MH issues",
            7: "Diabetes",
            8: "Drug/substance use",
            9: "High blood pressure",
            10: "HIV/AIDS",
            11: "Heart disease",
            12: "Obesity",
            13: "Smoking",
            14: "sips",
            14: "Thyroid disorder",
        }
        self.selections_keys_pairs = {
            "Allergies": 1,
            "Arthritis": 2,
            "Asthma": 3,
            "Cancer": 4,
            "Dental disease": 5,
            "Depression/MH issues": 6,
            "Diabetes": 7,
            "Drug/substance use": 8,
            "High blood pressure": 9,
            "HIV/AIDS": 10,
            "Heart disease": 11,
            "Obesity": 12,
            "Smoking": 13,
            "sips": 14,
            "Thyroid disorder": 15
        }
        self.selections_set = set([i for i in range(1, 16)])

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
            # remove_key = self.selections_keys_pairs.get(self.find_most_similar_sentence(sentence, target_sentences), None)
            most_similar_sentence = self.find_most_similar_sentence(sentence, target_sentences)
            remove_key = self.selections_keys_pairs.get(most_similar_sentence, None)
            # print(f"Input sentence: {sentence}")
            # print(f"Most similar sentence: {most_similar_sentence}")
            # print(f"Key to remove: {remove_key}")
            if remove_key in self.selections_set:
                self.selections_set.remove(remove_key)
        return self.selections_set

    def get_checked(self, input_sentences):
        res = [0] * 15
        selection_set = self.get_checked_sentences(input_sentences, list(self.selections_keys_pairs.keys()))

        for x in selection_set:
            res[x - 1] = 1

        return res + [0]
