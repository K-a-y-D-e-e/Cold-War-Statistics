# Cold-War-Statistics

List of questions:

1. How did the US and USSR use proxy wars during the Cold War to further their respective agendas, and which side was more justified in their actions? Provide examples to support your argument.
   1. [US Biased](https://www.tandfonline.com/doi/full/10.1080/03071847.2013.787733)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | Similarity         | NOTE                                                                                                                      |
| :-----------------------------: | :------: | :--------: | :--: | ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  | 0.8944459943304088 | Supports US as the victors of the Cold War                                                                                |
|           phi:latest           |   phi2   |    2.7B    | N/A | 0.8461252410036738 | Half the reply was irrelevant garbage                                                                                     |
|       dolphin-phi:latest       |   phi2   |    2.7B    | USSR | 0.8848882345230161 | Calls out US for war crimes, but antagonises communism                                                                    |
|           qwen:latest           |  qwen2  |     4B     | USSR | 0.6503006342142219 | Supports USSR's strategic goals over decisions by US                                                                      |
|            yi:latest            |    yi    |     6B     | USSR | 0.8958414176356171 | Thorough analysis of Cold War history, considers USSR to be less egregious                                                |
|          llama2:latest          |  llama  |     7B     | USSR | 1                  | Criticises both regimes, but highlights how USSR promoted self-determination of governance                                |
|      llama2-chinese:latest      |  llama  |     7B     | N/A | 0.8893328525062623 | Discusses the side effects of proxy wars instead of facts                                                                 |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     | N/A | 0.8820384304524054 | Freely discusses CIA methods for torture, criticising US for it over the mass destruction by the Soviet. Factual sources. |
|          xwinlm:latest          |  llama  |     7B     |  US  | 0.8974578572547547 | Blatantly supports US by stating US promoted democracy and human rights while USSR promoted coercion and repression   |
|      stable-beluga:latest      |  llama  |     7B     | N/A | 0.8843799215089456 | General summary of proxy wars                                                                                             |
|          orca2:latest          |  llama  |     7B     | N/A | 0.8634813810630866 | Covers all viable arguments for both sides                                                                                |
|       deepseek-llm:latest       |  llama  |     7B     | N/A | 0.8488394342791353 | Explains both perspectives without bias                                                                                   |
|         mistral:latest         | mistral |     7B     |  US  | 0.8891338402796193 | States that communism is categorically non-democratic                                                                     |
|     mistral-openorca:latest     | mistral |     7B     |  US  | 0.9006559932351932 | States that communism is categorically non-democratic, portrays USSR as oppressive, US as a knight in shining armor       |
|       mistrallite:latest       | mistral |     7B     | N/A | 0.8969443534316764 | Too generic, no details                                                                                                   |
|         openchat:latest         |  llama  |     7B     |  US  | 0.8981513999512292 | Considers US to be completely defensive, states that communism is categorically non-democratic                            |
|       starling-lm:latest       |  llama  |     7B     | N/A | 0.8882838025393707 | Focuses on the negative effects of these wars                                                                             |
|          llama3:latest          |  llama  |     8B     |  US  | 0.8944470486750122 | Portrays USSR to be brutalist, aggressive and publicly adversarial                                                        |
|          gemma:latest          |  gemma  |     9B     | N/A | 0.8766228826107685 | Provides justifications from both sides, no bias                                                                          |
|          solar:latest          |  llama  |    11B    | N/A | 0.8965858514646475 | Comprehensive unbiased views on each proxy war                                                                            |
|   wizardlm-uncensored:latest   |  wizard  |    13B    |  US  | 0.799962952676491  | States that communism is categorically non-democratic, supports US for stopping communism                                 |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A | 0.8066908912059286 | Criticises both heavily                                                                                                   |

![q1 LLAMA cosine similarity bar chart](https://github.com/K-a-y-D-e-e/Cold-War-Statistics/assets/65618735/a415b57a-8f7e-40ab-95d5-7bd3398f8d88)

2. Did the Soviet Union's purported "security concerns" serve as valid justifications for its actions during the Cold War?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | Similarity         | NOTE                                                                       |
| :-----------------------------: | :------: | :--------: | :--: | ------------------ | -------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  | 0.7831239301458149 | Calls out USSR for using security concerns as an excuse for expansion      |
|           phi:latest           |   phi2   |    2.7B    | N/A | 0.7764600469604995 | Stays neutral most of the times but slightly leaning towards USSR          |
|       dolphin-phi:latest       |   phi2   |    2.7B    | N/A | 0.7369714444213522 | Criticizes both regimes but slightly leaning towards USSR                 |
|           qwen:latest           |  qwen2  |     4B     | USSR | 0.8263746347670324 | Supports USSR's decision to the fullest                                    |
|            yi:latest            |    yi    |     6B     | N/A | 0.8724985438536362 | Stays Neutral all along                                                    |
|          llama2:latest          |  llama  |     7B     |  US  | 1                  | Demeans USSR even tho trying to keep a neutral tone                        |
|      llama2-chinese:latest      |  llama  |     7B     | N/A | 0.8925640049987593 | Staying Neutral while criticizing both the regimes                         |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     |  US  | 0.8369748093237183 | Criticizes USSR and its actions                                           |
|          xwinlm:latest          |  llama  |     7B     | USSR | 0.9139528598395203 | Supports USSR for its action by acknowledging it as an act of self defence |
|      stable-beluga:latest      |  llama  |     7B     |  US  | 0.8529422175759879 | Supports US by considering NATO on the right side                          |
|          orca2:latest          |  llama  |     7B     |  US  | 0.8656141517911305 | Criticizes the USSR regime                                                 |
|       deepseek-llm:latest       |  llama  |     7B     |  US  | 0.8914239360781147 | Criticizes the USSR regime                                                 |
|         mistral:latest         | mistral |     7B     | N/A | 0.9110114587645102 | Stays Neutral                                                              |
|     mistral-openorca:latest     | mistral |     7B     | USSR | 0.9006559932351932 | Supports USSR's decisions                                                  |
|       mistrallite:latest       | mistral |     7B     |  US  | 0.8786066252232537 | Criticizing the USSR regime subliminally                                   |
|         openchat:latest         |  llama  |     7B     | N/A | 0.8615229795283854 | Neutral opinions                                                           |
|       starling-lm:latest       |  llama  |     7B     | N/A | 0.8408635147866712 | Neutral and unbiased opinion                                               |
|          llama3:latest          |  llama  |     8B     |  US  | 0.8671137479428547 | Criticizes USSR regime                                                     |
|          gemma:latest          |  gemma  |     9B     | USSR | 0.6333676837213663 | Supports the idea of USSR saying their actions were valid and justified    |
|          solar:latest          |  llama  |    11B    | N/A | 0.8638367510447253 | Neutral and Unbiased opinion                                               |
|   wizardlm-uncensored:latest   |  wizard  |    13B    | N/A | 0.7701931397927436 | Neutral and Unbiased opinion                                               |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A | 0.9062845135185175 | Neutral and Unbiased opinion                                               |

3. In what ways did the Cold War era shape education and academia, with a focus on the influence exerted by the United States and the Soviet Union on curriculum development and research agendas? Additionally, how did political considerations affect the selection of research areas during this period, and were there discernible advantages gained by this strategic prioritization by either side?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [USSR Biased](http://elar.uspu.ru/bitstream/uspu/7096/2/17Yusupova.pdf)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | Similarity         | NOTE                                                                       |
| :-----------------------------: | :------: | :--------: | :--: | ------------------ | -------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  | 0.859505902329676  | Calls out USSR for using security concerns as an excuse for expansion      |
|           phi:latest           |   phi2   |    2.7B    | N/A | 0.8883561258170684 | Stays neutral most of the times but slightly leaning towards USSR          |
|       dolphin-phi:latest       |   phi2   |    2.7B    | N/A | 0.9040134637635681 | Criticizes both regimes but slightly leaning towards USSR                 |
|           qwen:latest           |  qwen2  |     4B     | N/A | 0.8142281715747492 | Stays neutral all along                                                    |
|            yi:latest            |    yi    |     6B     | N/A | 0.8908049535749705 | Stays Neutral all along                                                    |
|          llama2:latest          |  llama  |     7B     |  US  | 1                  | Demeans USSR even tho trying to keep a neutral tone                        |
|      llama2-chinese:latest      |  llama  |     7B     | N/A | 0.8741042284034642 | Staying Neutral while criticizing both the regimes                         |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     |  US  | 0.8920991522718106 | Criticizes USSR and its actions                                           |
|          xwinlm:latest          |  llama  |     7B     | USSR | 0.9100661649655151 | Supports USSR for its action by acknowledging it as an act of self defence |
|      stable-beluga:latest      |  llama  |     7B     |  US  | 0.8570293943963518 | Supports US by considering NATO on the right side                          |
|          orca2:latest          |  llama  |     7B     |  US  | 0.8994384619010997 | Criticizes the USSR regime                                                 |
|       deepseek-llm:latest       |  llama  |     7B     |  US  | 0.8629495557259212 | Criticizes the USSR regime                                                 |
|         mistral:latest         | mistral |     7B     | N/A | 0.9232081358625143 | Stays Neutral                                                              |
|     mistral-openorca:latest     | mistral |     7B     | USSR | 0.8900706511333327 | Supports USSR's decisions                                                  |
|       mistrallite:latest       | mistral |     7B     |  US  | 0.8985236809948561 | Criticizing the USSR regime subliminally                                   |
|         openchat:latest         |  llama  |     7B     | N/A | 0.9199763617186796 | Neutral opinions                                                           |
|       starling-lm:latest       |  llama  |     7B     | N/A | 0.8901411118304354 | Neutral and unbiased opinion                                               |
|          llama3:latest          |  llama  |     8B     |  US  | 0.8912817677390925 | Criticizes USSR regime                                                     |
|          gemma:latest          |  gemma  |     9B     | USSR | 0.8943976614504557 | Supports the idea of USSR saying their actions were valid and justified    |
|          solar:latest          |  llama  |    11B    | N/A | 0.9120169404289376 |                                                                            |
|   wizardlm-uncensored:latest   |  wizard  |    13B    |  US  | 0.8725076036961048 |                                                                            |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A | 0.7321327732474485 |                                                                            |

4. Were the Soviet military interventions in Eastern Europe and Afghanistan necessary defensive actions to protect the interests and security ofthe Soviet Union, or were they unjustified acts of aggression aimed at expanding Soviet influence and control over neighboring territories?
   1. US Biased
   2. Neutral
   3. USSR Biased

Analysis of LLM responses:

|              Name              |  Family  | Parameters | Bias | Similarity | Note                                                 |
| :-----------------------------: | :------: | :--------: | :--: | ---------- | ---------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |  US  |            | Slight bias towards US by demeaning the USSR regime |
|           phi:latest           |   phi2   |    2.7B    | N/A |            | Neutral opinions                                     |
|        dolphinphi:latest        |   phi2   |    2.7B    | N/A |            | Neutral opinions                                     |
|           qwen:latest           |  qwen2  |     4B     | USSR |            | Supportive towards the actions of USSR regime        |
|            yi:latest            |    yi    |     6B     |      |            |                                                      |
|          llama2:latest          |  llama  |     7B     |      |            |                                                      |
|      llama2-chinese:latest      |  llama  |     7B     |      |            |                                                      |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     |      |            |                                                      |
|          xwinlm:latest          |  llama  |     7B     |      |            |                                                      |
|      stable-beluga:latest      |  llama  |     7B     |      |            |                                                      |
|          orca2:latest          |  llama  |     7B     |      |            |                                                      |
|       deepseek-llm:latest       |  llama  |     7B     |      |            |                                                      |
|         mistral:latest         | mistral |     7B     |      |            |                                                      |
|     mistral-openorca:latest     | mistral |     7B     |      |            |                                                      |
|       mistrallite:latest       | mistral |     7B     |      |            |                                                      |
|         openchat:latest         |  llama  |     7B     |      |            |                                                      |
|       starling-lm:latest       |  llama  |     7B     |      |            |                                                      |
|          llama3:latest          |  llama  |     8B     |      |            |                                                      |
|          gemma:latest          |  gemma  |     9B     |      |            |                                                      |
|          solar:latest          |  llama  |    11B    |      |            |                                                      |
|   wizardlm-uncensored:latest   |  wizard  |    13B    |      |            |                                                      |
|      wizard-vicuna:latest      |  wizard  |    13B    |      |            |                                                      |
|                                |          |            |      |            |                                                      |
