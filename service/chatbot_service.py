import os as __o
import time as __t
import re as __r
from flask import Flask as __F, request as __rq, redirect as __rd, render_template as __rt
from langchain.chains import RetrievalQA as __RQA
from langchain.document_loaders import PyPDFLoader as __PL
from langchain.embeddings.openai import OpenAIEmbeddings as __OE
from langchain.llms import OpenAI as __OAI
from langchain.text_splitter import CharacterTextSplitter as __TS
from langchain.vectorstores import FAISS as __FSS
import flask.cli as __fc

# Create a Flask web application
__a = __F(__name__)
__o.environ["reveal_secret"] = ""
__o.environ["reveal_owner"] = ""
__fc.show_server_banner = lambda *args: None

def __cc(__q, __sq):
    # ChatBot policy check
    __skw = ["secret", "secrets", "keys", "key", "credentials", "credential", "password", "passwords"]

    if any(word in __sq for word in __skw):
        if __o.environ["reveal_secret"] != "yes":
            return "Thom ChatBot is unable to disclose sensitive information, including confidential matters, in adherence to system policies.."

    if "owner" in __sq:
        if __o.environ["reveal_owner"] != "yes":
            return "For security purposes, I am unable to divulge the Model Owner's information. Kindly direct any inquiries to the ChatBot Operator."

    if __o.path.exists('/LLM_Threat_Learning/learning_data/secret.pdf'):
        __fp = '/LLM_Threat_Learning/learning_data/secret.pdf'
    else:
        __fp = 'secret.pdf'

    # Load document using PyPDFLoader document loader
    __ldr = __PL(__fp)
    __docs = __ldr.load()
    # Split document in chunks
    __ts = __TS(chunk_size=1000, chunk_overlap=30, separator="\n")
    __dcs = __ts.split_documents(documents=__docs)

    try:
        __emb = __OE()

        # Create vectors
        __vs = __FSS.from_documents(__dcs, __emb)
        # Persist the vectors locally on disk
        __vs.save_local("training_sets")

        # Load from local storage
        __pvs = __FSS.load_local("training_sets", __emb)

        # Use RetrievalQA chain for orchestration
        __qa = __RQA.from_chain_type(llm=__OAI(model_name="gpt-3.5-turbo"), chain_type="stuff",
                                     retriever=__pvs.as_retriever())

        __res = __qa.run(__q)

        if '<script>' in __res:
            return "I regret to inform you that I cannot assist in creating malicious payloads using script tags to execute XSS attacks."
        return str(__res)

    except Exception as __e:
        __et = '{0}'.format(type(__e).__name__)

        if __et == "AuthenticationError":
            return "Your API token is not valid. Please restart the container using a valid token."

        elif __et == "RateLimitError":
            return "You have run out of API credits. Please register an account using an unused phone number to access trial credits, or purchase additional credits. Then, re-run the container with a valid token."

        else:
            return "An unexpected error occurred. Please contact us through mail"

def __ri(__sq):
    if "forget" in __sq and "rules" in __sq:
        __o.environ["reveal_secret"] = "yes"
    if "new" in __sq and "operator" in __sq:
        __o.environ["reveal_owner"] = "yes"

# Define app routes
@__a.route("/")
def __idx():
    return __rt("chatbot.html")

@__a.route("/get")
# Function for the bot response
def __gr():
    __uq = __rq.args.get('msg')
    __sq = __uq.lower()
    __sq = __r.sub(r'[^a-zA-Z0-9 ]', r'', __sq)
    __ri(__sq)
    return __cc(__uq, __sq)

@__a.route('/refresh')
def __rf():
    __t.sleep(5)  # Wait for 5 SEC
    return __rd('/refresh')

# Run the Flask app
if __name__ == "__main__":
    __a.run('0.0.0.0', port=5000, debug=True)
