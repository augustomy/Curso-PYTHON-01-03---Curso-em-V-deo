x = float(input('Digite uma distância em metros: '))
km = x / 1000
hm = x / 100
dam = x / 10
dm = x * 10
cm = x * 100
mm = x * 1000
print('A medida de {} metros corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(x, km, hm, dam, dm, cm, mm))
