n = int(input())
sum_of_negatives = []
count_positives = []

for i in range(n):
    current_num = int(input())
    if current_num >= 0:
        count_positives.append(current_num)
    else:
        sum_of_negatives.append(current_num)

print(count_positives)
print(sum_of_negatives)
print(f"Count of positives: {len(count_positives)}\nSum of negatives: {sum(sum_of_negatives)}")

"""
3. List Statistics

On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:

· One with all the positives (including 0) numbers

· One with all the negatives numbers

Finally, print the following message:

"Count of positives: {count_positives}

Sum of negatives: {sum_of_negatives}"
"""