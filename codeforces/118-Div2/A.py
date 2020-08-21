my_word =input().lower()
new_word=''
for i in my_word:
	if i not in 'aoieuy':
		new_word = new_word+'.'+i		
	else:
		new_word = new_word+''
print(new_word)
