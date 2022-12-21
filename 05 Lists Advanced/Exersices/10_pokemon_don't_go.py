pokemons = [int(n) for n in input().split()]
sum_of_captures_pokemons = []


def capture_pokemons(index, pokemons):
    first_element = int(pokemons[0])
    last_element = int(pokemons[-1])
    if index < 0:
        sum_of_captures_pokemons.append(first_element)  # appends the first element
        del pokemons[0]                     # deletes element at current_index 0
        pokemons.insert(0, last_element)    # puts last element to current_index 0

    elif index > len(pokemons) - 1:
        sum_of_captures_pokemons.append(last_element)  # appends the last element
        del pokemons[-1]                    # deletes element at current_index -1
        pokemons.insert(len(pokemons), first_element)  # puts first element at current_index -1

    if 0 <= index < len(pokemons):
        if index == len(pokemons):
            sum_of_captures_pokemons.append(pokemons[index - 1])
            del pokemons[index - 1]
        else:
            sum_of_captures_pokemons.append(pokemons[index])
            del pokemons[index]

    for counter, number in enumerate(pokemons):
        if number <= sum_of_captures_pokemons[-1]:
            pokemons[counter] = number + sum_of_captures_pokemons[-1]
        elif number > sum_of_captures_pokemons[-1]:
            pokemons[counter] = number - sum_of_captures_pokemons[-1]


while len(pokemons) > 0:
    current_position = int(input())
    capture_pokemons(current_position, pokemons)

print(sum(sum_of_captures_pokemons))

"""
10. *Pokemon Don't Go

Ely likes to play Pokemon Go a lot. But Pokemon Go bankrupted… So the developers made Pokemon Don't Go out of
depression. And so Ely now plays Pokemon Don't Go. In Pokemon Don't Go, when you walk to a certain pokemon, those
closest to you naturally get further, and those further from you, get closer.

You will receive a sequence of integers, separated by spaces - the distances to the pokemon. Then you will begin
receiving integers, which will correspond to indexes in that sequence.When you receive an index, you must remove the
element at that index from the sequence (as if you've captured the pokemon).

· You must increase the value of all elements in the sequence which are less or equal to the removed element
with the value of the removed element.
· You must decrease the value of all elements in the sequence which are greater than the removed element with the
 value of the removed element.
        If the given index is less than 0, remove the first element of the sequence, and copy the last element to its place.
        If the given index is greater than the last index of the sequence, remove the last element from the sequence, and copy
        the first element to its place.
        The increasing and decreasing elements should also be done in these cases. The element whose value you should use is the removed element.

The program ends when the sequence has no elements (there are no pokemon left for Ely to catch).

Input
· On the first line of input, you will receive a sequence of integers, separated by spaces.
· On the next several lines, you will receive integers - the indexes.

Output
· When the program ends, you must print the summed value of all removed elements.

Constrains
· The input data will consist only of valid integers in the range [-2.147.483.648…2.147.483.647].

Examples

Inpu         Output

4 5 3
1
1
0           14

Comments:
The array is {4, 5, 3}. The index is 1. We remove 5, and we increase all the lower ones and decrease all
the higher ones. In this case, there are no higher than 5. The result is {9, 8}. The index is 1. So we remove
8 and decrease all the higher ones. The result is {1}. The index is 0. So we remove 1. There are no elements left,
so we print the sum of all removed elements. 5 + 8 + 1 = 14.

5 10 6 3 5
2
4
1
1
3
0
0 51

comments :
Step 1: {11, 4, 9, 11} Step 2: {22, 15, 20, 22} Step 3: {7, 5, 7} Step 4: {2, 2} Step 5: {4, 4} Step 6: {8}
Step 7: {} (empty). Result = 6 + 11 + 15 + 5 + 2 + 4 + 8 = 51.
"""