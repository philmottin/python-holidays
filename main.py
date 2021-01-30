from datetime import date

import holidays
import sys

import argparse
import datetime
now = datetime.datetime.now()

print ("\nMODO DE USAR:\npython3 main.py --ano <ano> --uf <UF> \n")
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Exibe calendarios de feriados para o ano e estado especificado.")
   parser.add_argument('--ano', nargs='?', const=-1, type=int, default=-1, help='Ano com 4 digitos')
   parser.add_argument('--uf', nargs='?', const='-1', default='-1', help='Estado com 2 letras')   
   args = parser.parse_args()
   if (args.ano == -1):
     args.ano = now.year
     print("-> Nenhum ano foi especifivado, usando o ano atual como padrão:",now.year)
   if (args.uf == '-1'):
     args.uf = 'SP'
     print("-> Nenhum estado foi especifivado, usando 'SP' como padrão")

#https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('--example', nargs='?', const=1, type=int)
#args = parser.parse_args()
#print(args)

#% test.py 
#Namespace(example=None)
#% test.py --example
#Namespace(example=1)
#% test.py --example 2
#Namespace(example=2)

#nargs='?' means 0-or-1 arguments
#const=1 sets the default when there are 0 arguments
#type=int converts the argument to int
#If you want test.py to set example to 1 even if no --example is specified, then include default=1. That is, with
#parser.add_argument('--example', nargs='?', const=1, type=int, default=1)

#us_holidays = holidays.UnitedStates()
# or:
# us_holidays = holidays.US()
# or:
# us_holidays = holidays.CountryHoliday('US')
# or, for specific prov / states:
# us_holidays = holidays.CountryHoliday('US', prov=None, state='CA')


def pluralize(n, text):
    return "{} {}{}".format(n,text, 's' if n > 1 else '')


ano = args.ano
estado = args.uf
feriados = 0
print("\nFERIADOS EM",estado,"PARA O ANO",ano,"\n")
for date, name in sorted(holidays.BR(state=estado, years=ano).items()):
  print(date.strftime('%d/%m/%y'),name)
  #print(date, name)
  feriados = feriados+1
print("")
print(feriados,"FERIADOS\n")
