"""
154. Find Minimum in Rotated Sorted Array II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
说明：

这道题是 寻找旋转排序数组中的最小值 的延伸题目。
允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# by_hh https://zxi.mytechroad.com/blog/?s=Find+Minimum+in+Rotated+Sorted+Array
# 结合lc153


# review
class SolutionT154(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                res = i
                break
        return nums[res]

    def findMin_2(self, nums):
        return self.binary_search(nums, 0, len(nums)-1)

    def binary_search(self, nums, left, right):
        if left + 1 >= right:
            return min(nums[left], nums[right])

        if nums[left] < nums[right]:
            return nums[left]

        mid = left + (right - left) // 2

        return min(self.binary_search(nums, left, mid-1), self.binary_search(nums, mid, right))


