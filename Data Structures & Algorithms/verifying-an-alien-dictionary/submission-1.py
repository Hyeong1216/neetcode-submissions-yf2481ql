# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         # 1. Sort
#         # order_index = {c:i for i, c in enumerate(order)}

#         # def compare(word):
#         #     return [order_index[c] for c in word]

#         # return words == sorted(words, key=compare)

#         # 2. Comparing Adjacent words
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 알파벳(order) 각 문자가 몇 번째 순서인지 매핑하는 딕셔너리 생성
        # 예: order = "hlabcdefgijkmnopqrstuvwxyz" -> {'h':0, 'l':1, 'a':2, ...}
        order_index = {c: i for i, c in enumerate(order)}

        # 인접한 단어 쌍(w1, w2)을 순서대로 비교
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # w1의 각 글자를 w2와 같은 위치에서 하나씩 비교
            for j in range(len(w1)):
                # w1이 w2보다 길고, w2의 길이를 넘어서는 위치까지 왔다면
                # (예: w1="apple", w2="app" 처럼 앞부분이 똑같은 경우)
                # 더 긴 단어가 뒤에 와야 하는데 순서가 반대이므로 False
                if j == len(w2):
                    return False

                # 같은 위치의 글자가 다르다면, 여기서 대소 비교를 해야 함
                if w1[j] != w2[j]:
                    # 알파벳 순서상 w1의 글자가 w2의 글자보다 뒤에 있으면
                    # (즉, w1이 w2보다 사전순으로 더 크면) 정렬 위반 -> False
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    # 다른 글자를 찾았고 순서 문제 없음이 확인되었으므로
                    # 이 단어 쌍에 대한 비교는 여기서 끝내고 다음 쌍으로 이동
                    break
            # 만약 break 없이 for문이 끝났다면 (즉 w1이 w2의 접두사이거나 같은 경우)
            # w1 <= w2가 이미 보장되므로 별도 처리 없이 다음 단어 쌍으로 넘어감

        # 모든 인접 쌍이 순서를 위반하지 않았다면 정렬된 것
        return True