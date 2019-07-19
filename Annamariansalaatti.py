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
	
	