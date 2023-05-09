def capitalized_str(sentence):
    
    if sentence != "":
        if sentence[0] >= chr(97) and sentence[0] <= chr(122):
            new_sentence = chr(ord(sentence[0])-32)
        else:
            new_sentence = sentence[0]
            
        if sentence[1] != " ":
            
            if sentence[1] >= chr(97) and sentence[1] <= chr(122):
                new_sentence += sentence[1]
            else:
                new_sentence += chr(ord(sentence[1])+32)
           
        for i in range(2,len(sentence)):
            
                if sentence[i - 1] == " " and sentence[i] == "i" and sentence[i + 1] == " ":
                    new_sentence += "I"
                elif sentence[i-2] == '.' or sentence[i-2] == '!' or sentence[i-2] == '?':
                    new_sentence += chr(ord(sentence[i]) - 32)

                else:
                    new_sentence += sentence[i]
    
        return new_sentence 
    else:
        print("Please enter a valid string as input.")
    

print(
    capitalized_str(
        "my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much."
    )
)

