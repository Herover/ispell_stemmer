import ispell

test = ispell()
test.readAffixFile("../corpa/ispell/dansk.aff")
test.readWordFile("../corpa/ispell/dansk.ispell")
