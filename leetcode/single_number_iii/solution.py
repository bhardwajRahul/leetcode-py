class Solution:
    # Time: O(n)
    # Space: O(1)
    def single_number(self, nums: list[int]) -> list[int]:
        # XOR all numbers - the result is xor of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Find rightmost set bit (differentiating bit between the two unique numbers)
        diff_bit = xor_all & -xor_all

        # Partition numbers based on the differentiating bit
        # and XOR each partition to find the unique numbers
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
