#function on parametes
def volume_balok(p, l, t, kode_balok = "TBxx"):
    volume = p * l * t
    print("volume balok dari balok %s adalah %d: " % (kode_balok, volume))
volume_balok(12, 7, 3)
