﻿class Tuote:
	def __init__(self, nimi, hinta):
		self.nimi = nimi
		self.hinta = hinta

lista = []

while True:
	syote = input('Syötä komento: "lisää" tai "poistu": ')

	if syote == 'poistu':
		indeksi = 0
		suurin = lista[0].hinta
		suurinTuote = lista[indeksi]
		while indeksi < len(lista):
			if lista[indeksi].hinta > suurin:
				suurin = lista[indeksi].hinta
				suurinTuote = lista[indeksi]
			indeksi = indeksi + 1
		print('Kallein tuote: ' + suurinTuote.nimi + ' ' + str(suurinTuote.hinta) + '€')

		indeksi = 0
		pienin = lista[0].hinta
		pieninTuote = lista[indeksi]
		while indeksi < len(lista):
			if lista[indeksi].hinta < pienin:
				pienin = lista[indeksi].hinta
				pieninTuote = lista[indeksi]
			indeksi = indeksi + 1
		print('Halvin tuote: ' + pieninTuote.nimi + ' ' + str(pieninTuote.hinta) + '€')

		break

	elif syote == 'lisää':
		
		tuote = input('Anna tuote: ')
		hinta = input('Anna hinta: ')
		uusiTuote = Tuote(tuote, int(hinta))
		lista.append(uusiTuote)