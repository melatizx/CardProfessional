#cpf=[5,4,0,3,8,0,7,7,8,0,2]
cpf1= str(input("Digite seu CPF: "))
cpf=[]
for m in cpf1:
    if m in "0123456789":
        d1=int(m)
        cpf.append(d1)
mult=cpf[0]*10,cpf[1]*9,cpf[2]*8,cpf[3]*7,cpf[4]*6,cpf[5]*5,cpf[6]*4,cpf[7]*3,cpf[8]*2
soma=sum(mult)
div1=soma%11
DV_1=0
if (div1<2):
    DV_1=0
else:
    DV_1=11-div1
nmult=cpf[0]*11,cpf[1]*10,cpf[2]*9,cpf[3]*8,cpf[4]*7,cpf[5]*6,cpf[6]*5,cpf[7]*4,cpf[8]*3,cpf[9]*2
nsoma=sum(nmult)
ndiv1=nsoma%11
DV_2=0
if (ndiv1<2):
    DV_1=0
else:
    DV_2=11-ndiv1
if(DV_1==cpf[-2] and DV_2==cpf[-1]):
    print("CPF VÁLIDO!!")
else:
    print("CPF INVÁLIDO!!")