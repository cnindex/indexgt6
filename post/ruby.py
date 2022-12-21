def main(name = ''):
	filename = name
	dic = {
		'三倍装填': 'Reload Three Times',
		'重启': '起床',
		'幻想杀手': 'Imagine Breaker',
		'必要恶之教会': 'Necessarius',
		'蔷薇十字': 'Rosicrucianism',
		'警备员': 'Anti-Skill',
		'致幻剂': 'LSD',
		'超能力': 'Level 5',
	}

	out = ""

	with open(filename, 'r', encoding='UTF-8') as F:
		text = F.readlines()
		for i in text:
			new = i
			for word in dic:
				new = new.replace("%s(%s)"%(word, dic[word]), 
					"<ruby>%s<rp>(</rp><rt>%s</rt><rp>)</rp></ruby>"%(word, dic[word]))
			out = out + new


	with open(filename, 'w', encoding='UTF-8') as F:
		print(out, file = F)

namelist = ['0.md', '1.md', '2.md', '2.5.md', '3.md', '3.5.md', '4.md', '5.md', '6.md', '7.md']

for i in namelist:
	main('post/' + i)
	print(i, 'is finish!')
