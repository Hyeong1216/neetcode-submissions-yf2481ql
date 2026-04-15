class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        sorted_cards = sorted(count.keys())

        print(f"count:{count}")
        print(f"sorted_cards:{sorted_cards}")

        for card in sorted_cards:
            # TODO: If this card still needs to be used
            # TODO: Try to form a group starting from this card
            # TODO: Check if all consecutive cards are available
            if count[card] > 0:
                # we need to form count[card] groups starting with 'card'
                groups_needed = count[card]

                # Try to form groups: [card, card+1, card+2, ..., card+groupSize-1]
                for i in range(groupSize):
                    next_card = card + i

                    if count[next_card] < groups_needed:
                        return False
                    
                    count[next_card] -= groups_needed


        return True