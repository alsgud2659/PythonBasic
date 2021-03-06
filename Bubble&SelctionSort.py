# 버블정렬

def bubbleSort(arr):                                           
    n = len(arr)                                        # 코드 간결화를 위해 arr의 길이를 n에 저장                                    
    for i in range(n):                                  # 배열의 크기만큼 반복
        print(f'{i + 1}번째 반복')                       # 몇번째 반복인지 출력 
        for j in range(0, n - i - 1):                   # 0 부터 n - i - 1까지 반복 하면 이미 정렬된 부분까지 돌지 않음
            if arr[j] > arr[j + 1]:                     # 현재 인덱스 값이 다음 인덱스를 비교해 더 크면 교환을 함
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print('정렬중:', arr)                        # 어디까지 정렬했는지 출력

# 선택정렬

def selectionSort(arr):                                  
    n = len(arr)                                        # 코드 간결화를 위해 arr의 길이를 n에 저장  
    for i in range(n - 1):                              # n - 1만큼 반복
        print(f'{i + 1}번째 반복')                       # 몇번째 반복인지 출력
        min = i                                         # 최소값을 임의로 지정
        for j in range(i + 1, n):                       # i + 1 부터 배열의 길이만큼 반복
            if arr[j] < arr[min]:                       # 최소값으로 지정한 인덱스 값이 현재 인덱스보다 크다면 최소값을 현재 인덱스로 갱신
                min = j
            
        arr[i], arr[min] = arr[min], arr[i]             # 갱신후 두 값의 자리를 변경
        print('정렬중:', arr)
    

              
                
arr = [5,2,3,1,4]
arr1 = [8,6,10,7,9]


print('정렬전:', arr)
bubbleSort(arr)
print('정렬후:', arr)
print('--------------------------')

# 버블정렬 결과
# 정렬전: [5, 2, 3, 1, 4]
# 0번째 반복
# 정렬중: [2, 5, 3, 1, 4]
# 정렬중: [2, 3, 5, 1, 4]
# 정렬중: [2, 3, 1, 5, 4]
# 정렬중: [2, 3, 1, 4, 5]
# 1번째 반복
# 정렬중: [2, 3, 1, 4, 5]
# 정렬중: [2, 1, 3, 4, 5]
# 정렬중: [2, 1, 3, 4, 5]
# 2번째 반복
# 정렬중: [1, 2, 3, 4, 5]
# 정렬중: [1, 2, 3, 4, 5]
# 3번째 반복
# 정렬중: [1, 2, 3, 4, 5]
# 4번째 반복
# 정렬후: [1, 2, 3, 4, 5]

print('정렬전:', arr1)
selectionSort(arr1)
print('정렬후:', arr1)


# 선택 정렬
# 정렬전: [8, 6, 10, 7, 9]
# 1번째 반복
# 정렬중: [6, 8, 10, 7, 9]
# 2번째 반복
# 정렬중: [6, 7, 10, 8, 9]
# 3번째 반복
# 정렬중: [6, 7, 8, 10, 9]
# 4번째 반복
# 정렬중: [6, 7, 8, 9, 10]
# 정렬후: [6, 7, 8, 9, 10]