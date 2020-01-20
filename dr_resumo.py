# -*- coding: utf-8 -*-

import wikipedia
from googletrans import Translator
import Algorithmia

print('-'*17)
print('\n')
print('-----------------')
print('| DOUTOR RESUMO |')
print('-----------------')
print('\n')
print('By:Rutherford')
print('\n')
print('-'*17)
print('0 - Sair')
print('1 - Wikipedia')
print('2 - Site')
print('3 - Escrever texto (Somente em inglês)')
print('\n')
print('-'*17)
menu = int(input('Digite sua opção: '))

while menu != 0:

    if menu == 1:

        
        termo = input('Digite o termo que deseja fazer um resumo: ')
        print('-'*30)
        print('realizando resumo , aguarde...')
        print('-'*30)

        resumo = wikipedia.summary(termo)
        arquivo = open('resumo.txt','w')
        translator = Translator()
        traduzido = translator.translate(resumo,dest='pt')
        arquivo.write(str(traduzido))

        #c = canvas.Canvas("resumo.pdf")
        #c.drawString(0,0,str(traduzido))
        #c.save()
        
        print('Resumo feito com sucesso !')
        print('-'*30)
        menu = int(input('Digite sua opção: '))

    elif menu == 2:
        site = input('Digite a url do site: ')
        print('-'*30)
        print('realizando resumo , aguarde...')
        print('-'*30)

        client = Algorithmia.client('YOUR API KEY')
        algo = client.algo('nlp/SummarizeURL/0.1.4')
        algo.set_options(timeout=300) # optional

        resultado = algo.pipe(site).result

        arquivo = open('resumo.txt','w')
        arquivo.write(str(resultado))
        print('Resumo feito com sucesso !')
        print('-'*30)
        menu = int(input('Digite sua opção: '))
    
    elif menu == 3:
        
        texto = input('Digite o texto : ')

        print('-'*30)
        print('realizando resumo , aguarde...')
        print('-'*30)

        client = Algorithmia.client('YOUR API KEY'')
        algo = client.algo('nlp/Summarizer/0.1.8')
        algo.set_options(timeout=300) # optional

        arquivo = open('resumo.txt','w')
        arquivo.write(algo.pipe(texto).result)
        print('Resumo feito com sucesso !')
        print('-'*30)
        menu = int(input('Digite sua opção: '))







