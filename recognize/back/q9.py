from fuzzywuzzy import fuzz


class Q9:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "parents involved in students' education",
            2: "Preschool activities for child(ren) to develop school readiness skills",
            3: "assessable counseling to prepare students for tech or college",
            4: "certificate/degree programs offered locally",
            5: "Affordable transportation options to and from school",
            6: "Affordable high quality childcare options for parent who would like to further their education",
            7: "Increasing the community's knowledge of available education resources",
            8: "please specify:",
        }
        self.selections_keys_pairs = {
            "parents involved in students' education": 1,
            "Preschool activities for child(ren) to develop school readiness skills": 2,
            "assessable counseling to prepare students for tech or college": 3,
            "certificate/degree programs offered locally": 4,
            "Affordable transportation options to and from school": 5,
            "Affordable high quality childcare options for parent who would like to further their education": 6,
            "Increasing the community's knowledge of available education resources": 7,
            "please specify:": 8,
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
