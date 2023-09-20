class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Initialize two lists to store products to the left and right of each element
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate the products to the left of each element
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        # Calculate the products to the right of each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        # Combine the left and right products to get the final result
        result = [left_products[i] * right_products[i] for i in range(n)]
        
        return result

        '''
        this was togggling my brains for a lot of time
        essentially this is easy if yoou can do it o(n^2) time by taking each element in the array 
        and performing a basic function where you pop that element and multiply the rest by iteratin gover the list each tike again!!
        but we need it in o(n)

        so for that the left product and right product for each elemenr
        like in [1,2,3,4]
        left product of 3 will be 1*2 = 2
        right product of 3 will be 4
        so two new arrays of same length as initial nums array need to store these products seperately
        so basically the addtual product can be calculated by muling these l adn r products!!
        o(n) time!!
        '''