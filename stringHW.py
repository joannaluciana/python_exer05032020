# word = input("Enter first string: ")
# word2 = input("Enter second string: ")

def str_check(word,word2):
    
    if word[1:] == word2:
            return True
    else: return False        
           
# print(str_check(word, word2))




def test_str_check():
    assert str_check('asia', 'sia') == True

    # failure test
    assert str_check('kiciakocia','kkicikici')==False  


     



