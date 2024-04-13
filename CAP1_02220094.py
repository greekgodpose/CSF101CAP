################################
# Sonam Zangmo
# 1EE
# 02220094
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# Put your number here: 4
################################
# Read the input.txt file
f = open('input_4_cap1.txt', 'r')
print(f.read())
f.close()

def read_input():
    my_file = open('input_4_cap1.txt','r')
    return my_file

def calculate_score(point):
    score = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
    total_score = 0
    for line in point:
        key = line.strip()
        value_in_dict = score.get(key, None)
        if value_in_dict is not None:
            total_score += value_in_dict
    print("Total score :", total_score)

read_input()
calculate_score(read_input())