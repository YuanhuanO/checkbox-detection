from fuzzywuzzy import fuzz

class Q1:
    def __init__(self):
        self.keys_selections_pairs = {
            1: "Parent/Caregiver or Resident",
            2: "Faith Based Organization Representative (Church/Faith Based groups, clubs, councils, associations, etc.)",
            3: "Private Sector Representative/Community Member (for profit, small business, private citizen, etc.)",
            4: "Community Organization/Partner (local service provider and non-profits)",
            5: "Educational Institution Faculty/Staff (school, local adult ed, schools, college and universities)",
            6: "Government Agency Employee",
            7: "Staff or Volunteer of Smart from the Start",
            8: "Local Politician/Government/Public Sector Representative (non-profit, government regulated, funding sources, etc.)",
        }
        self.selections_keys_pairs = {
            "Parent/Caregiver or Resident": 1,
            "Faith Based Organization Representative (Church/Faith Based groups, clubs, councils, associations, etc.)": 2,
            "Private Sector Representative/Community Member (for profit, small business, private citizen, etc.)": 3,
            "Community Organization/Partner (local service provider and non-profits)": 4,
            "Educational Institution Faculty/Staff (school, local adult ed, schools, college and universities)": 5,
            "Government Agency Employee": 6,
            "Staff or Volunteer of Smart from the Start": 7,
            "Local Politician/Government/Public Sector Representative (non-profit, government regulated, funding sources, etc.)": 8,
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