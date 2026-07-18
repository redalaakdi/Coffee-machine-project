#method 1 original
student_scores = [180, 124, 165, 173, 189, 169, 146]
print(max(student_scores))


#method 2 classic
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

