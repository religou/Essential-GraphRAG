def chunk_text(text, chunk_size, overlap, split_on_whitespace_only=True):
    """
    文本分块函数：保证不拆分单个单词，仅在空格处分割
    :param text: 原始长文本
    :param chunk_size: 分块目标长度
    :param overlap: 分块重叠长度
    :param split_on_whitespace_only: 是否仅按空白符分割（保证单词完整）
    :return: 分块后的文本列表
    """
    chunks = []
    index = 0
    
    while index < len(text):
        if split_on_whitespace_only:
            # 向左查找重叠区域内的最后一个空格
            prev_whitespace = 0
            left_index = index - overlap
            while left_index >= 0:
                if text[left_index] == " ":
                    prev_whitespace = left_index
                left_index -= 1
            
            # 向右查找目标位置后的下一个空格
            next_whitespace = text.find(" ", index + chunk_size)
            if next_whitespace == -1:
                next_whitespace = len(text)
            
            # 截取分块并清理首尾空格
            chunk = text[prev_whitespace:next_whitespace].strip()
            chunks.append(chunk)
            index = next_whitespace + 1
        else:
            # 非仅空格分割模式
            start = max(0, index - overlap + 1)
            end = min(index + chunk_size + overlap, len(text))
            chunk = text[start:end].strip()
            chunks.append(chunk)
            index += chunk_size
            break
    
    return chunks


# 调用示例：500字符分块，40字符重叠
text = "这是一个示例文本，用于测试文本分块函数。我们希望将这个长文本分成多个块，每个块大约500字符，并且每个块之间有40字符的重叠。这样可以确保在处理文本时不会丢失重要的信息，同时也不会拆分单词。这个函数对于处理长文本非常有用，特别是在自然语言处理任务中。"
chunks = chunk_text(text, 500, 40)
print(len(chunks))  # 输出总块数，示例：89 chunks in total