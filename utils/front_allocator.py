from fuzzywuzzy import fuzz

class TextMatcher:

    def __init__(self):
        self.question_bank = {
            "Q1": {
                1: "Parent/Caregiver or Resident",
                2: "Faith Based Organization Representative (Church/Faith Based groups, clubs, councils, associations, etc.)",
                3: "Private Sector Representative/Community Member (for profit, small business, private citizen, etc.)",
                4: "Community Organization/Partner (local service provider and non-profits)",
                5: "Educational Institution Faculty/Staff (school, local adult ed, schools, college and universities)",
                6: "Government Agency Employee",
                7: "Staff or Volunteer of Smart from the Start",
                8: "Local Politician/Government/Public Sector Representative (non-profit, government regulated, funding sources, etc.)",
            },

            "Q3": {
                1: "Male",
                2: "Female",
            },

            "Q4": {
                1: "Under 18",
                2: "18-24",
                3: "25-34",
                4: "35-44",
                5: "45-54",
                6: "55-64",
                7: "65 and over"
            },

            "Q5": {
                1: "American Indian or Alaska Native",
                2: "Asian",
                3: "Black or African American",
                4: "Native Hawaiian and Other Pacific Islander",
                5: "White",
                6: 'Multi-race (two or more of the previous)',
            },

            "Q6": {
                1: "Hispanic, Latino or Spanish Origins",
                2: "Not Hispanic, Latino or Spanish Origins"
            },

            "Q7": {
                1: "Grades 0-8",
                2: "Grades 9-12/Non-Graduate",
                3: "High School Graduate/Equivalency Diploma",
                4: "12th Grade + Some Post-Secondary",
                5: "2 or 4 years College Graduate",
                6: "Graduate of Other Post-Secondary School"
            },

            "Q8": {
                1: "Veteran",
                2: "Active Military",
                3: "N/A"
            }
        }

    def match_text(self, input_text):
        scores = []

        for question, answers in self.question_bank.items():
            for id, answer_text in answers.items():
                score = fuzz.partial_ratio(input_text, answer_text)
                scores.append((question, score))

        # Sort scores in descending order (higher score means better match) and return the first element
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        return scores[0][0]

question_bank = {
    "Q1": {
        1: "Parent/Caregiver or Resident",
        2: "Faith Based Organization Representative (Church/Faith Based groups, clubs, councils, associations, etc.)",
        3: "Private Sector Representative/Community Member (for profit, small business, private citizen, etc.)",
        4: "Community Organization/Partner (local service provider and non-profits)",
        5: "Educational Institution Faculty/Staff (school, local adult ed, schools, college and universities)",
        6: "Government Agency Employee",
        7: "Staff or Volunteer of Smart from the Start",
        8: "Local Politician/Government/Public Sector Representative (non-profit, government regulated, funding sources, etc.)",
    },

    "Q3": {
        1: "Male",
        2: "Female",
        3: "Other"
    },

    "Q4": {
        1: "Under 18",
        2: "18-24",
        3: "25-34",
        4: "35-44",
        5: "45-54",
        6: "55-64",
        7: "65 and over"
    },

    "Q5": {
        1: "American Indian or Alaska Native",
        2: "Asian",
        3: "Black or African American",
        4: "Native Hawaiian and Other Pacific Islander",
        5: "White",
        6: 'Multi-race (two or more of the previous)',
        7: "Other"
    },

    "Q6": {
        1: "Hispanic, Latino or Spanish Origins",
        2: "Not Hispanic, Latino or Spanish Origins"
    },

    "Q7": {
        1: "Grades 0-8",
        2: "Grades 9-12/Non-Graduate",
        3: "High School Graduate/Equivalency Diploma",
        4: "12th Grade + Some Post-Secondary",
        5: "2 or 4 years College Graduate",
        6: "Graduate of Other Post-Secondary School"
    },

    "Q8": {
        1: "Veteran",
        2: "Active Military",
        3: "N/A"
    }
}

matcher = TextMatcher()

input_text = 'hispanic'
matched_question = matcher.match_text(input_text)

print('Matched question:', matched_question)
