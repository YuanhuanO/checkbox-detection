
from utils import detect_back,warpper
from recognize.back.q9 import Q9
from recognize.back.q10 import Q10
from recognize.back.q11 import Q11
from recognize.back.q12 import Q12
from recognize.back.q13 import Q13
from recognize.back.q14 import Q14
from recognize.back.q15 import Q15
from recognize.back.q16 import Q16
from recognize.back.q17 import Q17
import pandas as pd
if __name__ == "__main__":
    columns = [f'Person{i + 1}' for i in range(16)]
    columns = ['Ques', 'Answer'] + columns
    df = pd.DataFrame(columns=columns)

    all_questions = ['Q9','Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17'] 
    all_answers = {question: [] for question in all_questions}
    for i in range(16):  
        input_file_path = f"./images/Philly2_1/page_{2 * i + 1}.png"
        output_file_path = f"./output/philly2_1/marked_image_{2 * i + 1}.png"
        
        Q9_res, Q10_res, Q11_res, Q12_res, Q13_res, Q14_res, Q15_res, Q16_res, Q17_res = detect_back.get_detected_sentences(input_file_path, output_file_path)
        q9 = Q9()
        q10 = Q10()
        q11 = Q11()
        q12 = Q12()
        q13 = Q13()
        q14 = Q14()
        q15 = Q15()
        q16 = Q16()
        q17 = Q17()
        questions_answers = [q9.get_checked(Q9_res), q10.get_checked(Q10_res), q11.get_checked(Q11_res), q12.get_checked(Q12_res), q13.get_checked(Q13_res), q14.get_checked(Q14_res), q15.get_checked(Q15_res), q16.get_checked(Q16_res), q17.get_checked(Q17_res)]
        for question, answers in zip(all_questions, questions_answers):
            all_answers[question].append(answers)
    for q_number, q_answers in all_answers.items():
        max_answers = max(len(person_answers) for person_answers in q_answers)  
        for answer_idx in range(max_answers):
            row = {
                'Ques': q_number if answer_idx == 0 else '',
                'Answer': answer_idx + 1 if answer_idx < len(q_answers[0]) else ''
            }
            for person_idx, person_answers in enumerate(q_answers):
                row[f'Person{person_idx + 1}'] = person_answers[answer_idx] if answer_idx < len(person_answers) else ''
            df = df.append(row, ignore_index=True)
  
    csv_file_path = "./result/result_back_philly_new.csv"
    df.to_csv(csv_file_path, index=False)
# if __name__ == "__main__":
#     columns = [f'Person{i + 1}' for i in range(33)]
#     columns = ['Ques', 'Answer'] + columns
#     df = pd.DataFrame(columns=columns)

#     all_questions = ['Q9','Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17'] 
#     all_answers = {question: [] for question in all_questions}
#     for i in range(39):  
#         input_file_path = f"./images/Philly2/page_{2 * i + 1}.png"
#         output_file_path = f"./output/philly2/marked_image_{2 * i + 1}.png"
        
#         Q9_res, Q10_res, Q11_res, Q12_res, Q13_res, Q14_res, Q15_res, Q16_res, Q17_res = detect_back.get_detected_sentences(input_file_path, output_file_path)
#         q9 = Q9()
#         q10 = Q10()
#         q11 = Q11()
#         q12 = Q12()
#         q13 = Q13()
#         q14 = Q14()
#         q15 = Q15()
#         q16 = Q16()
#         q17 = Q17()
#         questions_answers = [q9.get_checked(Q9_res), q10.get_checked(Q10_res), q11.get_checked(Q11_res), q12.get_checked(Q12_res), q13.get_checked(Q13_res), q14.get_checked(Q14_res), q15.get_checked(Q15_res), q16.get_checked(Q16_res), q17.get_checked(Q17_res)]
#         for question, answers in zip(all_questions, questions_answers):
#             all_answers[question].append(answers)
#     # for i in range(25, 33):  
#     #     input_file_path = f"./images/Atlanta/page_{2 * i + 1}.png"
#     #     output_file_path = f"./output/atlanta/marked_image_{2 * i + 1}.png"
        
#     #     Q9_res, Q10_res, Q11_res, Q12_res, Q13_res, Q14_res, Q15_res, Q16_res, Q17_res = detect_back.get_detected_sentences_50(input_file_path, output_file_path)
#     #     q9 = Q9()
#     #     q10 = Q10()
#     #     q11 = Q11()
#     #     q12 = Q12()
#     #     q13 = Q13()
#     #     q14 = Q14()
#     #     q15 = Q15()
#     #     q16 = Q16()
#     #     q17 = Q17()
#     #     questions_answers = [q9.get_checked(Q9_res), q10.get_checked(Q10_res), q11.get_checked(Q11_res), q12.get_checked(Q12_res), q13.get_checked(Q13_res), q14.get_checked(Q14_res), q15.get_checked(Q15_res), q16.get_checked(Q16_res), q17.get_checked(Q17_res)]
#     #     for question, answers in zip(all_questions, questions_answers):
#     #         all_answers[question].append(answers)
#     for q_number, q_answers in all_answers.items():
#         max_answers = max(len(person_answers) for person_answers in q_answers)  
#         for answer_idx in range(max_answers):
#             row = {
#                 'Ques': q_number if answer_idx == 0 else '',
#                 'Answer': answer_idx + 1 if answer_idx < len(q_answers[0]) else ''
#             }
#             for person_idx, person_answers in enumerate(q_answers):
#                 row[f'Person{person_idx + 1}'] = person_answers[answer_idx] if answer_idx < len(person_answers) else ''
#             df = df.append(row, ignore_index=True)
  
#     csv_file_path = "./result/result_back_philly_new.csv"
#     df.to_csv(csv_file_path, index=False)
 