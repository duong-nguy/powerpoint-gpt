import os
import argparse

import dspy

from dspy.retrieve.chromadb_rm import ChromadbRM
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from load_data import load_data


class GenerateAnswer(dspy.Signature):

    context = dspy.InputField(desc="may contain relevant facts")
    question = dspy.InputField()
    answer = dspy.OutputField()

class RAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()

        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate_answer = dspy.ChainOfThought(GenerateAnswer)

    def forward(self, question):
        context = self.retrieve(question).passages
        prediction = self.generate_answer(context=context, question=question)
        return dspy.Prediction(context=context, answer=prediction.answer)


def main(collection_name,persist_directory):
    embedding_function = OpenAIEmbeddingFunction(
        api_key=os.environ.get('OPENAI_API_KEY'),
        model_name="text-embedding-ada-002"
    )

    rm = ChromadbRM(
        collection_name,
        './data/database',
        embedding_function=embedding_function,
        k=5
    )
    # lm = MistralLM("ministral-3b-latest")
    lm = dspy.LM('mistral/ministral-3b-latest')
    # lm = dspy.LM('gpt-3.5-turbo')
    dspy.configure(lm=lm, rm=rm)
    rag = RAG()

    while True:
        query = input("Query: ")
        if len(query) == 0:
            print("Please enter a question. Ctrl+C to Quit.\n")
            continue
        response = rag(query)
        # pred.answer


        print("\n")
        print(response.answer)
        print("\n")



if __name__ == '__main__':

    # Read the data directory, collection name, and persist directory
    parser = argparse.ArgumentParser(
        description="Load documents from a directory into a Chroma collection"
    )

    # Add arguments
    parser.add_argument(
        "--data_directory",
        type=str,
        default="./data/documents",
        help="The directory where your text files are stored",
    )
    parser.add_argument(
        "--collection_name",
        type=str,
        default="barrier-free-it",
        help="The name of the Chroma collection",
    )
    parser.add_argument(
        "--persist_directory",
        type=str,
        default="./data/database",
        help="The directory where you want to store the Chroma collection",
    )

    # Parse arguments
    args = parser.parse_args()

    load_data(
        documents_directory=args.data_directory,
        collection_name=args.collection_name,
        persist_directory=args.persist_directory,
    )

    main(args.collection_name,args.persist_directory)



