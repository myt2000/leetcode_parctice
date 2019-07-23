'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = []
        p2 = []
        s1 = l1
        s2 = l2
        while True:
            p1.append(s1.val)
            s1 = s1.next
            if not s1:
                break
        while s2:
            p2.append(s2.val)
            s2 = s2.next
            if not s2:
                break
        p1.reverse()
        p2.reverse()
        num1 = int("".join(map(str, p1)))
        num2 = int("".join(map(str, p2)))
        num3 = num1 + num2
        s3 = str(num3)
        length = len(s3)
        # for i in range(length, 0, -1):
        node = ListNode(int(s3[0]))
        if length > 1:
            for i in range(1, length):
                p3 = ListNode(int(s3[i]))
                p3.next = node
                node = p3
        else:
            p3 = node
        return p3


    def addTwoNumbers2(self, l1, l2):
        target = ListNode(0)  # 作为根节点的引用
        p = target
        add = 0  # 作为上一次相加是否需要进1的依据
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + add) % 10)
            add = (l1.val + l2.val + add) // 10
            p, l1, l2 = p.next, l1.next, l2.next
        l1 = l1 if l1 else l2
        while add:
            if l1:
                p.next = ListNode((l1.val + add) % 10)
                add = (l1.val + add) // 10
                p, l1 = p.next, l1.next
            else:
                p.next = ListNode(add)
                p = p.next
                break
        p.next = l1

        return target.next


    def addTwoNumbers3(self, l1, l2):
        add = 0
        l3 =l4 = ListNode(0)
        while l1 or l2 or add:
            if l1 or l2:
                if l1:
                    num = l1.val +add
                    if l2:
                        num = num + l2.val
                elif l2:
                    num = l2.val + add
                    if l1:
                        num = num + l1.val
            else:
                num = add
            add = 0
            if num//10 >0:
                add = 1
                num = num%10
            l3.val = num

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if l1 or l2 or add:
                l3.next = ListNode(0)
                l3 = l3.next
        return l4.next


    def addTwoNumbers4(self, l1, l2):
        '''
        完全使用链表完成，不存在数字和字符串转换
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        # 最优解52ms
        # 链表初始值
        re = ListNode(0)
        # 用于创建游标节点
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            # 求取十位数，整除求取
            carry = s // 10
            # 因为求取个位数，求取余数
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        # 返回初始值的下一个结点即可
        return re.next


if __name__ == "__main__":
    num1 = [7,8,9]
    num2 = [5,6,7]
    length1 = len(num1)
    length2 = len(num2)
    node1 = ListNode(num1[-1])
    node2 = ListNode(num2[-1])
    if length1 > 1:
        for i in range(length1-2, -1, -1):
            # print(list(range(length1-1,0,-1)))
            p1 = ListNode(int(num1[i]))
            p1.next = node1
            node1 = p1
    else:
        p1 = node1
    if length2 > 1:
        for i in range(length2-2, -1, -1):
            p2 = ListNode(int(num2[i]))
            p2.next = node2
            node2 = p2
    else:
        p2 = node2

    test_demo = Solution()
    result = test_demo.addTwoNumbers4(p1, p2)
    print(result)

