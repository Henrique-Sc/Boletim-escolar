# Imports
from statistics import mean
from time import sleep

# Cores
r = '\033[m'
IR = '\033[38;5;9m'
IB = '\033[38;5;12m'
negrito = '\033[1m'

alunos = list()

# Título
print('-=--=--= Boletim escolar =--=--=-')

# While para inserção dos dados
while True:
    print('\n----------------------------------')
    
    nome = (str(input('\nPrimeiro nome do aluno: ').strip().title()))
    notas = [float(input('Nota 1: ').strip()), float(input('Nota 2: ').strip())]
    
    print('\n----------------------------------')
    media = mean(notas)

    alunos.append([nome, notas[:], media])

    sleep(0.3)

    while True:
        esc = input(f'\nDeseja continuar? [{IB}S{r}im / {IR}N{r}ão]: ').strip().upper()[0]
        # Tratamento de erros
        while esc not in 'SN':
            print(f'\n{IR}Valor incorreto!{r} Digite novamente.')
            esc = input(f'Deseja continuar? [{IB}S{r}im / {IR}N{r}ão]: ').strip().upper()[0]
        break

    sleep(0.3)

    if esc == 'N':
        break
    
# Linha para design
print('\n', '-=' * 20)
sleep(0.3)
print('')

# Exibição do boletim
print('\t', '-' * 31)
sleep(0.3)
print(f'\t | {negrito}Nº  | Nome         | Média  {r}|')
sleep(0.3)


for n, aluno in enumerate(alunos):
    print(f'\t | {n + 1:<3} | {aluno[0]:<12} | {f"{aluno[2]:.1f}":<6} |')
    sleep(0.3)

print('\t', '-' * 31)
sleep(0.3)
print('\n', '-=' * 20)
sleep(0.3)
print('')

print('Obs: digite o número do aluno(a) (0 para parar).')
while True:
    ver_nota = int(input('\nDeseja mostrar as notas de qual aluno(a)? ').strip())
    sleep(0.5)
    
    print('')
    
    while ver_nota < 0 or ver_nota > len(alunos):
        ver_nota = int(input(f'{IR}Valor inválido! Digite o número correto de um dos alunos: {r}').strip())
        sleep(0.5)
    
    if ver_nota == 0:
        
        break

    print(f'Notas do(a) {alunos[ver_nota - 1][0]}: {alunos[ver_nota - 1][1]}')

for c in range(5):
    sleep(0.3)
    print('.')

print('\n<- Programa finalizado. ->')
