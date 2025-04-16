# Redirecting input and output

# echo "word" >> file.txt -> add word to file
# file1.txt > file2.txt -> will copy (replace) content from one to the other file
# file1.txt >> file2.txt -> will copy (add) content from one to the other file

# cat file.txt | wc -> command outputs the number of lines, words, and characters in file
# sort file.txt -> sorts and displays content
# uniq file.txt ->  filters out adjacent, duplicate lines in a file and displays content

# grep word file.txt -> "global regular expression print", searches files for lines that match a pattern and then returns the results (case sensitive)
# grep -i word file.txt -> not case sensitive
# grep -R word /folder -> searches all files in a directory and outputs filenames and lines containing matched results

# sed 's/search_word/replace_word/' file.txt -> "stream editor", accepts standard input and modifies it based on an expression, & displays output data (“find and replace”)
# sed 's/search_word/replace_word/g' file.txt -> replaces ALL search_words
# sed -i 's/search_word/replace_word/g' file.txt -> replaces ALL search_words and amends file (not only display)
