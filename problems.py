import re

def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: True or False
    """
    pattern = r'[1-7][0-9]{2}\.[a-zA-Z]{1,10}[0-9]*@(shield\.gov|starkindustries\.com)'

    if re.fullmatch(pattern, searchstring):
        return "valid"
    else:
        return "invalid"


def problem2(searchstring):
    """
    Extract author and book.

    :param searchstring: string
    :return: tuple
    """
    pattern = r'([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)?)\s+wrote\s+((?:[A-Z0-9][a-zA-Z0-9]*\s?){1,3}|books)'

    match = re.search(pattern, searchstring)

    if match:
        author = match.group(1).strip()
        book_title = match.group(2).strip()
        return (author, book_title)
    else:
        return ("nohero", "noname")

def problem3(searchstring):
    """
    Replace Boy/Girl or boy/girl with Man/Woman.

    :param searchstring: string
    :return: string
    """
    def replace(match):
        name = match.group(1)
        gender = match.group(2)

        if gender.lower() == 'boy':
            return f"{name} Man"
        elif gender.lower() == 'girl':
            return f"{name} Woman"
        return match.group(0)
    
    pattern = r'([A-Z][a-zA-Z]*)\s+(Boy|Girl|boy|girl)'

    end = re.sub(pattern, replace, searchstring)

    if end == searchstring:
        return "nomatch"
    
    return end


if __name__ == '__main__':

    print("\nProblem 1:")
    testcase11 = '123.iamironman@starkindustries.com'
    print("Student answer: ",problem1(testcase11),"\tAnswer correct?", problem1(testcase11) == 'valid')

    testcase12 = '250.Srogers1776@starkindustries.com'
    print("Student answer: ",problem1(testcase12),"\tAnswer correct?", problem1(testcase12) == 'valid')

    testcase13 = '100.nickfury@shield.gov'
    print("Student answer: ",problem1(testcase13),"\tAnswer correct?", problem1(testcase13) == 'valid')

    testcase14 = '144.venom@starkindustries.comasdf'
    print("Student answer: ",problem1(testcase14),"\tAnswer correct?", problem1(testcase14) == 'invalid')

    testcase15 = '942.hyperion@starkindustries.com'
    print("Student answer: ",problem1(testcase15),"\tAnswer correct?", problem1(testcase15) == 'invalid')

    testcase16 = '567.greengoblin@shield.gov'
    print("Student answer: ",problem1(testcase16),"\tAnswer correct?", problem1(testcase16) == 'invalid')

    testcase17 = '324drdoom324@starkindustries.com'
    print("Student answer: ",problem1(testcase17),"\tAnswer correct?", problem1(testcase17) == 'invalid')

    testcase18 = '765.Hosborn*876@shield.gov'
    print("Student answer: ",problem1(testcase18),"\tAnswer correct?", problem1(testcase18) == 'invalid')

    testcase19 = '234.vulture@shield.com'
    print("Student answer: ",problem1(testcase19),"\tAnswer correct?", problem1(testcase19) == 'invalid')


    print("\nProblem 2:")
    testcase21 = "George Orwell wrote 1984"
    print("Student answer: ",problem2(testcase21),"\tAnswer correct?", problem2(testcase21) == ("George Orwell","1984"))

    testcase22 = "In the 1930s, a Mystery writer wrote Mary Westmacotts. Later it was found that Agatha Christie wrote The Westmacott Novels"
    print("Student answer: ",problem2(testcase22),"\tAnswer correct?", problem2(testcase22) == ("Agatha Christie", "The Westmacott Novels"))

    testcase23 = "Roxette wrote books"
    print("Student answer: ", problem2(testcase23), "\tAnswer correct?", problem2(testcase23) == ("Roxette", "books"))

    testcase24 = "Erin Morgenstern wrote The Starless Sea Book and The Night Circus"
    print("Student answer: ",problem2(testcase24),"\tAnswer correct?", problem2(testcase24) == ("Erin Morgenstern", "The Starless Sea"))

    testcase25 = "Haruki Murakami wrote 1Q84"
    print("Student answer: ",problem2(testcase25),"\tAnswer correct?", problem2(testcase25) == ("Haruki Murakami", "1Q84"))

    testcase26 = "Khaled Hosseini wrote sad books"
    print("Student answer: ",problem2(testcase26),"\tAnswer correct?", problem2(testcase26) == ("nohero", "noname"))

    testcase27 = "Haruki Murakami wrote Norwegian Wood"
    print("Student answer: ",problem2(testcase27),"\tAnswer correct?", problem2(testcase27) == ("Haruki Murakami", "Norwegian Wood"))


    print("\nProblem 3:")
    testcase31 = 'Spider Boy, I need help!'
    print("Student answer: ",problem3(testcase31),"\tAnswer correct?", problem3(testcase31) == "Spider Man, I need help!")

    testcase32 = 'There is a boy trapped in a burning building Iron Boy'
    print("Student answer: ",problem3(testcase32),"\tAnswer correct?", problem3(testcase32) == "There is a boy trapped in a burning building Iron Man")

    testcase33 = 'Spider Girl, I need help!'
    print("Student answer: ",problem3(testcase33),"\tAnswer correct?", problem3(testcase33) == "Spider Woman, I need help!")

    testcase34 = 'The Invisible girl is a member of the Fantastic Four'
    print("Student answer: ",problem3(testcase34),"\tAnswer correct?", problem3(testcase34) == "The Invisible Woman is a member of the Fantastic Four")

    testcase35 = 'There is a boy that needs to be saved from the alien!'
    print("Student answer: ",problem3(testcase35),"\tAnswer correct?", problem3(testcase35) == "nomatch")
