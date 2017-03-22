import urllib

def read_text():
    quotes = open('/Users/John/Desktop/ipnd/ipnd-starter-code-master/stage_3/lesson_3.3_classes/c_profanity_editor/movie_quotes.txt')
    contents = quotes.read()
    print contents
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=QUERY' + text)
    output = connection.read()
#    print output
    connection.close()
    if 'true' in output:
        print "\nProfanity detected."
    elif 'false' in output:
        print "\nOccular patdown clean."
    else:
        print "\nCan't read doc."


read_text()
