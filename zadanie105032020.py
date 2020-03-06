

# zadanie wizytowka 
# nazwisko = "jjjjjjjj"
# tytul = "kdjskdjskd"

# użyć zmiennych i 
# " " * (len(tytul) - len (nazwisko))
# level up - nazwisko wysrodkowane
# wrzucic na github


print ('!'*23 + "\n" + ('!' + ' '*8 + 'HELLO'+' '*8 + '!')+ "\n" + '!'*23)
# dane wejsciowe
name="Joanna Włoskowicz"
job="Architect"

# minitesty programu
print(name)
print(job)
print(len(name))
print(len(job))

# obliczenie roznicy znakow wyrazow
space=len(name)-len(job)
print(space)
# wyliczenie polowy
polow=space/2
# proba ułamka
print(polow)
# usawienie linijki z imieniem
fline=len(name)+6 
print(fline)

print('%'*int(space/2))
# gotowy program drukujacy wizytowke
print (('+' +'!'*fline + '+' ) + "\n" +('|'+ ' '* fline + '|') + "\n" + ('|' + ' '*3 + name +' '*3 + '|') + "\n" +('|' + ' '*(3+int(space/2)) + job +' '*(3+int(space/2)) + '|') + "\n" +('|'+ ' '* fline + '|')+"\n"+ ('+' +'!'*fline + '+' ))

