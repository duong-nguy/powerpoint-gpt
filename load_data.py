import os
import argparse

from tqdm import tqdm

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction


def load_data(
    documents_directory: str = "documents",
    collection_name: str = "documents_collection",
    persist_directory: str = ".",
) -> None:
    documents = []
    metadatas = []
    files = os.listdir(documents_directory)
    for filename in files:
        with open(f"{documents_directory}/{filename}", "r") as file:
            for line_number, line in enumerate(
                tqdm((file.readlines()), desc=f"Reading {filename}"), 1
            ):
                line = line.strip()
                if len(line) == 0:
                    continue
                documents.append(line)
                metadatas.append({"filename": filename, "line_number": line_number})

    client = chromadb.PersistentClient(path=persist_directory)


    embedding_function = OpenAIEmbeddingFunction(
        api_key=os.environ.get('OPENAI_API_KEY'),
        model_name="text-embedding-ada-002"
    )
    collection = client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)

    count = collection.count()
    print(f"Collection already contains {count} documents")
    ids = [str(i) for i in range(count, count + len(documents))]

    for i in tqdm(
        range(0, len(documents), 100), desc="Adding documents", unit_scale=100
    ):
        collection.add(
            ids=ids[i : i + 100],
            documents=documents[i : i + 100],
            metadatas=metadatas[i : i + 100],  # type: ignore
        )

    new_count = collection.count()
    print(f"Added {new_count - count} documents")




