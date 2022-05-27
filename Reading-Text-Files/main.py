# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
filename = "./story.txt"
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        content= f.read()
        return content

def count_words():
    text = read_file_content(filename).lower()
    clean_strs = text.split()
    dict_words = {}

    for word in clean_strs:
        num_word = clean_strs.count(word)
        dict_words[word] = num_word
    
    return dict_words

print(count_words())

