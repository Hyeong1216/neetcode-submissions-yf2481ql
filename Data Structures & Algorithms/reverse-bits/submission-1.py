class Solution:
    def reverseBits(self, n: int) -> int:
        # res = 0
        # for i in range(32):
        #     bit = (n >> i) & 1
        #     res += (bit << (31-i))
        # return res
        #--------------------------------------------------------------------------
        # Example: n = 21
        # Binary: 00000000000000000000000000010101
        # Goal: Reverse to get 10101000000000000000000000000000 = 2818572288
        
        res = 0  # This will store our reversed result (starts as 0)
        
        # Loop through all 32 bit positions (0 to 31)
        # i represents the position we're reading FROM (right to left)
        for i in range(32):  # i = 0, 1, 2, ..., 31
            
            # Step 1: Extract the bit at position i from the right
            # (n >> i) shifts n right by i positions
            # & 1 extracts only the rightmost bit (masks all other bits)
            bit = (n >> i) & 1
            
            # Let's trace through first few iterations for n=21:
            # i=0: (21 >> 0) & 1 = 21 & 1 = 10101 & 00001 = 1
            # i=1: (21 >> 1) & 1 = 10 & 1 = 01010 & 00001 = 0  
            # i=2: (21 >> 2) & 1 = 5 & 1  = 00101 & 00001 = 1
            # i=3: (21 >> 3) & 1 = 2 & 1  = 00010 & 00001 = 0
            # i=4: (21 >> 4) & 1 = 1 & 1  = 00001 & 00001 = 1
            # i=5: (21 >> 5) & 1 = 0 & 1  = 00000 & 00001 = 0
            # ... all remaining bits are 0
            
            # Step 2: Place this bit at the reversed position
            # (31-i) calculates the target position from the left
            # (bit << (31-i)) shifts the bit to that position
            # res += adds this positioned bit to our result
            res += (bit << (31 - i))
            
            # Let's trace the positioning:
            # i=0: bit=1, target pos=31-0=31, res += (1 << 31) = res += 2147483648
            # i=1: bit=0, target pos=31-1=30, res += (0 << 30) = res += 0
            # i=2: bit=1, target pos=31-2=29, res += (1 << 29) = res += 536870912  
            # i=3: bit=0, target pos=31-3=28, res += (0 << 28) = res += 0
            # i=4: bit=1, target pos=31-4=27, res += (1 << 27) = res += 134217728
            # i=5 onwards: bit=0, so res += 0
            
            # Final result: 2147483648 + 536870912 + 134217728 = 2818572288
        
        return res  # Return the final reversed number