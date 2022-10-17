import unittest
from translator import english_to_french, french_to_english

class Englishtofrench(unittest.TestCase):
    def teste2f(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
class Frenchtoenglish(unittest.TestCase):
    def testf2e(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Bonjour"), "Hello")
unittest.main()       