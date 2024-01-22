from fuzzywuzzy import fuzz


class Q10:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "jobs with better pay and benefits",
            2: "training for the types of jobs available in the area",
            3: "Affordable transportation to and from job",
            4: "Affordable childcare during work hours",
            5: "Early reinforcement of the values of entering the workforce",
            6: "Increasing the community's knowledge of available employment resources",
            7: "Improve the workforce readiness skills of peoble who are able to work",
            8: "Other (please specify):",
        }
        self.selections_keys_pairs = {
            "jobs with better pay and benefits": 1,
            "training for the types of jobs available in the area": 2,
            "Affordable transportation to and from job": 3,
            "Affordable childcare during work hours": 4,
            "Early reinforcement of the values of entering the workforce": 5,
            "Increasing the community's knowledge of available employment resources": 6,
            "Improve the workforce readiness skills of peoble who are able to work": 7,
            "Other (please specify):": 8,
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
