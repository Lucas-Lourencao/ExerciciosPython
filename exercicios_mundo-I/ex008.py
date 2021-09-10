m = float(input('Digite uma distância em metros: '))
k = m/1000
hct = m/100
dct = m/10
dcm = m*10
cm = m*100
mm = m*1000
print('A distância de {} metros informada corresponde a: \n{} Quilômetros;\n{} Hectômetros;\n{}Decâmetros;\n{:.0f}Decímetros;\n{:.0f}Centímetros e;\n{:.0f}Milímetros.'.format(m, k, hct, dct, dcm, cm, mm))
