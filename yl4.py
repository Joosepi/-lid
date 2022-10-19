arv_tekstina = input('Palun sisesta mingi arv: ')
arv = float(arv_tekstina)

if arv < 0:

    vastus = -arv
else:
    vastus = arv

print('Selle arvu on ' + str(vastus))