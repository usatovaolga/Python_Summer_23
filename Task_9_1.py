z={'G':'C','C':'G','T':'A','A':'T'}
s=input("Введите код ДНК - ")
print(f"Код РНК - {s.translate(s.maketrans(z))}")