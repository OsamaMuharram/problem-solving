x=input()
digit_even=''
digit_odd=''
chr_upper=''
chr_lowper=''
def _sort(y):
    return "".join(sorted(y))
for i in x:
    try:
        a=int(i)%2
        if a==0:
            digit_even= digit_even+str(i)
        else:
            digit_odd=str(i)+digit_odd
    except ValueError:
        if i.isupper():
            chr_upper = chr_upper + i
        else:
            chr_lowper=i+chr_lowper

print(_sort(chr_lowper)+_sort(chr_upper)+_sort(digit_odd)+_sort(digit_even))


