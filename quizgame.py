#Python DSA Quiz

questions = ("1. You have a list of dragons sorted by age, but you need to sort them by wingspan. The list is large, and you want the most efficient sorting algorithm.",
             "2. The castle gate has 1,000 keys arranged randomly, and you need to find the one with the unique magical symbol.",
             "3. You are planning a delivery route for magical potions through several planets, where each path between planets has a specific travel cost.",
             "4. A wizard must select items from a treasure chest to maximize value without exceeding the chest's weight limit.",
             "5. You are analyzing two DNA sequences to find the longest common subsequence.")

options= (("A.Bubble Sort","B.Quick Sort","C.Merger Sort"),
          ("A.Binary Search","B.Linear Search","C.Hashing "),
          ("A.DFS","B.BFS","C.Dijkstra’s Algorithm"),
          ("A.Greedy Algorithm","B. Dynamic Programming (Knapsack)","C.Backtracking"),
          ("A.Dynamic Programming","B.Divide and Conquer","C.Sliding Window"))

answers = ("B","B","C","B","A")

userAnswer = []
i=0
score = 0

for question in questions:
    print('_________________________________________________________')
    print(question)
    for option in options[i]:
        print(option)
    userInput = input("Enter the answer as (A,B,C):").upper()
    userAnswer.append(userInput)
    if userInput==answers[i]:
        score += 1
        print("Correct Answer!!")
        print("__________________")
        print(f"Your current score:{score}")
    else:
        print("Incorrect >_<")
        print(f"Correct answer is : {answers[i]}")
    i +=1

print("____________________")
print("_______Results______")
total = score/len(questions) * 100
print(f"Your scored {total}%")
print("____________________")
