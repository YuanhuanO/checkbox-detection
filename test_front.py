
from utils import detect_front,detect_back, warpper,front_allocator
from recognize.front.q1 import Q1
from recognize.front.q3 import Q3
from recognize.front.q4 import Q4
from recognize.front.q5 import Q5
from recognize.front.q6 import Q6
from recognize.front.q7 import Q7
from recognize.front.q8 import Q8
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
    columns = [f'Person{i + 1}' for i in range(9)]
    columns = ['Ques', 'Answer'] + columns
    df = pd.DataFrame(columns=columns)

    all_questions = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'] 
    all_answers = {question: [] for question in all_questions}


    for i in range(1):  # loop from page 0 to 31
        input_file_path = f"./images/Philly2/page_0.png"
        output_file_path = f"./output/philly2/marked_image_0.png"
        
        Q1_res, Q3_res, Q4_res, Q5_res, Q6_res, Q7_res, Q8_res = detect_front.get_detected_sentences(input_file_path, output_file_path)
        q1 = Q1()
        q3 = Q3()
        q4 = Q4()
        q5 = Q5()
        q6 = Q6()
        q7 = Q7()
        q8 = Q8()
        questions_answers = [q1.get_checked(Q1_res), q3.get_checked(Q3_res), q4.get_checked(Q4_res), q5.get_checked(Q5_res), q6.get_checked(Q6_res), q7.get_checked(Q7_res), q8.get_checked(Q8_res)]
        for question, answers in zip(all_questions, questions_answers):
            all_answers[question].append(answers)
    for q_number, q_answers in all_answers.items():
        max_answers = max(len(person_answers) for person_answers in q_answers)  # 获取此问题的最大答案数量
        for answer_idx in range(max_answers):
            row = {
                'Ques': q_number if answer_idx == 0 else '',
                'Answer': answer_idx + 1 if answer_idx < len(q_answers[0]) else ''
            }
            for person_idx, person_answers in enumerate(q_answers):  
                row[f'Person{person_idx + 1}'] = person_answers[answer_idx] if answer_idx < len(person_answers) else ''
            df = df.append(row, ignore_index=True)
# if __name__ == "__main__":
#     columns = [f'Person{i + 1}' for i in range(1)]
#     columns = ['Ques', 'Answer'] + columns
#     df = pd.DataFrame(columns=columns)

#     all_questions = ['Q9','Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17'] 
#     all_answers = {question: [] for question in all_questions}
#     for i in range(1):  
#         # input_file_path = f"./images/Philly/page_3.png"
#         # output_file_path = f"./output/philly/marked_image3.png"
#         input_file_path = f"./images/Philly2/page_1.png"
#         output_file_path = f"./output/philly2/marked_image_1.png"
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


    csv_file_path = "./result/result_test.csv"
    df.to_csv(csv_file_path, index=False)
