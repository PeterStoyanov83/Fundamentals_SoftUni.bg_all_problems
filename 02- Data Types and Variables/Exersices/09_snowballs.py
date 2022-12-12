num_of_balls = int(input())
best_snowball_quality = 0
best_snowball_data = ""

for _ in range(num_of_balls):

    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight/time) ** quality

    if result > best_snowball_quality:
        best_snowball_quality = result
        best_snowball_data = f"{weight} : {time} = {int(result)} ({quality})"

print(best_snowball_data)



"""
9. *Snowballs

Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes 
the best snowballs. They have decided to involve you in their fray by writing a program that calculates snowball data 
and outputs the best snowball value.

You will receive N – an integer, the number of snowballs being made by Tony and Andi. On the following lines, 
you will receive 3 inputs for each snowball:
· The weight of the snowball (integer).
· The time needed for the snowball to get to its target (integer).
· The quality of the snowball (integer).
For each snowball, you must calculate its value by the following formula:
(snowball_weight / snowball_time) ** snowball_quality
In the end, you must print the highest calculated value of a snowball.

Input
· On the first input line, you will receive N – the number of snowballs.
· On the next N*3 input lines, you will be receiving data about each snowball.

Output
· You need to print the highest calculated snowball's value in the format: 
"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

Constraints
· The number of snowballs (N) will be an integer in range [0, 100].
· The weight is an integer in the range [0, 1000].
· The time is an integer in the range [1, 500].
· The quality is an integer in the range [0, 100].

Examples

Input       Output
2
10
2
3           10 : 2 = 125 (3)
5 
5 
5
________________________________
3
10
5
7
16
4
2
20
2
2           10 : 5 = 128 (7)

"""