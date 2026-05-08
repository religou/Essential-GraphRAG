# 定义文本块嵌入函数
def embed(texts):
    # 调用 OpenAI 嵌入模型生成向量
    response = open_ai_client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    # 提取并返回所有向量
    return list(map(lambda n: n.embedding, response.data))

# 对文本块进行嵌入，得到向量列表
embeddings = embed(chunks)

# 打印向量列表长度（与文本块数量一致）
print(len(embeddings))  # 89, matching the number of chunks

# 打印单个向量的维度
print(len(embeddings[0]))  # 1536 dimensions