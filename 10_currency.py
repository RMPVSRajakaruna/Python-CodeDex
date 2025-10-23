# Write code below 💖

rate_cop_to_usd = 0.0002624   
rate_pen_to_usd = 0.2854      
rate_brl_to_usd = 0.1846      

Colombian_pesos = float(input('Enter amount in Colombian pesos : '))
Peruvian_soles = float(input('Enter amount in Peruvian soles : '))
Brazilian_reais = float(input('Enter amount in Brazilian reais : '))

usd_from_cop = Colombian_pesos * rate_cop_to_usd
usd_from_pen = Peruvian_soles * rate_pen_to_usd
usd_from_brl = Brazilian_reais * rate_brl_to_usd

usd_total = usd_from_cop + usd_from_pen + usd_from_brl

print(usd_total)