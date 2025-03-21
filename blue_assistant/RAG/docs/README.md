# RAG 🔥

## query pdf 🔥

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


```yaml
'        Bash is important in AI as it facilitates command-line operations, automation,
  and integration with Python.'

```

Cons:

- Response is mixed with the prompt. ⚠️
- Multiple deprecations, ⚠️


<details>
<summary>deprecations</summary>

> /Users/kamangir/git/blue-assistant/blue_assistant/RAG/input.py:41: LangChainDeprecationWarning: The class `HuggingFaceEmbeddings` was deprecated in LangChain 0.2.2 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-huggingface package and should be used instead. To use it run `pip install -U :class:`~langchain-huggingface` and import as `from :class:`~langchain_huggingface import HuggingFaceEmbeddings``.
>  embeddings = HuggingFaceEmbeddings()
/Users/kamangir/git/blue-assistant/blue_assistant/RAG/input.py:41: LangChainDeprecationWarning: Default values for HuggingFaceEmbeddings.model_name were deprecated in LangChain 0.2.16 and will be removed in 0.4.0. Explicitly pass a model_name to the HuggingFaceEmbeddings constructor instead.
  embeddings = HuggingFaceEmbeddings()

</details>


🔥 

## web crawl 🚧

🚧

Using [orbital-data-explorer-2025-03-16-xoo5vc](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-16-xoo5vc.tar.gz) from [orbital data explorer](../../script/repository/orbital_data_explorer/docs/README.md).

---

- [round 1](./round-1.md)
- [round 2](./round-2.md)
- [round 3](./round-3.md)
