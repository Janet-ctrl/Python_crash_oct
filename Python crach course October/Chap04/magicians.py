magicians = ['alice', 'david', 'carolina']

#code block
for magician in magicians:
	print(magician)
	print("_________")
	

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("------------------------------------")
print("Thank you everyone, that was a great magic show!")