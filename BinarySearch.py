# Binary Search 이진 탐색법

# 이진 탐색법은 탐색하는 범위를 절반씩 줄여서 탐색하는 방법이다.
# 데이터들이 먼저 오름차순이나 내림차순으로 정렬되어 있어야만 쓸 수 있다.


# 이진 탐색법의 알고리즘
# 1. 가운데 요소를 선택
# 2. 가운데 요소의 데이터와 찾는 데이터를 비교
# 3. 탐색 범위를 절반으로 줄이는 처리


arr = [11, 13, 17, 19, 23, 29, 31]

def binary_search(num, list, head, tail):
  list.sort()
  if head > tail:
    return None
  mid = int((head + tail) / 2)
  if num == list[mid]:
    return print(f'{num}은 {mid + 1}번째 인덱스에 있습니다.')
  elif num > list[mid]:
    head = mid + 1
  else:
    tail = mid - 1

  return binary_search(num, list, head, tail)


print(binary_search(17, arr, 0, len(arr)))
