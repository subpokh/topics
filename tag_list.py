import nltk

#returns list of tuples with as (tokens, tag)
def tags(text):
    tokenized_text = nltk.word_tokenize(text)
    tagged_list = nltk.pos_tag(tokenized_text)
    return tagged_list


#returns tags of a sentence in order
def tags_list(text):
    tuple_list = tags(text)
    tuples_l = []
    for i in range(len(tuple_list)):
        tuples_l.append(tuple_list[i][1])
    return tuples_l

