# -*- coding: utf-8 -*-
# Kaloyan Krastev Krastev, kaloyansen@gmail.com
###########################################################

"""
Kalyan KRASTEV
little private library

"""

__version__ = '210227'
__url__ = 'http://www.apache.org'
__license__ = 'apache'


import sys


class num2mot:
	""" traduir un numéro positif de l'arabe vers le français """
	debug = False
	numax = 1e15

	def __init__(self, arg1=0):
		self.num = '{}'.format(arg1)

	def __str__(self):
		strarr = self.num.split('.')
		intarr = []
		for arr in strarr:
			if arr.isdigit():
				intarr.append(int(arr))
			else:
				print('attention ' + arr + ' is not a number')
				intarr.append(0)
		mot = ''
		for arr in intarr:
			if mot != '':
				mot += ' point '
			mot += self.int2mot(arr)
		return mot

	def setdebug(self, deb=True):
		self.debug = deb

	def int2mot(self, i):# whole numbers only
		self.mot = ''
		while i > -1:
			if self.mot != '':
				self.mot += ' '
			if i >= self.numax:
				return 'un dépassement du numéro max = {} < {}'.format(self.numax, i)
			elif i >= 1e12:
				i = self.tran4(i, 1e12,  'un billion',  ' billions')
			elif i >= 1e9:
				i = self.tran4(i,  1e9, 'un milliard', ' milliards')
			elif i >= 1e6:
				i = self.tran4(i,  1e6,  'un million',  ' millions')
			elif i >= 1e3:
				i = self.tran4(i,  1e3,       'mille',     ' mille')
			elif i >= 1e0:
				j = int(i / 1e0)
				i = i - 1e0 * j
				self.mot += self.tran3(j)
			else:
				if self.mot == '':
					self.mot = 'zéro'
				i -= 1

		return self.mot.strip()

	def tran2(self, i, n, t, diff):
		return i - diff, n + t

	def tran3(self, i):
		if i > 999 or i < 0:
			sys.exit('ERROR {}'.format(i))

		n = ''

		while (i > 0):
			if self.debug:
				print ('\ndebug::{0} {1}\n'.format(i, n))
			#if not n.isspace():  attention déductive
			if not n == '':
				if not n.endswith('cent'):
					if not n.endswith(' '):
						if i != 1:
							if i != 11:
								if n != '':
									n += '-'

			if i >= 1e2:
				j = int(i / 1e2)
				m = self.tran3(j)
				i -= 1e2 * j
				if i == 0 and j > 1: n = n + m + ' cents'
				else:
					if j > 1:
						n = n + m + ' cent '
					else:
						n = n + 'cent '
			elif i >  80: i, n = self.tran2(i, n, 'quatre-vingt', 80)
			elif i == 80: i, n = self.tran2(i, n, 'quatre-vingts', 80)
			elif i >= 60: i, n = self.tran2(i, n, 'soixante', 60)
			elif i >= 50: i, n = self.tran2(i, n, 'cinquante', 50)
			elif i >= 40: i, n = self.tran2(i, n, 'quarante', 40)
			elif i >= 30: i, n = self.tran2(i, n, 'trente', 30)
			elif i >= 20: i, n = self.tran2(i, n, 'vingt', 20)
			elif i >  16: i, n = self.tran2(i, n, 'dix', 10)
			elif i == 16: i, n = self.tran2(i, n, 'seize', 16)
			elif i == 15: i, n = self.tran2(i, n, 'quinze', 15)
			elif i == 14: i, n = self.tran2(i, n, 'quatorze', 14)
			elif i == 13: i, n = self.tran2(i, n, 'treize', 13)
			elif i == 12: i, n = self.tran2(i, n, 'douze', 12)
			elif i == 11:
				if n.isspace() or n == '' or n.endswith('cent '): n += 'onze'
				elif n.endswith('quatre-vingt'): n += '-onze'
				elif n.endswith('cent') or n.endswith('mille'): n += ' onze'
				elif n.endswith('million') or n.endswith('milliard'): n += ' onze'
				elif n.endswith('vingt') or n.endswith('trente'): n += ' et onze'
				elif n.endswith('quarante') or n.endswith('cinquante') or n.endswith('soixante'): n += ' et onze'
				else: n += '-onze'
				i -= 11
			elif i == 10: i, n = self.tran2(i, n, 'dix', 10)
			elif i == 9: i, n = self.tran2(i, n, 'neuf', 9)
			elif i == 8: i, n = self.tran2(i, n, 'huit', 8)
			elif i == 7: i, n = self.tran2(i, n, 'sept', 7)
			elif i == 6: i, n = self.tran2(i, n, 'six', 6)
			elif i == 5: i, n = self.tran2(i, n, 'cinq', 5)
			elif i == 4: i, n = self.tran2(i, n, 'quatre', 4)
			elif i == 3: i, n = self.tran2(i, n, 'trois', 3)
			elif i == 2: i, n = self.tran2(i, n, 'deux', 2)
			elif i == 1:
				if n == '' or n.isspace() or n.endswith('cent '): n += 'un'
				elif n.endswith('quatre-vingt'): n += '-un'
				elif n.endswith('cent') or n.endswith('mille') or n.endswith('million') or n.endswith('milliard'): n += ' un'
				elif n.endswith('vingt') or n.endswith('trente') or n.endswith('quarante') or n.endswith('cinquante') or n.endswith('soixante'): n += ' et un'
				else: n += '-un'
				i -= 1
			else:
				print ('ça ne sera pas')
				if n.isspace(): n += 'zéro'

		return n


	def tran4(self, i, maxi, t1='', t2=''):
		j = int(i / maxi)
		i = i - maxi * j
		if j > 1: self.mot += self.tran3(j) + t2
		else: self.mot += t1
		return i

