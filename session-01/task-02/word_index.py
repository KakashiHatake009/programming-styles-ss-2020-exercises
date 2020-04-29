import sys, string, re

# Word Index is a program that takes a plain text file as input and outputs all the words contained in it
# sorted alphabetically along with the page numbers on which they occur. The program assumes that a page is a
# sequence of 45 lines, each line has max 80 characters, and there is no hyphenation. Additionally, Word Index
# must ignore all words that occur more than 100 times.

# Global variables

LINES_PER_PAGE = 45
MAX_SIZE_LINE = 80
STOP_FREQUENCY_LIMIT = 100


def main():

    # set of stopwords with no duplication
    stop_words = []

    # List of words with page number and count
    word_list = []

    word_flag = False
    line_index = 0
    page_num = 0

    # Opening the file
    for line in open(sys.argv[1]):
        print("entry1")
        if line_index % LINES_PER_PAGE == 0:  # Checking to update pageNumber
            page_num += 1
        # Regex to match and word and put it into List
        wordsInLine = re.findall("\\w+", line.lower())

        for word in wordsInLine:  # Iterating over the List
            if word not in stop_words:  # if word is not in StopWord List:continue
                for data in word_list[:]:  # Checking if the word is already added to wordList
                    if word == data[0]:  # if word found
                        data[1] += 1  # incrementing the count
                        if page_num not in data[2]:
                            data[2].append(page_num)  # if the word is found in different page append it
                        if data[1] > STOP_FREQUENCY_LIMIT:  # if the word is repeated more than the threshold
                            stop_words.append(word)  # add it to stopWord set
                            word_list.remove(data)  # removing from the lost
                        word_flag = True
                        break
                if not word_flag:
                    index = 0
                    while index < len(word_list):
                        if word < word_list[index][0]:
                            word_list.insert(index, [word, 1, [page_num]])  # inserting in to list using index
                            break
                        index += 1
                    else:
                        word_list.insert(index, [word, 1, [page_num]])
            word_flag = False
        line_index += 1

    for output in word_list:  # iterating and printing the list
        print(output[0], '-', str(output[2])[1:-1])


if __name__ == '__main__':
    main()
