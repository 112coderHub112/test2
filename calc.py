#import pandas as pd
sun_table = [[35,32,27,22,13,5],
             [0,35,67,94,116,129]]


kj = 278338

z = kj // 24350
z_remainder = kj % 24350
degree = z_remainder//811
d_remainder = z_remainder % 811
minute = d_remainder//14

d_total = z*30+degree
mathasun = d_total*60+minute-3



if mathasun > 21600:
    raise Exception('mathasun exceed 21600')
elif mathasun < 0:
    raise Exception('mathasun below 0')
elif mathasun < 4800:
    pholsun = 21600+mathasun-4800
else:
    pholsun = mathasun-4800


if pholsun > 21600:
    raise Exception('pholsun exceed 21600')
elif pholsun < 0:
    raise Exception('pholsun below 0')
elif pholsun >= 0 and pholsun <5400:
    pholGA = pholsun

elif pholsun >= 5400 and pholsun <10800:
    pholGA = 10800-pholsun

elif pholsun >= 10800 and pholsun <16200:
    pholGA = pholsun-10800

elif pholsun >= 16200:
    pholGA = 21600-pholsun
    

khan = pholGA // 900
pushlip = pholGA % 900


jyaGA = (sun_table[0][khan]*pushlip) // 900
ravipphol = sun_table[1][khan]+jyaGA


if pholsun < 10800:
    Ssun = mathasun-ravipphol
elif pholsun > 10800:
    Ssun= mathasun+ravipphol
elif pholsun == 10800:
    if(ravipphol != 0):raise Exception('pholsun=10800 but ravipphol not 0')
    Ssun= mathasun

if Ssun < 0:
    Ssun = Ssun+21600
elif Ssun > 21600:
    Ssun= Ssun-21600

zodiac,frac = divmod(Ssun,1800)
degree,minute = divmod(frac,60)



##print(z)
##print(degree)
##print(minute)
##print(d_total)


print('mathasun =',mathasun)
print('pholsun =',pholsun)
print('pholGA =',pholGA)
print('khan =',khan)
print('pushlip =',pushlip)
print('ravipphol =',ravipphol)
print('Ssun =',Ssun)

print('zodiac =',zodiac)
print('degree =',degree)
print('minute =',minute)


##df = pd.DataFrame(columns=['kj','sun'])
###print(df)
###print(len(df.index))
###df = pd.DataFrame()
##df = df.append({'kj' : kj , 'sun' : Ssun} , ignore_index=True)
##	
##
##print(df)


'''
s_ravi = {
    'jya': [35,32,27,22,13,5],
    'ravi': [0,35,67,94,116,129]
}
df = pd.DataFrame(s_ravi)

#df.iloc[1] = [kj,Ssun]
#df.append(data)
df = df.append({'kj' : 'Sahil' , 'sun' : 22} , ignore_index=True)
df = df.append({'kj' : 'Sahil' , 'sun' : 22} , ignore_index=True)


##z,frac = divmod(kj,24350)
##d,frac = divmod(frac,811)
##m,fm = divmod(frac,14)
##mathasun = (z*30+d)*60+m-3


'''
