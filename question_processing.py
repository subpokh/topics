from tag_list import tags, tags_list


#returns probable answer words sequence
def wh_bin(question):
    tagged_wh = tags(question)
    ans_seq = ''
    bin_ans_seq_yes = ''
    bin_ans_seq_no = ''
    subject = ''
    verb = ''
    possessive = ''
    subject_ext = ''
    for i in range(len(tagged_wh)):
        if tagged_wh[i][1] in ['PRP$']:
            possessive = possessive + tagged_wh[i][0] + ' '
        if tagged_wh[i][1] in ['JJ']:
            subject_ext = subject_ext + tagged_wh[i][0] + ' '
        if tagged_wh[i][1] in ['NN', 'NNS', 'PRP']:
            subject = subject + tagged_wh[i][0] + ' '
        if tagged_wh[i][1] in ['VBZ', 'VBN', 'VBD', 'VB', 'VBG']:
            verb = verb + tagged_wh[i][0] + ' '
    ans_seq = ans_seq + subject_ext + possessive + subject + verb
    bin_ans_seq_no = bin_ans_seq_no + 'no ' + subject + 'not ' + verb
    bin_ans_seq_yes = subject + verb
    return ans_seq, bin_ans_seq_no, bin_ans_seq_yes
