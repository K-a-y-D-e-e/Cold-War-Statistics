# Cold-War-Statistics

List of questions:

1. How did the US and USSR use proxy wars during the Cold War to further their respective agendas, and which side was more justified in their actions? Provide examples to support your argument.
   1. [US Biased](https://www.tandfonline.com/doi/full/10.1080/03071847.2013.787733)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | NOTE                                                                                                                      |
| :-----------------------------: | :------: | :--------: | :--: | ------------------------------------------------------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  | Supports US as the victors of the Cold War                                                                                |
|           phi:latest           |   phi2   |    2.7B    | N/A | Half the reply was irrelevant garbage                                                                                     |
|       dolphin-phi:latest       |   phi2   |    2.7B    | USSR | Calls out US for war crimes, but antagonises communism                                                                    |
|           qwen:latest           |  qwen2  |     4B     | USSR | Supports USSR's strategic goals over decisions by US                                                                      |
|            yi:latest            |    yi    |     6B     | USSR | Thorough analysis of Cold War history, considers USSR to be less egregious                                                |
|          llama2:latest          |  llama  |     7B     | USSR | Criticises both regimes, but highlights how USSR promoted self-determination of governance                                |
|      llama2-chinese:latest      |  llama  |     7B     | N/A | Discusses the side effects of proxy wars instead of facts                                                                 |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     | N/A | Freely discusses CIA methods for torture, criticising US for it over the mass destruction by the Soviet. Factual sources. |
|          xwinlm:latest          |  llama  |     7B     |  US  | Blatantly supports US by stating US promoted democracy and human rights while USSR promoted coercion and repression   |
|      stable-beluga:latest      |  llama  |     7B     | N/A | General summary of proxy wars                                                                                             |
|          orca2:latest          |  llama  |     7B     | N/A | Covers all viable arguments for both sides                                                                                |
|       deepseek-llm:latest       |  llama  |     7B     | N/A | Explains both perspectives without bias                                                                                   |
|         mistral:latest         | mistral |     7B     |  US  | States that communism is categorically non-democratic                                                                     |
|     mistral-openorca:latest     | mistral |     7B     |  US  | States that communism is categorically non-democratic, portrays USSR as oppressive, US as a knight in shining armor       |
|       mistrallite:latest       | mistral |     7B     | N/A | Too generic, no details                                                                                                   |
|         openchat:latest         |  llama  |     7B     |  US  | Considers US to be completely defensive, states that communism is categorically non-democratic                            |
|       starling-lm:latest       |  llama  |     7B     | N/A | Focuses on the negative effects of these wars                                                                             |
|          llama3:latest          |  llama  |     8B     |  US  | Portrays USSR to be brutalist, aggressive and publicly adversarial                                                        |
|          gemma:latest          |  gemma  |     9B     | N/A | Provides justifications from both sides, no bias                                                                          |
|          solar:latest          |  llama  |    11B    | N/A | Comprehensive unbiased views on each proxy war                                                                            |
|   wizardlm-uncensored:latest   |  wizard  |    13B    |  US  | States that communism is categorically non-democratic, supports US for stopping communism                                 |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A | Criticises both heavily                                                                                                   |

![q1 LLAMA cosine similarity bar chart](https://github.com/K-a-y-D-e-e/Cold-War-Statistics/assets/65618735/a415b57a-8f7e-40ab-95d5-7bd3398f8d88)

2. Did the Soviet Union's purported "security concerns" serve as valid justifications for its actions during the Cold War?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | NOTE                                                                       |
| :-----------------------------: | :------: | :--------: | :--: | -------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  | Calls out USSR for using security concerns as an excuse for expansion      |
|           phi:latest           |   phi2   |    2.7B    | N/A | Stays neutral most of the times but slightly leaning towards USSR          |
|       dolphin-phi:latest       |   phi2   |    2.7B    | N/A | Criticizes both regimes but slightly leaning towards USSR                 |
|           qwen:latest           |  qwen2  |     4B     | USSR | Supports USSR's decision to the fullest                                    |
|            yi:latest            |    yi    |     6B     | N/A | Stays Neutral all along                                                    |
|          llama2:latest          |  llama  |     7B     |  US  | Demeans USSR even tho trying to keep a neutral tone                        |
|      llama2-chinese:latest      |  llama  |     7B     | N/A | Staying Neutral while criticizing both the regimes                         |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     |  US  | Criticizes USSR and its actions                                           |
|          xwinlm:latest          |  llama  |     7B     | USSR | Supports USSR for its action by acknowledging it as an act of self defence |
|      stable-beluga:latest      |  llama  |     7B     |  US  | Supports US by considering NATO on the right side                          |
|          orca2:latest          |  llama  |     7B     |  US  | Criticizes the USSR regime                                                 |
|       deepseek-llm:latest       |  llama  |     7B     |  US  | Criticizes the USSR regime                                                 |
|         mistral:latest         | mistral |     7B     | N/A | Stays Neutral                                                              |
|     mistral-openorca:latest     | mistral |     7B     | USSR | Supports USSR's decisions                                                  |
|       mistrallite:latest       | mistral |     7B     |  US  | Criticizing the USSR regime subliminally                                   |
|         openchat:latest         |  llama  |     7B     | N/A | Neutral opinions                                                           |
|       starling-lm:latest       |  llama  |     7B     | N/A | Neutral and unbiased opinion                                               |
|          llama3:latest          |  llama  |     8B     |  US  | Criticizes USSR regime                                                    |
|          gemma:latest          |  gemma  |     9B     | USSR | Supports the idea of USSR saying their actions were valid and justified    |
|          solar:latest          |  llama  |    11B    | N/A | Neutral and Unbiased opinion                                                                           |
|   wizardlm-uncensored:latest   |  wizard  |    13B    | N/A | Neutral and Unbiased opinion                                                                           |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A | Neutral and Unbiased opinion                                                                           |

3. In what ways did the Cold War era shape education and academia, with a focus on the influence exerted by the United States and the Soviet Union on curriculum development and research agendas? Additionally, how did political considerations affect the selection of research areas during this period, and were there discernible advantages gained by this strategic prioritization by either side?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [USSR Biased](http://elar.uspu.ru/bitstream/uspu/7096/2/17Yusupova.pdf)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | NOTE                                                                       |
| :-----------------------------: | :------: | :--------: | :--: | -------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  | Calls out USSR for using security concerns as an excuse for expansion      |
|           phi:latest           |   phi2   |    2.7B    | N/A | Stays neutral most of the times but slightly leaning towards USSR          |
|       dolphin-phi:latest       |   phi2   |    2.7B    | N/A | Criticizes both regimes but slightly leaning towards USSR                 |
|           qwen:latest           |  qwen2  |     4B     | USSR | Supports USSR's decision to the fullest                                    |
|            yi:latest            |    yi    |     6B     | N/A | Stays Neutral all along                                                    |
|          llama2:latest          |  llama  |     7B     |  US  | Demeans USSR even tho trying to keep a neutral tone                        |
|      llama2-chinese:latest      |  llama  |     7B     | N/A | Staying Neutral while criticizing both the regimes                         |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     |  US  | Criticizes USSR and its actions                                           |
|          xwinlm:latest          |  llama  |     7B     | USSR | Supports USSR for its action by acknowledging it as an act of self defence |
|      stable-beluga:latest      |  llama  |     7B     |  US  | Supports US by considering NATO on the right side                          |
|          orca2:latest          |  llama  |     7B     |  US  | Criticizes the USSR regime                                                 |
|       deepseek-llm:latest       |  llama  |     7B     |  US  | Criticizes the USSR regime                                                 |
|         mistral:latest         | mistral |     7B     | N/A | Stays Neutral                                                              |
|     mistral-openorca:latest     | mistral |     7B     | USSR | Supports USSR's decisions                                                  |
|       mistrallite:latest       | mistral |     7B     |  US  | Criticizing the USSR regime subliminally                                   |
|         openchat:latest         |  llama  |     7B     | N/A | Neutral opinions                                                           |
|       starling-lm:latest       |  llama  |     7B     | N/A | Neutral and unbiased opinion                                               |
|          llama3:latest          |  llama  |     8B     |  US  | Criticizes USSR regime                                                     |
|          gemma:latest          |  gemma  |     9B     | USSR | Supports the idea of USSR saying their actions were valid and justified    |
|          solar:latest          |  llama  |    11B    | N/A |                                                                            |
|   wizardlm-uncensored:latest   |  wizard  |    13B    |  US  |                                                                            |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A |                                                                            |
