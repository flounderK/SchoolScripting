# import argparse
from string import punctuation
from re import sub
def find_words(file, *wordlist):

    words =list()
    with open(str(file), "r") as f:
        for word in sub('['+sub("'","",punctuation)+']'," ", f.read()).split():
            words.append(word.strip(punctuation).lower())

    common=set(words) & set({*wordlist})
    return common

# parser=argparse.ArgumentParser()
# parser.add_argument("-h","--help",
#                     "Finds matching words between the ones you" +
#                     "provide and the file you provide")
# parser.add_argument("-f","--file",
#                     help="The file you are searching", required=True)
# parser.add_argument("-w","--wordlist",
#                     help="List of words you would like to search the "+
#                     "document for, comma separated strings",required=True)
# args = parser.parse_args()
# find_words(file=args.file, wordlist=args.wordlist)
