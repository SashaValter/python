eng = {1: 'AEIOULNSTR',
       	2: 'DG',
       	3: 'BCMP',
       	4: 'FHVWY',
       	5: 'K',
       	8: 'JZ',
       	10: 'QZ'}
rus = {1: 'АЕИНОРСТ',
       	2: 'ВДКЛМПУ',
       	3: 'БГЁЬЫ',
       	4: 'ЙЯ',
       	5: 'ЖЗХЦЧ',
       	8: 'ЩШЭЮ',
       	10: 'ФЪ'}
N = (int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
word = input('Введите слово: ').upper()
if N == 1:
 	print('За это слово вы получаете', sum(
 		[k for i in word for k, v in eng.items() if i in v]), 'очков')
elif N == 0:
 	print('За это слово вы получаете', sum(
 		[k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
     print('Третьего не дано!')
