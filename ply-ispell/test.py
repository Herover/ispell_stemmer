import ispell

test = ispell.ispell()
test.readAffixFile("../corpa/ispell/dansk.aff")
test.readWordFile("../corpa/ispell/dansk.ispell")
#test.readAffixFile("../corpa/ispell/english.aff")
#test.readWordFile("../corpa/ispell/american-insane.mwl")

#from collections import OrderedDict
#orderedlist = OrderedDict(sorted(test.wordrelations.items()))
#print(orderedlist)

print(test.getBaseOfWord("vandpibe"))
print(test.getBaseOfWord("vandpibes"))
print(test.getBaseOfWord("vandpiber"))
print(test.getBaseOfWord("vandpiben"))
print(test.getBaseOfWord("vandpiberne"))
print(test.getBaseOfWord("bil"))
print(test.getBaseOfWord("bils"))
print(test.getBaseOfWord("biler"))
print(test.getBaseOfWord("bilen"))
print(test.getBaseOfWord("bilerne"))

#print(test.getBaseOfWord("car"))
#print(test.getBaseOfWord("cars"))
#print(test.getBaseOfWord("preventive"))
#print(test.getBaseOfWord("weakens"))
#print(test.getBaseOfWord("fallen"))
