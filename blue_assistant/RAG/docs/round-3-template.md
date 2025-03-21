# RAG - round 3

## query pdf

[LangChain_QnA_RAG.ipynb](../../../notebooks/LangChain_QnA_RAG-3.ipynb)

Using [giza.pdf](https://kamangir-public.s3.ca-central-1.amazonaws.com/giza-v1/giza.pdf)

```bash
@RAG query_pdf \
        filename=giza \
        $(@mlflow tags search \
                contains=latest-giza \
                --log 0 \
                --count 1) \
        "What is the importance of Bash in AI? in less than 20 words."
```

set:::object_name giza-v1

metadata:::get:::object_name:::blue_assistant-RAG-query_pdf.ans

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)