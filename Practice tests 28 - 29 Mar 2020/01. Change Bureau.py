bitcoin = int(input())
yan = float(input())
commision = float(input()) / 100

bitcoin_to_bgn = 1168
yan_to_usd = 0.15
usd_to_bgn = 1.76
eur_to_bgn = 1.95

total = (((bitcoin * bitcoin_to_bgn) / 1.95) + (((yan * yan_to_usd) * usd_to_bgn) / 1.95)) * (1 - commision)
print("%.2f" % total)
