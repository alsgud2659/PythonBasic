# Binary Search 이진 탐색법

# 이진 탐색법은 탐색하는 범위를 절반씩 줄여서 탐색하는 방법이다.
# 데이터들이 먼저 오름차순이나 내림차순으로 정렬되어 있어야만 쓸 수 있다.


# 이진 탐색법의 알고리즘
# 1. 가운데 요소를 선택
# 2. 가운데 요소의 데이터와 찾는 데이터를 비교
# 3. 탐색 범위를 절반으로 줄이는 처리


arr = [11, 13, 17, 19, 23, 29, 31]

def binary_search(num, list, head, tail):
  list.sort()                                                   # 이진탐색은 시작하기전 정렬이 되어 있어야 하기 때문에 정렬을 해줌
  if head > tail:                                               # head가 tail보다 커지면 리턴시킴
    return None
  mid = int((head + tail) / 2)                                  # head 와 tail의 중간값을 변수 mid에 저장
  if num == list[mid]:                                          # 찾는 값이 list[mid]와 같다면 그 값을 리턴
    return print(f'{num}은 {mid + 1}번째 인덱스에 있습니다.') 
  elif num > list[mid]:                                         # list[mid]가 찾는 값보다 작으면 head를 mid + 1로 변경
    head = mid + 1
  else:
    tail = mid - 1                                              # list[mid]가 찾는 값보다 크면 tail를 mid - 1로 변경

  return binary_search(num, list, head, tail)                   # 변경된 head와 tail값을 넣고 함수를 재귀적으로 호출


print(binary_search(17, arr, 0, len(arr)))
