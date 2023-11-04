import pandas as pd
import difflib
from llama_index import GPTVectorStoreIndex, StorageContext, ServiceContext
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index import Document
import os
import pinecone
from llama_index.node_parser import SimpleNodeParser
from llama_index.vector_stores import PineconeVectorStore
import time

def process_rows_in_batches(input_df, batch_size=10):
    output_data = []

    for i in range(0, len(input_df), batch_size):
        batch = input_df.iloc[i:i + batch_size]
        text_concatenated = ' '.join(batch['text'])
        avg_start = batch['start'].mean()
        avg_end = batch['end'].mean()
        new_id = i
        output_data.append([new_id, text_concatenated, avg_start, avg_end])

    output_df = pd.DataFrame(output_data, columns=['id', 'text', 'start', 'end'])

    return output_df

def calculate_similarity(string1, string2):
    similarity_ratio = difflib.SequenceMatcher(None, string1, string2).ratio()
    similarity_percentage = similarity_ratio * 100

    return similarity_percentage

# find API key in console at app.pinecone.io
os.environ['PINECONE_API_KEY'] = 'be74b604-2693-4cd3-9a96-de7ab4972ee8'
# environment is found next to API key in the console
os.environ['PINECONE_ENVIRONMENT'] = 'gcp-starter'
os.environ['OPENAI_API_KEY'] = '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'  
# platform.openai.com

def process_dataframe(idata,sentences):
    data = process_rows_in_batches(idata,5)
    docs = []
    for i, row in data.iterrows():
        docs.append(Document(
            text=row['text'],
            start = row['start'],
            end = row['end'],
            doc_id=row['id'],
        ))
    parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=20)
    nodes = parser.get_nodes_from_documents(docs)
    # # initialize connection to pinecone
    pinecone.init(
        api_key=os.environ['PINECONE_API_KEY'],
        environment=os.environ['PINECONE_ENVIRONMENT']
    )

    # # create the index if it does not exist already
    index_name = 'summary1'
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(
            index_name,
            dimension=768,
            metric='cosine'
        )

    # # connect to the index
    pinecone_index = pinecone.Index(index_name)
    # we can select a namespace (acts as a partition in an index)
    namespace = '' # default namespace
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    # setup our storage (vector db)
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings

    embed_model = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-base-en")

    service_context = ServiceContext.from_defaults(embed_model=embed_model)

    index = GPTVectorStoreIndex.from_documents(
        docs, storage_context=storage_context,
        service_context=service_context
    )
    query_engine = index.as_query_engine()
    similarities = []
    for s in sentences:
        maxi = 0
        pmaxi = 0
        while pmaxi==0:
            time.sleep(20)
            res = query_engine.query(s)
            string1 = res.get_formatted_sources(10000)[57:].split(" \n\n")[0] 
            for i in range(0,len(nodes)):
                percentage = calculate_similarity(string1, nodes[i].text)
                if(percentage>maxi):
                    pmaxi = percentage
                    maxi = i
        similarities.append(data.iloc[maxi,2])
        
    pinecone.delete_index("summary1")
    return similarities
   

