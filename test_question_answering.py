from nltk.tokenize import word_tokenize, sent_tokenize
from question_processing import wh_bin
import math
import re


def vector_model(doc1, doc2):
    doc1_list = word_tokenize(doc1)
    doc2_list = word_tokenize(doc2)
    model_list = doc1_list + doc2_list
    model_words = set(model_list)
    words_dic ={}
    for item in model_words:
        words_dic[item] = [doc1_list.count(item), doc2_list.count(item)]
    d1 = []
    d2 = []
    for keys in words_dic:
        d1.append(words_dic[keys][0])
        d2.append(words_dic[keys][1])
    return d1, d2


def cosine_similarity(x, y):
    x_dot_y = 0
    x_sq = 0
    y_sq = 0
    for i in range(len(x)):
        x_dot_y = x_dot_y + x[i]*y[i]
        x_sq = x_sq + x[i]**2
        y_sq = y_sq + y[i]**2
    cos_theta = x_dot_y/(((x_sq)**(1/2))*((y_sq)**(1/2)))
    theta = math.acos(cos_theta)
    return math.degrees(theta)


def print_ans(filename, question):
    f = open(filename, 'r')
    text_file = ''
    for line in f:
        text_file = text_file + line
    sentences = sent_tokenize(text_file)
#print(wh_bin('what can lead to depression'))
#print(wh_bin('Do you want to stay in bed?'))
    wh, no, yes = wh_bin(question)
    theta_list = []
    theta_min_index = 0
    theta_min = 360
    for i in range(len(sentences)):
        pattern = re.compile('[h|w*]')
        if pattern.match(question):
            d1, d2 = vector_model(wh,sentences[i])
            c = cosine_similarity(d1,d2)
            theta_list.append(c)
            if c < theta_min:
                theta_min = c
                theta_min_index = i
        else:
            d1, d2 = vector_model(no, sentences[i])
            c = cosine_similarity(d1, d2)
            theta_list.append(c)
            if c < theta_min:
                theta_min = c
                theta_min_index = i

    answer_wh_bin = sentences[theta_min_index]
    print(question)
    return answer_wh_bin


#running sample question answers
if __name__ == '__main__':
    print('These are the sample question answering results from four texts files-- train1.txt, train2.txt, train3.txt and train4.txt.\n##########################################################################################################################')
    print()
    print(print_ans('train2.txt', 'What can lead to depression?'))
    print()
    print(print_ans('train2.txt', 'Do you want to stay in bed?'))
    print()
    print(print_ans('train2.txt', 'What can take toll on your sex life?'))
    print()
    print(print_ans('train3.txt', 'What does this block outlines?'))
    print()
    print(print_ans('train1.txt', 'Who designs elevators?'))
    print()
    print(print_ans('train4.txt', 'How much is the annual salary of software developers?'))
    print()
    print(print_ans('train4.txt', 'How much is the annual salary of software developers?'))
    print()
    print(print_ans('train4.txt', 'Why are software developers needed?'))
    print()
    print(print_ans('train1.txt', 'Are mechanical engineers responsible for sensors?'))
    print()
    print(print_ans('train4.txt', 'why are software developers needed?'))
    print()
    print(print_ans('train3.txt', 'Are NLP tools open-source?'))
    print('###############################################################################################################################################')
    q = input('Enter a WH or a binary question: ')
    text_file = input('Enter a .txt file with the text related to the question:')
    print()
    print(print_ans(text_file, q))
