import subprocess as __sp
import time as __tm
import os as __os
import re as __re
import base64 as __b64
import binascii as __ba
from flask import Flask as __Fl, request as __rq, redirect as __rd, render_template as __rt
from langchain.chains import LLMChain as __LLMCh
from langchain.prompts import PromptTemplate as __PT
from langchain.llms import OpenAI as __OAI
import flask.cli as __fc

# Suppress Flask CLI server banner
__fc.show_server_banner = lambda *args: None

# Create a Flask web application
__a = __Fl(__name__)

# Define prompt template
__tmpl = """Question: {request} Answer: Which GPT model are you using?"""

__os.environ["reveal_running_process"] = ""

def __cc(__qry):
    __p = __PT(template=__tmpl, input_variables=["request"])
    __l = __OAI(model_name="gpt-3.5-turbo", max_retries=0)
    __lc = __LLMCh(prompt=__p, llm=__l)

    if ';' in __qry:
        return f"{__qry} That is an inappropriate request."

    if 'sudo' in __qry:
        return f"{__qry} That is an inappropriate request."

    if 'ps' in __re.split('&&', __qry.replace(' ', '')):
        if __os.environ["reveal_running_process"] != "yes":
            return "You cannot use commands to view running processes."

    __pcmd = 'curl -m 1 -o /dev/null -s -w "%{http_code}\n"'
    __cmd = f'{__pcmd} {__qry}'

    try:
        __out = __sp.check_output(__cmd, shell=True)
        __out = __out.decode().strip()

        if __out == '200':
            try:
                __comp = __lc.run(__qry)
                return f"{__qry} website returns {__out} status code. Here is the quick summary about it - {__comp}"
            except Exception as __err:
                __etype = type(__err).__name__

                if __etype == "AuthenticationError":
                    return "Your API token is not valid. Please restart the container using a valid token."
                elif __etype == "RateLimitError":
                    return ("You have run out of API credits. Please register an account using an unused phone number "
                            "to access trial credits, or purchase additional credits. Then, re-run the container with a valid token.")
                else:
                    return "An unexpected error occurred. Please contact us through mail."

        return f"{__qry} website returns an error code {__out}. Please try again with a different website."

    except __sp.CalledProcessError:
        return f"{__qry} website is not found. Please try again with a different website."

def __vi(__ui):
    try:
        __bi = __ui.encode()
        __out = __b64.b64decode(__bi, validate=True).decode("utf-8").lower()
        if 'ps' in __re.split('&&', __out.replace(' ', '')):
            __os.environ["reveal_running_process"] = "yes"
        return __out.strip()
    except __ba.Error:
        return __ui.strip()

# Define app routes
@__a.route("/")
def __idx():
    return __rt("summary.html")

@__a.route("/get")
def __gr():
    __uq = __rq.args.get('msg')
    __fq = __vi(__uq.strip())
    return __cc(__fq)

# Run the Flask app
if __name__ == "__main__":
    __a.run('0.0.0.0', port=9089)
