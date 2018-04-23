"""
因为put(), get()的时间复杂度都为O(1)
所以考虑使用dict，因为dict的底层是hashmap，可以保证这个时间复杂度的时间
但是dict无法满足只保留最后使用的k个元素这个条件
所以考虑使用双向链表
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def del_node(self, node):  # 在get()里面会用到这个删除，因为get()之后要把当前结点移到最前
        if node.pre is not None and node.next is not None:  # 如果是中间结点
            node.pre.next = node.next
            node.next.pre = node.pre
        elif node.pre is None and node.next is None:  # 如果只有一个节点
            self.tail = None
            self.head = None
        elif node.pre is None:  # 头结点
            node.next.pre = None
            self.head = node.next
        else:  # 尾结点
            node.pre.next = None
            self.tail = node.pre
        node.pre = None
        node.next = None

    def add(self, node):  # 添加肯定是往头添加
        if self.head is None:  # 如果是双向链表是空
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.pre = node
        self.head = node


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.link_list = DoubleLinkList()
        self.capacity = capacity
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        # 如果在列表中，则先在链表中删除结点，再插入到头部
        node = self.cache[key]
        self.link_list.del_node(node)
        self.link_list.add(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:  # 如果还不在缓存里
            if self.count >= self.capacity:  # 如果达到了上限
                node = self.link_list.tail
                self.link_list.del_node(node)  # 删除尾结点
                self.cache.pop(node.key)  # 删除索引
                self.count -= 1
            tmp = Node(key, value)  # 构建新的结点
            self.cache[key] = tmp  # 添加到dict里面
            self.link_list.add(tmp)  # 添加到双向链表里面
            self.count += 1  # dict里面的东西加一
        else:  # 如果在缓存里了
            tmp = self.cache[key]
            self.link_list.del_node(tmp)  # 先删除链表里的结点
            tmp.value = value  # 改变value
            self.link_list.add(tmp)  # 重新插入
