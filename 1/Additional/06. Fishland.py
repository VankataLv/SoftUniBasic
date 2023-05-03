skumria_kg = float(input())
caca_kg = float(input())
need_palamud = float(input())
need_safrid = float(input())
need_midi = float(input())

money_palamud = need_palamud * (skumria_kg * 1.6)
money_safrid = need_safrid * (caca_kg * 1.8)
money_midi = need_midi * 7.50
money_total = money_midi + money_safrid + money_palamud

print("%.2f" % money_total)
