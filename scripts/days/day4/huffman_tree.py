import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # 重载小于运算符，以便在优先队列中进行比较
    def __lt__(self, other):
        return self.freq < other.freq

# 生成哈夫曼树
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

# 生成哈夫曼编码表
def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# 编码文本
def encode_text(text, codebook):
    return ''.join(codebook[char] for char in text)

# 译码文本
def decode_text(encoded_text, root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_text.append(node.char)
            node = root

    return ''.join(decoded_text)

# 主程序
if __name__ == "__main__":
    # (1) 输入短文
    text = """Your long A4 text goes here. This should be a lengthy paragraph with various characters and punctuation marks. This text will be used to demonstrate Huffman encoding and decoding."""
    
    # (2) 统计频率
    frequency = Counter(text)

    # (3) 构建哈夫曼树并生成编码表
    huffman_tree = build_huffman_tree(frequency)
    codebook = generate_codes(huffman_tree)
    
    # (4) 编码短文
    encoded_text = encode_text(text, codebook)
    
    # (5) 输出编码表
    print("Huffman Codes:", codebook)
    
    # 输出编码后的文本
    print("Encoded Text:", encoded_text)
    
    # (6) 译码给定的二进制编码（此处使用刚才生成的编码文本为例）
    decoded_text = decode_text(encoded_text, huffman_tree)
    print("Decoded Text:", decoded_text)
    
    # 任意给出一组长度不小于 1000 位二进制编码
    # 为了演示，这里使用上面编码文本的一部分或全部（确保长度大于等于1000）
    test_encoded_text = encoded_text[:1000]
    decoded_test_text = decode_text(test_encoded_text, huffman_tree)
    print("Decoded Test Text:", decoded_test_text)
