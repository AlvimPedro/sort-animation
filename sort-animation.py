import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def bubble_sort(arr):
    n = len(arr)
    changed = True

    while changed:
        changed = False
        for i in range(n - 1):
            if arr[i] > arr[i+1]:
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
                changed = True
                yield arr   #Esse yield é um return só q retorna um generator, então sempre que mudar vai criar um novo generator

def insertion_sort(arr):
    n = len(arr)

    for i in range (1, n):
        pos = i
        while pos != 0 and arr[pos] < arr[pos - 1]:
            tmp = arr[pos]
            arr[pos] = arr[pos - 1]
            arr[pos - 1] = tmp
            pos =  pos - 1
            yield arr

def merge_sort(arr, start, end):
    if start < end:                     #Exclui o caso que o array tem tamanho 1 (start = end)
        mid = int((start + end)/2)           #Pegando o ponto do meio
        yield from merge_sort(arr, start, mid)     #Fazendo merge_sort recursivamente na primeira parte do array
        yield from merge_sort(arr, mid+1, end)     #Fazendo merge_sort recursivamente na segunda parte do array
        yield from merge(arr, start, mid, end)     #Fazendo um merge dessas duas partes que vao estar ordenadas por voltar do merge_sort

def merge(arr, start, mid, end):
    arr_auxiliar = []  #Array auxiliar de tamanho dos dois arrays

    i = start               #i vai acompanhar o array da esquerda que vai até mid
    j = mid + 1             #j vai acompanhar o array da direita que vai até end
    k = 0                   #k acompanha o array auxiliar
    
    while i <= mid and j <= end:    #Enquanto não foi preenchido todo o array auxiliar
        if arr[i] <= arr[j]:
            arr_auxiliar.append(arr[i])
            i += 1
            k += 1

        elif arr[j] < arr[i]:
            arr_auxiliar.append(arr[j])
            j += 1
            k += 1

    while k <= (end - start): #Ainda não colocou todos os dados
        if i <= mid:    #Ainda precisa colocar os restos dos i no arr auxiliar
            arr_auxiliar.append(arr[i])
            i += 1
            k += 1
        elif j <= end:    #Ainda precisa colocar os restos dos j no arr auxiliar
            arr_auxiliar.append(arr[j])
            j += 1
            k += 1

    k = 0
    for u in range(start,end+1):
        arr[u] = arr_auxiliar[k]
        k += 1
        yield arr


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minimo = arr[i]
        pos_min = i
        for j in range(i,n):
            if arr[j] < minimo:
                minimo = arr[j]
                pos_min = j
        arr[pos_min] = arr[i]
        arr[i] = minimo
        yield arr

if __name__ == "__main__":

    N = int(input('Digite a quantidade de números: '))
    algo_input = 'Coloque o Algorítimo de Ordenação:\n(b)ubble\n(i)nsertion\n(m)erge \
        \n(q)uick\n(s)election\n'
    algo = input(algo_input)


    y = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(y)


    #Ver qual algoritmo usar
    if algo == 'b':
        title = 'Bubble Sort'
        generator = bubble_sort(y)

    if algo == 'i':
        title = 'Insertion Sort'
        generator = insertion_sort(y)

    elif algo == 's':
        title = 'Selection Sort'
        generator = selection_sort(y)

    elif algo == 'm':
        title = 'Merge Sort'
        generator = merge_sort(y,0,len(y)-1)

    else:
        title = 'Selection Sort'
        generator = selection_sort(y)



    #Inicializar o plot do gráfico
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(y)),y)
    ax.set_title(title)
    

    def update(i):
        global bar_rects
        bar_rects.remove()
        bar_rects = ax.bar(range(len(i)),i, color='#0C98E8')

    anim = FuncAnimation(fig, update, repeat = False, frames=generator, interval=100)

    plt.show()