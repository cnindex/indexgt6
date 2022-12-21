out = ""

with open('./post/test.md', 'r', encoding='UTF-8') as F:
	text = F.readlines()
	for i in text:
		out = out + i + '\n'

with open('./post/test.md', 'w', encoding='UTF-8') as F:
	print(out, file = F)
