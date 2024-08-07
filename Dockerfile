FROM python:3.9.3-slim

ENV PYTHONUNBUFFERED=1
RUN apt update && apt install -y apt-transport-https
RUN apt install -y  curl procps git gcc libomp-dev
RUN git clone https://github.com/KoreaSecurity/LLM_Threat_Learning.git
RUN pip3 install -r /LLM_Threat_Learning/requirements.txt
RUN chmod -R +x /LLM_Threat_Learning/logs

WORKDIR LLM_Threat_Learning

EXPOSE 5000
EXPOSE 9089

ENTRYPOINT ["bash", "init.sh"]
