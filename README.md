<img src="https://github.com/KoreaSecurity/LLM_Threat_Learning/assets/8425791/3bb09293-f197-45e2-8937-5bdb6750cd43" alt="image" width="800px">


![image](https://github.com/KoreaSecurity/LLM_Threat_Learning/assets/8425791/2386fbda-1c37-4dec-a2b7-00ffce7cbd21)


## Usage

```sh
sudo docker build -t llm .
sudo docker run -e OPENAI_API_KEY=your_api_key -p 5000:5000 -p 9089:9089 llm

```

# Project for Practicing LLM Security

Language models (LLMs, Large Language Models) are exposed to various security threats due to their nature and usage. These threats can vary depending on the vulnerabilities within the model itself and the environment in which it operates. Here are some major security threats:

## Data Leakage

- **Training Data Leakage**: LLMs are trained using vast amounts of text data, which may contain sensitive information that could appear in the model's responses. For instance, the model might generate phone numbers or credit card details seen in the training data.
- **Model Exfiltration**: The LLM itself can contain critical information. If improperly accessed or extracted, this information could be leaked.

## Malicious Use

- **Phishing and Social Engineering**: LLMs can be used to craft highly sophisticated phishing messages or fraudulent emails, which can deceive users into divulging sensitive information.
- **Fake Information Generation**: LLMs can generate and disseminate large volumes of fake news or misinformation, potentially causing social unrest or manipulating public opinion.

## Adversarial Attacks

- **Input Data Manipulation**: Attackers can manipulate input data to cause the model to produce incorrect responses. For example, specific patterns of text might be input to make the LLM generate unintended results.
- **Backdoor Attacks**: Malicious code or data can be inserted during the model's training phase, causing the model to act according to the attacker’s intentions under certain conditions.

## Privacy Threats

- **Model Inversion Attack**: Attackers can infer the original input data from the model’s output, potentially exposing personally identifiable information (PII).
- **Model Snooping**: This involves intercepting the data being processed by the model in real-time to obtain sensitive information.

## Resource Misuse

- **Denial of Service (DoS) Attacks**: LLM-based AI services require significant computational resources. Malicious users could overwhelm the service with excessive requests, depleting its resources and disrupting normal usage.

To mitigate these security threats, it is crucial to implement thorough security designs during the model’s development and deployment phases. Establishing monitoring and control systems for model usage is also important. Additionally, educating users and raising awareness about security can be an effective defense strategy.


# LLM 보안 실습을 위한 프로젝트

언어 모델 (LLM, Large Language Model)은 그 특성과 사용 방식 때문에 여러 가지 보안 위협에 노출될 수 있음. 이러한 위협들은 모델 자체의 취약점이나 이를 사용하는 환경에 따라 다양하게 나타날 수 있음. 주요 보안 위협을 몇 가지 설명하겠음:

## 데이터 유출

- **훈련 데이터 유출**: LLM은 대량의 텍스트 데이터를 사용하여 훈련됨. 이 데이터에 포함된 민감한 정보가 모델의 응답에 포함될 가능성이 있음. 예를 들어, 모델이 훈련 데이터에서 본 전화번호나 신용카드 번호를 생성하는 경우가 이에 해당함.
- **모델 반출**: LLM 자체가 중요 정보를 포함할 수 있으므로, 이를 부적절하게 반출하거나 접근하는 경우 기밀이 유출될 수 있음.

## 악의적인 사용

- **피싱 및 소셜 엔지니어링**: LLM을 이용해 매우 정교한 피싱 메시지나 사기 이메일을 작성할 수 있음. 이를 통해 사용자를 속여 민감한 정보를 탈취하는 등의 악의적인 행위가 가능함.
- **허위 정보 생성**: LLM을 통해 가짜 뉴스나 허위 정보를 대량으로 생성하여 배포할 수 있음. 이는 사회적 혼란을 야기하거나 여론을 조작하는 데 사용될 수 있음.

## 적대적 공격 (Adversarial Attacks)

- **입력 데이터 변조**: 공격자가 입력 데이터를 변조하여 모델이 잘못된 응답을 하도록 유도할 수 있음. 예를 들어, 특정 패턴의 텍스트를 입력하여 LLM이 의도하지 않은 결과를 출력하도록 할 수 있음.
- **백도어 공격**: 모델 훈련 시기에 악의적인 코드나 데이터를 삽입하여, 특정 조건 하에 모델이 공격자의 의도대로 작동하도록 할 수 있음.

## 프라이버시 위협

- **모델 반추 공격 (Model Inversion Attack)**: 공격자가 모델의 출력을 통해 원래 입력 데이터를 역으로 추론할 수 있는 방법임. 이를 통해 개인 식별 정보 (PII)가 유출될 수 있음.
- **모델 스니핑 (Model Snooping)**: 모델이 처리하는 데이터를 실시간으로 가로채어 민감한 정보를 획득하는 방법임.

## 리소스 남용

- **서비스 거부 공격 (DoS)**: LLM을 포함한 AI 서비스는 계산 자원이 많이 필요함. 악의적인 사용자가 과도한 요청을 보내 서비스의 자원을 고갈시키고 정상적인 사용을 방해할 수 있음.

이와 같은 보안 위협을 완화하기 위해서는, 모델의 개발 및 배포 과정에서 보안 설계를 철저히 하고, 모델 사용에 대한 모니터링 및 통제 시스템을 구축하는 것이 중요함. 또한, 사용자 교육과 보안 인식을 높이는 것도 중요한 방어 전략 중 하나임.
