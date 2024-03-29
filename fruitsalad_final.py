'''
Marjukan fruitsalad-ohjelma
uusi kommmentti
'''
def marjukan():
    def haetaantiedot():
        tuotteet=[]
        hinnat=[]
        while True:
              try:
                  name=input(str('Anna ostoslistatiedoston nimi:\n')).lower()
                  with open(name, 'r') as tiedosto:
                      for rivi in tiedosto: #iteroidaan tiedosto rivi riviltä
                          tuote,hinta=rivi.split()
                          tuotteet.append(tuote)
                          hinnat.append(float(hinta))
              except IOError:
                  print('Tiedostoa ei löydy. Tarkista tiedostonimi.')
              else:
                  break

        return (tuotteet,hinnat) #palautetaan kaksi listaa

    def hintalaskuri(ostoslista):
      '''
      Hakee korkeimman ja alimman arvon sekä mahdolliset duplikaatit.
      Tulostaa näytölle lopputuloksen.
      '''
      kallein = max(ostoslista[1])
      halvin = min(ostoslista[1])


      kalleimmattuotteet = [ostoslista[0][ind] for ind, hinta in enumerate(ostoslista[1]) if hinta==kallein]
      halvimmattuotteet = [ostoslista[0][ind] for ind, hinta in enumerate(ostoslista[1]) if hinta==halvin]

      #harjoittelin stringien muotoilua tekemällä puheliaan tuloksen annon:
      if len(kalleimmattuotteet)==1:
          print(f'\nListasi kallein tuote on {kalleimmattuotteet[0]}. Sen hinta on {kallein}.')
      else:
          print(f"\nListasi kalleimmat tuotteet ovat {', '.join(kalleimmattuotteet[:-1])} ja {kalleimmattuotteet[-1]}. Niistä jokaisen hinta on {kallein}.")
      if len(halvimmattuotteet)==1:
          print(f' \nListasi halvin tuote on {halvimmattuotteet[0]}. Sen hinta on {halvin}.')
      else:
          print(f"\nListasi halvimmat tuotteet ovat {', '.join(halvimmattuotteet[:-1])} ja {halvimmattuotteet[-1]}. Niistä jokaisen hinta on {halvin}.")

    return hintalaskuri(haetaantiedot())

def annamarian():

	values = ()
	table =[]
	tuote = []
	hinta = []
	jatkuu = []
	i = 0
	while i < 1:
		tuote=input('kirjoita hedelmä: ')
		hinta=input('kirjoita hinta: ')
		jatkuu=input('onko salaatti valmis? [k/e]? ')
		values=(tuote,hinta)
		table.append(values)

		if (jatkuu == 'k'):
			i=1
			print(table)

		x=min(table)
		y=max(table)

		print("Edullisin: ", x)
		print("Kalliin: ", y)

                  
		if (jatkuu == 'k'): 
			i=1
			print(table)
        
		x=min(table)
		y=max(table)
    
		print("Edullisin: ", x)
		print("Kalliin: ", y)
		

def jonin():

  class Tuote:
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



val = input("Valitse, kenen koodi ajetaan (Marjukka, Annamaria tai Joni) :")

if val == "Marjukka":
	marjukan()

elif val == "Annamaria":
	annamarian()

elif val == "Joni":
	jonin()
