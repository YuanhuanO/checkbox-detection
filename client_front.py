
from utils import detect_front,warpper
from recognize.front.q1 import Q1
from recognize.front.q3 import Q3
from recognize.front.q4 import Q4
from recognize.front.q5 import Q5
from recognize.front.q6 import Q6
from recognize.front.q7 import Q7
from recognize.front.q8 import Q8
import pandas as pd
if __name__ == "__main__":
    columns = [f'Person{i + 1}' for i in range(16)]
    columns = ['Ques', 'Answer'] + columns
    df = pd.DataFrame(columns=columns)

    all_questions = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'] 
    all_answers = {question: [] for question in all_questions}


    for i in range(15):  # loop from page 0 to 31
        input_file_path = f"./images/Philly2_1/page_{2 * i}.png"
        output_file_path = f"./output/philly2_1/marked_image_{2 * i}.png"
        
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
        max_answers = max(len(person_answers) for person_answers in q_answers)  
        for answer_idx in range(max_answers):
            row = {
                'Ques': q_number if answer_idx == 0 else '',
                'Answer': answer_idx + 1 if answer_idx < len(q_answers[0]) else ''
            }
            for person_idx, person_answers in enumerate(q_answers):
                row[f'Person{person_idx + 1}'] = person_answers[answer_idx] if answer_idx < len(person_answers) else ''
            df = df.append(row, ignore_index=True)


    csv_file_path = "./result/result_front_philly_new_1.csv"
    df.to_csv(csv_file_path, index=False)
    
# if __name__ == "__main__":
#     columns = [f'Person{i + 1}' for i in range(33)]
#     columns = ['Ques', 'Answer'] + columns
#     df = pd.DataFrame(columns=columns)

#     all_questions = ['Q1', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'] 
#     all_answers = {question: [] for question in all_questions}


#     for i in range(40):  # loop from page 0 to 50
#         input_file_path = f"./images/Philly2/page_{2 * i}.png"
#         output_file_path = f"./output/philly2/marked_image_{2 * i}.png"
        
#         Q1_res, Q3_res, Q4_res, Q5_res, Q6_res, Q7_res, Q8_res = detect_front.get_detected_sentences(input_file_path, output_file_path)
#         q1 = Q1()
#         q3 = Q3()
#         q4 = Q4()
#         q5 = Q5()
#         q6 = Q6()
#         q7 = Q7()
#         q8 = Q8()
#         questions_answers = [q1.get_checked(Q1_res), q3.get_checked(Q3_res), q4.get_checked(Q4_res), q5.get_checked(Q5_res), q6.get_checked(Q6_res), q7.get_checked(Q7_res), q8.get_checked(Q8_res)]
#         for question, answers in zip(all_questions, questions_answers):
#             all_answers[question].append(answers)
#     # for i in range(25, 33):  # loop from page 50 to 65
#     #     input_file_path = f"./images/Atlanta/page_{2 * i}.png"
#     #     output_file_path = f"./output/atlanta/marked_image_{2 * i}.png"
        
#     #     Q1_res, Q3_res, Q4_res, Q5_res, Q6_res, Q7_res, Q8_res = detect_front.get_detected_sentences_after_50(input_file_path, output_file_path)
#     #     q1 = Q1()
#     #     q3 = Q3()
#     #     q4 = Q4()
#     #     q5 = Q5()
#     #     q6 = Q6()
#     #     q7 = Q7()
#     #     q8 = Q8()
#     #     questions_answers = [q1.get_checked(Q1_res), q3.get_checked(Q3_res), q4.get_checked(Q4_res), q5.get_checked(Q5_res), q6.get_checked(Q6_res), q7.get_checked(Q7_res), q8.get_checked(Q8_res)]
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
  
#     csv_file_path = "./result/result_front_philly_new.csv"
#     df.to_csv(csv_file_path, index=False)