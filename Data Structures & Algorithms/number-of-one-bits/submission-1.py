class Solution:
    def hammingWeight(self, n: int) -> int:
        def print_in_32_bits(number):
            # For positive numbers
            if number >= 0:
                # Convert to binary, remove the '0b' prefix
                binary_representation = bin(number)[2:]
                # Pad with leading zeros to 32 bits
                padded_binary = binary_representation.zfill(32)
                print(f"Positive {number}: {padded_binary}")
            # For negative numbers (using two's complement for 32 bits)
            else:
                # Calculate the two's complement value for 32 bits
                # The range for a signed 32-bit integer is -2^31 to (2^31 - 1)
                # 2**32 is 4294967296
                # -number is positive, then subtract from 2^32
                two_complement_value = (1 << 32) + number
                
                # Convert this two's complement value to binary and pad
                binary_representation = bin(two_complement_value)[2:]
                padded_binary = binary_representation.zfill(32)
                print(f"Negative {number}: {padded_binary}")
        print_in_32_bits(11)
        print_in_32_bits(10)
        print()
        print_in_32_bits(10)
        print_in_32_bits(9)


        res = 0
        while n:
            n = n & (n-1)
            res += 1
            
        return res