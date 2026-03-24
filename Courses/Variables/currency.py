'''
We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
    🇨🇴 Colombian pesos
    🇵🇪 Peruvian soles
    🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates for pesos, soles, and reais!
'''
# Write code below 💖

CO = int(input('What do you have left in pesos? '))
CO_USD = CO * 0.00027

PE = int(input('What do you have left in soles? '))
PE_USD = PE * 0.29

BR = int(input('What do you have left in reais? '))
BR_USD = BR * 0.19

total = CO_USD + PE_USD + BR_USD
print(total)