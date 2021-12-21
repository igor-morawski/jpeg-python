from queue import PriorityQueue

# class HuffmanTree:
#     class Node:
#         def __init__(self, freq, symbol, left=None, right=None):
#             self.freq = freq
#             self.symbol = symbol
#             self.left = left
#             self.right = right


#     def __init__(self, arr, default=False):
#         self.default = default
#         if self.default:
#             # https://www.w3.org/Graphics/JPEG/itu-t81.pdf page 149
#             self.__value_to_bitstring = {   0 : '00',
#                                             1 : '010', 
#                                             2 : '011',
#                                             3 : '100',
#                                             4 : '101',
#                                             5 : '110',
#                                             6 : '1110',
#                                             7 : '11110',
#                                             8 : '111110',
#                                             9 : '1111110',
#                                             10 : '11111110',
#                                             11 : '111111110', }
#             return

#         q = PriorityQueue()
#         freq_dict = dict()
#         for elem in arr:
#             if elem in freq_dict:
#                 freq_dict[elem] += 1
#             else:
#                 freq_dict[elem] = 1
#         return freq_dict

#         for val, freq in freq_dict.items():
#             q.put(self.Node(freq, val))

#         while q.qsize() >= 2:
#             u = q.get()
#             v = q.get()

#             q.put(self.Node(u.freq+v.freq, None, u, v))

#         self.root = q.get()
#         self.value_to_bitstring = dict()

#         def tree_traverse(current_node, bitstring=''):
#             if current_node is None:
#                 return
#             if current_node.valu:
#                 self.__value_to_bitstring[current_node.value] = bitstring
#                 return
#             tree_traverse(current_node.left_child, bitstring + '0')
#             tree_traverse(current_node.right_child, bitstring + '1')

#         tree_traverse(self.root)
        



class HuffmanTree:

    class __Node:
        def __init__(self, value, freq, left_child, right_child):
            self.value = value
            self.freq = freq
            self.left_child = left_child
            self.right_child = right_child

        @classmethod
        def init_leaf(self, value, freq):
            return self(value, freq, None, None)

        @classmethod
        def init_node(self, left_child, right_child):
            freq = left_child.freq + right_child.freq
            return self(None, freq, left_child, right_child)

        def is_leaf(self):
            return self.value is not None

        def __eq__(self, other):
            stup = self.value, self.freq, self.left_child, self.right_child
            otup = other.value, other.freq, other.left_child, other.right_child
            return stup == otup

        def __nq__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self.freq < other.freq

        def __le__(self, other):
            return self.freq < other.freq or self.freq == other.freq

        def __gt__(self, other):
            return not (self <= other)

        def __ge__(self, other):
            return not (self < other)

    def __init__(self, arr, default=False):
        self.default = default
        if self.default:
            # https://www.w3.org/Graphics/JPEG/itu-t81.pdf page 149
            self.__value_to_bitstring = {   0 : '00',
                                            1 : '010', 
                                            2 : '011',
                                            3 : '100',
                                            4 : '101',
                                            5 : '110',
                                            6 : '1110',
                                            7 : '11110',
                                            8 : '111110',
                                            9 : '1111110',
                                            10 : '11111110',
                                            11 : '111111110', }
            return
        q = PriorityQueue()

        # calculate frequencies and insert them into a priority queue
        for val, freq in self.__calc_freq(arr).items():
            q.put(self.__Node.init_leaf(val, freq))

        while q.qsize() >= 2:
            u = q.get()
            v = q.get()

            q.put(self.__Node.init_node(u, v))

        self.__root = q.get()

        # dictionaries to store huffman table
        self.__value_to_bitstring = dict()

    def value_to_bitstring_table(self):
        if len(self.__value_to_bitstring.keys()) == 0:
            self.__create_huffman_table()
        print(self.__value_to_bitstring)
        return self.__value_to_bitstring

    def __create_huffman_table(self):
        def tree_traverse(current_node, bitstring=''):
            if current_node is None:
                return
            if current_node.is_leaf():
                self.__value_to_bitstring[current_node.value] = bitstring
                return
            tree_traverse(current_node.left_child, bitstring + '0')
            tree_traverse(current_node.right_child, bitstring + '1')

        tree_traverse(self.__root)

    def __calc_freq(self, arr):
        freq_dict = dict()
        for elem in arr:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        return freq_dict
