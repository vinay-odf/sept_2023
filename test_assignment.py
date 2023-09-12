def word_freq_count(sentence):
    # Using split function divide the sentence into a list by identifying space between words.

    word_list = sentence.split(' ')

    words = {}
    if word_list==['']:
        return {}
    for word in word_list:
        # count function returns number of indetical words present in the list

        words[word] = word_list.count(word)

    return words

def test_function():

    assert word_freq_count(  "The quick brown fox jumps over the lazy dog.") == {"The": 1, "quick": 1, "brown": 1,
                                                                               "fox": 1, "jumps": 1, "over": 1,
                                                                               "the": 1, "lazy": 1, "dog.": 1}

    assert word_freq_count(  "This is a test. This is only a test.") ==  {"This": 2, "is": 2, "a": 2,
                                                                          "test.": 2, "only": 1}


    assert word_freq_count(  "apple banana cherry banana cherry") == {"apple": 1, "banana": 2, "cherry": 2}


    assert word_freq_count( "")  == {}


    assert word_freq_count( "q") == {'q': 1}

    assert word_freq_count( "Testing the function" ) == {"Testing": 1, "the": 1 ,"function": 1}

    assert word_freq_count( "Hello, Hello, World!" ) ==  {"Hello,": 2, "World!": 1}

    assert word_freq_count("My name is Rishi Babu. Call me Rishi.") == {"My": 1, "name": 1, "is": 1, "Rishi": 1,
                                                                        "Rishi.": 1,"Babu.": 1,'Call':1,'me': 1}

    assert word_freq_count("Hi") == {"Hi": 1 }

    assert word_freq_count("Super ra Bittu") =={ 'Super':1, "ra": 1 , "Bittu":1}