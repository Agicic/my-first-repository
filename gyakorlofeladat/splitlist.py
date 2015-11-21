#!/usr/bin/python
# -*- coding: utf-8 -*-

text = "Gorcsev Iván, a Rangoon teherjáró matróza még huszonegy éves sem volt, midõn elnyerte a fizikai Nobel-díjat. Ilyen nagy jelentõségû tudományos jutalmat e poétikusan ifjú korban megszerezni péIdátlan nagyszerû teljesitmény, még akkor is, ha egyesek elõtt talán szépséghibának tûnik majd, hogy Goresev Iván a fizikai Nobel-díjat a makao nevû kártyajátékon nyerte el, Noah Bertinus professzortól, akinek ezt a kitüntetést Stockholm-ban, néhány nappal elõbb, a svéd király nyújtotta át, de végre is a kákán csomót keresõk nem számítanak; a lényeg a fõ: hogy Gorcsev Iván igenis huszonegy éves korában elnyerte a Nobel-díjat."
lowercase_text=text.lower()
szavak=lowercase_text.split()
word_dict={}
for word in szavak:
	if word[0] in word_dict:
		word_dict[word[0]]+=1
	else:
		word_dict[word[0]]=1
print (word_dict)
