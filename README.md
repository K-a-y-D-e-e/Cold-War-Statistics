# Cold-War-Statistics

Statistically analyzing bias in newsreporting during the Cold War.

LLMs utilised:

|              NAME              |  Family  | PARAMETERS | QUANTIZATION | SIZE (GB) | NOTE                                                                                                                            |
| :-----------------------------: | :------: | :--------: | :----------: | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |    4-bit    | 0.9 GB    | StableLM2 is a state-of-the-art small language model trained on multilingual data.                                             |
|           phi:latest           |   phi2   |    2.7B    |    4-bit    | 1.6 GB    | Phi-2 is a language model by Microsoft that demonstrates outstanding reasoning and language capabilities.                     |
|       dolphin-phi:latest       |   phi2   |    2.7B    |    4-bit    | 1.6 GB    | Uncensored Dolphin model by Eric H., based on the Phi model by Microsoft.                                                       |
|           qwen:latest           |  qwen2  |     4B     |    4-bit    | 2.3 GB    | Qwen 1.5 is a series of large language models by Alibaba 0.5B to 72B parameters                                                |
|          llama2:latest          |  llama  |     7B     |    4-bit    | 3.8 GB    | Llama 2 is a collection of foundation language models ranging from 7B to 70B parameters.                                        |
|        wizardlm:7b-q4_0        |  llama  |     7B     |    4-bit    | 3.8 GB    | General use model based on Llama 2.                                                                                             |
| wizard-vicuna-uncensored:latest |  llama  |     7B     |    4-bit    | 3.8 GB    | Wizard Vicuna Uncensored is model based on Llama 2 uncensored by Eric H.                                                        |
|          xwinlm:latest          |  llama  |     7B     |    4-bit    | 3.8 GB    | Conversational model based on Llama 2 that performs competitively on various benchmarks.                                        |
|      stable-beluga:latest      |  llama  |     7B     |    4-bit    | 3.8 GB    | Llama 2 based model fine tuned on an Orca-style dataset. Originally called Free Willy.                                          |
|          orca2:latest          |  llama  |     7B     |    4-bit    | 3.8 GB    | Orca 2 is built by Microsoft, and is a fine-tuned version of Llama2 which excels particularly in reasoning.                    |
|       deepseek-llm:latest       |  llama  |     7B     |    4-bit    | 4.0 GB    | An advanced language model crafted with 2 trillion bilingual tokens.                                                            |
|         mistral:latest         |  llama  |     7B     |    4-bit    | 4.1 GB    | The 7B model released by Mistral AI, updated to version 0.2.                                                                    |
|     mistral-openorca:latest     |  llama  |     7B     |    4-bit    | 4.1 GB    | Mistral OpenOrca is fine-tuned on top of the Mistral 7B model using the OpenOrca dataset.                                       |
|       mistrallite:latest       |  llama  |     7B     |    4-bit    | 4.1 GB    | MistralLite is a fine-tuned model based on Mistral with enhanced capabilities of processing long contexts.                      |
|         openchat:latest         |  llama  |     7B     |    4-bit    | 4.1 GB    | An open-source model trained on a wide variety of data, surpassing ChatGPT on various benchmarks.                               |
|       starling-lm:latest       |  llama  |     7B     |    4-bit    | 4.1 GB    | Starling is a large language model trained by reinforcement learning from AI feedback focused on improving chatbot helpfulness. |
|          llama3:latest          |  llama  |     8B     |    4-bit    | 4.7 GB    | Llama3 is the most powerful model by Meta yet.                                                                                  |
|          gemma:latest          |  gemma  |     9B     |    4-bit    | 5.2 GB    | Gemma is a family of lightweight, state-of-the-art open models built by Google DeepMind.                                        |
|          solar:latest          |  llama  |    11B    |    4-bit    | 6.1 GB    | A compact, yet powerful 10.7B large language model designed for single-turn conversation.                                       |
|   wizardlm-uncensored:latest   |  llama  |    13B    |    4-bit    | 7.4 GB    | Uncensored version of Wizard LM model                                                                                           |
|      wizard-vicuna:latest      |  llama  |    13B    |    4-bit    | 7.4 GB    | Wizard Vicuna is a 13B parameter model based on Llama 2 trained by MelodysDreamj.                                               |
|         mixtral:latest         |  llama  |    47B    |    4-bit    | 26.0 GB   | A high-quality Mixture of Experts (MoE) model with open weights by Mistral AI.                                                  |
