list = [2200,2350,2600,2130,2190]
print("In Feb how many extra compare to January? ",list[1]-list[0])
print("Find out your total expense in first quarter (first three months) of the year.",list[0]+list[1]+list[2])
print("Find out if you spent exactly 2000 dollars in any month", 2000 in list)
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list", list.append(1980))
list[3]-=200
print("You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this",list)
