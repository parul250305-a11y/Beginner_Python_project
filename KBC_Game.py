questions = [
["What is the capital of India?" , "Mumbai" , "New Delhi", "Kolkata" ,"Chennai" , 2],

["Who is known as the Father of the Nation in India?" , "Jawaharlal Nehru" , "Subhas Chandra Bose", "Mahatma Gandhi" ,"Bhagat Singh" , 3],

["Which is the national animal of India?" , "Lion" , "Elephant", "Tiger" ,"Leopard" , 3],

["Which river is considered the holiest in India?" , "Yamuna" , "Brahmaputra", "Ganga" ,"Godavari" , 3],

["How many states are there in India (as of now)?" , "28" , "29", "30" ,"27" , 1],

["Which is the national sport of India (officially)?" , "Cricket" , "Hockey", "Kabaddi" ,"No official national sport" , 4],

["Who was the first Prime Minister of India?" , "Mahatma Gandhi" , "Sardar Patel", "Jawaharlal Nehru" ,"Rajendra Prasad" , 3],

["Which is the largest state in India by area?" , "Maharashtra" , "Rajasthan", "Madhya Pradesh" ,"Uttar Pradesh" , 2],

["Which Indian festival is known as the Festival of Lights?" , "Holi" , "Diwali", "Eid" ,"Pongal" , 2],

["Which is the national bird of India?" , "Peacock" , "Sparrow", "Parrot" ,"Eagle" , 1]
]

prize = [10000 , 20000 ,30000 ,40000 , 50000, 60000 , 70000 , 80000 ,90000 , 100000]
i = 0
for question in questions :
    print(question[0])
    print(f"a . {question[1]}")
    print(f"b . {question[2]}")
    print(f"c . {question[3]}")
    print(f"d . {question[4]}")

    checking = int(input("Enter ur answer :press 1 for a ,press 2 for b , press 3 for c , press 4 for d : "))
    if (question[5] == checking):
        print("hurra!! YOU WON ")
    else :
        print("YOU LOSS ! better luck next time")
        break    
    print(f"YOU WON  {prize[i]} DOLLARs")
    i += 1




































































































