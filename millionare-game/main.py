questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which language is primarily used for web development?", "Python", "Java", "HTML", "C++", 3],
    ["Who wrote the play 'Romeo and Juliet'?", "Leo Tolstoy", "William Shakespeare", "Charles Dickens", "Mark Twain", 2],
    ["What gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    ["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "India", "Japan", 4],
    ["How many continents are there on Earth?", "5", "6", "7", "8", 3],
    ["What is the boiling point of water at sea level?", "100°C", "90°C", "80°C", "120°C", 1]
]

prizes = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000]
i=0



for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Check whether the answer is correct or not 
    a = int(input("Enter your asnwer: 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("Correct answer")
    else:
        print(f"You loose, the correct answer was {question[5]}")
        print("Better luck next time")
        break
    print(f"You won {prizes[i]}")
    i++
