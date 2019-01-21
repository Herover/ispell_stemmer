from unittest import TestCase

from ispell_stemmer import ispell

class TestIspell(TestCase):
	def setUp(self):
		self.speller = ispell()
		self.speller.readAffixFile("./ispell_stemmer/tests/basic.aff")
		self.speller.readWordFile("./ispell_stemmer/tests/basic.ispell")
		# print(self.speller.wordrelations.items())

	def test_single_ending(self):
		self.assertEqual(self.speller.getBaseOfWord('1x'), ['1x'])
		self.assertEqual(self.speller.getBaseOfWord('1xa'), ['1x'])

		self.assertEqual(self.speller.getBaseOfWord('2y'), ['2y'])
		self.assertEqual(self.speller.getBaseOfWord('2ya'), ['2y'])

	def test_multi(self):
		self.assertEqual(self.speller.getBaseOfWord('3x'), ['3x'])
		self.assertEqual(self.speller.getBaseOfWord('3xb'), ['3x'])
		self.assertEqual(self.speller.getBaseOfWord('3y'), ['3y'])
		self.assertEqual(self.speller.getBaseOfWord('3yb'), ['3y'])


if __name__ == '__main__':
	unittest.main()
