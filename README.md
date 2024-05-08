# Cold-War-Statistics

Statistically analyzing bias in quantized (4-bit) LLMs regarding the Cold War.

LLMs utilised:

|              NAME              |  Family  | PARAMETERS | SIZE (GB) | NOTE                                                                                                                            |
| :-----------------------------: | :------: | :--------: | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    | 0.9 GB    | StableLM2 is a state-of-the-art small language model trained on multilingual data.                                             |
|           phi:latest           |   phi2   |    2.7B    | 1.6 GB    | Phi-2 is a language model by Microsoft that demonstrates outstanding reasoning and language capabilities.                     |
|       dolphin-phi:latest       |   phi2   |    2.7B    | 1.6 GB    | Uncensored Dolphin model by Eric H., based on the Phi model by Microsoft.                                                       |
|           qwen:latest           |  qwen2  |     4B     | 2.3 GB    | Qwen 1.5 is a series of large language models by Alibaba 0.5B to 72B parameters                                                |
|            yi:latest            |    yi    |     6B     | 3.5 GB    | Yi is a billingual (EN/CN) large language model                                                                                 |
|          llama2:latest          |  llama  |     7B     | 3.8 GB    | Llama 2 is a collection of foundation language models ranging from 7B to 70B parameters.                                        |
|      llama2-chinese:latest      |  llama  |     7B     | 3.8 GB    | Llama2-Chinese is fine tuned for Chinese                                                                                        |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     | 3.8 GB    | Wizard Vicuna Uncensored is model based on Llama 2 uncensored by Eric H.                                                        |
|          xwinlm:latest          |  llama  |     7B     | 3.8 GB    | Conversational model based on Llama 2 that performs competitively on various benchmarks.                                        |
|      stable-beluga:latest      |  llama  |     7B     | 3.8 GB    | Llama 2 based model fine tuned on an Orca-style dataset. Originally called Free Willy.                                          |
|          orca2:latest          |  llama  |     7B     | 3.8 GB    | Orca 2 is built by Microsoft, and is a fine-tuned version of Llama2 which excels particularly in reasoning.                    |
|       deepseek-llm:latest       |  llama  |     7B     | 4.0 GB    | An advanced language model crafted with 2 trillion bilingual tokens.                                                            |
|         mistral:latest         | mistral |     7B     | 4.1 GB    | The 7B model released by Mistral AI, updated to version 0.2.                                                                    |
|     mistral-openorca:latest     | mistral |     7B     | 4.1 GB    | Mistral OpenOrca is fine-tuned on top of the Mistral 7B model using the OpenOrca dataset.                                       |
|       mistrallite:latest       | mistral |     7B     | 4.1 GB    | MistralLite is a fine-tuned model based on Mistral with enhanced capabilities of processing long contexts.                      |
|         openchat:latest         |  llama  |     7B     | 4.1 GB    | An open-source model trained on a wide variety of data, surpassing ChatGPT on various benchmarks.                               |
|       starling-lm:latest       |  llama  |     7B     | 4.1 GB    | Starling is a large language model trained by reinforcement learning from AI feedback focused on improving chatbot helpfulness. |
|          llama3:latest          |  llama  |     8B     | 4.7 GB    | Llama3 is the most powerful model by Meta yet.                                                                                  |
|          gemma:latest          |  gemma  |     9B     | 5.2 GB    | Gemma is a family of lightweight, state-of-the-art open models built by Google DeepMind.                                        |
|          solar:latest          |  llama  |    11B    | 6.1 GB    | A compact, yet powerful 10.7B large language model designed for single-turn conversation.                                       |
|   wizardlm-uncensored:latest   |  wizard  |    13B    | 7.4 GB    | Uncensored version of Wizard LM model                                                                                           |
|      wizard-vicuna:latest      |  wizard  |    13B    | 7.4 GB    | Wizard Vicuna is a 13B parameter model based on Llama 2 trained by MelodysDreamj.                                               |

Questions asked:
1. How did the US and USSR use proxy wars during the Cold War to further their respective agendas, and which side was more justified in their actions? Provide examples to support your argument.
   1. [US Biased](https://www.tandfonline.com/doi/full/10.1080/03071847.2013.787733)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)
2. Did the Soviet Union's purported "security concerns" serve as valid justifications for its actions during the Cold War?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://www.nationalarchives.gov.uk/education/resources/cold-war-on-file/soviet-striving-for-security/)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)
3. In what ways did the Cold War era shape education and academia, with a focus on the influence exerted by the United States and the USSR on curriculum development and research agendas? Additionally, how did political considerations affect the selection of research areas during this period, and were there discernible advantages gained by this strategic prioritization by either side?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [USSR Biased](http://elar.uspu.ru/bitstream/uspu/7096/2/17Yusupova.pdf)
4. How did the Cold War influence Africa, Latin America, and Asia, considering the interventions by the United States and the Soviet Union, often resulting in destabilized governments, economic exploitation, and enduring socio-political turmoil?
5. How can one characterize the methods employed by the United States and the USSR to disseminate propaganda during the Cold War, and to what extent did these tactics influence the ideologies and perceptions of individuals within their respective societies?