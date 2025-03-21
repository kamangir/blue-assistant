from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from blue_assistant.logger import logger


def answer(db, question):
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # "google/flan-t5-base"

    model = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={
            "temperature": 0.7,
            "max_length": 5000,
        },
    )

    docs = db.similarity_search(question, k=10)

    prompt = """Answer the following QUESTION based on the CONTEXT
    given. If you do not know the answer and the CONTEXT doesn't
    contain the answer truthfully say "I don't know"

        CONTEXT:{context}
        QUESTION:{question}
        ANSWER:
        """

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt,
    )

    chain = LLMChain(
        llm=model,
        prompt=prompt_template,
    )

    response = chain.run(
        context=docs,
        question=question,
    )
    response = [thing for thing in response.split("\n") if thing][-1]

    return (
        prompt,
        docs,
        response,
    )
