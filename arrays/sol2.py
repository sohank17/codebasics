heros=['spider man','thor','hulk','iron man','captain america']

print("Length of the list",len(heros))
print("Add 'black panther' at the end of this list",heros.append("black panther"))
heros.pop()
heros.insert(3,"black panther")
print("You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'",heros)
heros[1:3]=["doctor strange"]
print("Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.", heros)
print("Sorted",sorted(heros))
