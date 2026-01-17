name = "Python"    # LEN = LENGHTH
print(len(name))
line = "i will become the full stack developer insha allah"
print(len(line))

word = "python"     # UPPER = UPPERCASEING
uppercase_word = word.upper()
print(uppercase_word)

word = "PYTHON"    # LOWER = LOWERCASEING
lowercase_word = word.lower()
print(lowercase_word)

phrase = "   hello world   "   # STRIP = REMOVING WHITESPACES
stripped_phrase = phrase.strip()
print(stripped_phrase)

line = "welcome to the world of java programming"   # REPLACE = REPLACING A WORD
second_line = line.replace("java", "python") 
print(second_line)

text = "i love coding" # FIND = FINDING A WORD
index = text.find("coding")
print(index)

statement = "i love python programming" # SPLIT = SPLITTING A SENTENCE INTO WORDS 
words = statement.split()
print(words) 

quote = ''' Steve Jobs highlighted that those "crazy enough" to think they can change the world
are ultimately the ones who do. '''
line = quote.split()         # SPLITTING A SENTENCE INTO WORDS
print(line)

line = "python is best for beginners"
print(line.title())

def calc_sum(a, b):    # def function
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)
calc_sum(20, 30)
calc_sum(100, 200)
calc_sum(7, 3)
