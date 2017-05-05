class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r_origin = len(nums)
        c_origin = len(nums[0])
        if r_origin * c_origin != r * c:
            return nums
        else:
            new_list = []
            for i in range(r_origin):
                new_list += nums[i]

            reshaped_list = []
            for j in range(r):
                new_row = new_list[j*c:(j+1)*c]
                reshaped_list.append(new_row)

            return reshaped_list