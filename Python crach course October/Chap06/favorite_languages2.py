favorite_languages = {
'jen': ['python','ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python','haskell'],
}

for name, langauges in favorite_languages.items():
	print(f"\n{name.title()}'s favorite langauges are:")
	for langauge in langauges:
		print(f"\t{langauge.title()}")