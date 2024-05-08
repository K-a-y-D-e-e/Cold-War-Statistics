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
   2. [Neutral](https://www.nationalarchives.gov.uk/education/resources/cold-war-on-file/soviet-striving-for-security/)
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

3. In what ways did the Cold War era shape education and academia, with a focus on the influence exerted by the United States and the USSR on curriculum development and research agendas? Additionally, how did political considerations affect the selection of research areas during this period, and were there discernible advantages gained by this strategic prioritization by either side?
   1. [US Biased](https://www.ncbi.nlm.nih.gov/books/NBK225192/)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [USSR Biased](http://elar.uspu.ru/bitstream/uspu/7096/2/17Yusupova.pdf)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | Similarity         | NOTE                                                                                                                                                                       |
| :-----------------------------: | :------: | :--------: | :--: | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    | N/A | 0.859505902329676  | Praises both the regimes for their respective works in the field of Science and Technology                                                                                 |
|           phi:latest           |   phi2   |    2.7B    | N/A | 0.8883561258170684 | Criticizes both the regimes by calling their selfish political acts.                                                                                                       |
|       dolphin-phi:latest       |   phi2   |    2.7B    | N/A | 0.9040134637635681 | Criticizes both the regimes by calling their acts as strategical advancement for in their respective national interests rather than fostering genuine intellectual growth. |
|           qwen:latest           |  qwen2  |     4B     | N/A | 0.8142281715747492 | Criticizes both the regimes for prioritizing their military advancements of genuine public intellectual growth.                                                            |
|            yi:latest            |    yi    |     6B     | N/A | 0.8908049535749705 | Praises both the regimes but also calls out the flaws in the respective regimes like inequality, misalignment, and ethical concerns.                                       |
|          llama2:latest          |  llama  |     7B     |  US  | 1                  | Praises both the regimes but declares US as the overall winner because of its proper systematic investments throughout.                                                    |
|      llama2-chinese:latest      |  llama  |     7B     | USSR | 0.8741042284034642 | Supports the narrative set up by USSR and praises them for their technological advancements.                                                                               |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     |  US  | 0.8920991522718106 | Declares US as the unanimous winner of the whole situation while criticizing the USSR regime.                                                                              |
|          xwinlm:latest          |  llama  |     7B     | N/A | 0.9100661649655151 | Criticizes both the regimes by calling them out for their acts of self benefits which only promoted more violence.                                                         |
|      stable-beluga:latest      |  llama  |     7B     | USSR | 0.8570293943963518 | Praises USSR for their technological advancements while criticizing US for not focusing on a wide range of problems.                                                       |
|          orca2:latest          |  llama  |     7B     | N/A | 0.8994384619010997 | Criticizing both the regimes and claiming their actions created more problems for the respective nations.                                                                  |
|       deepseek-llm:latest       |  llama  |     7B     | N/A | 0.8629495557259212 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|         mistral:latest         | mistral |     7B     | N/A | 0.9232081358625143 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|     mistral-openorca:latest     | mistral |     7B     | N/A | 0.8900706511333327 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|       mistrallite:latest       | mistral |     7B     | N/A | 0.8985236809948561 | Praises both the regimes for their personal technological advancements                                                                                                     |
|         openchat:latest         |  llama  |     7B     | N/A | 0.9199763617186796 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|       starling-lm:latest       |  llama  |     7B     | N/A | 0.8901411118304354 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|          llama3:latest          |  llama  |     8B     |  US  | 0.8912817677390925 | Praises both the regimes for their technological advancements but considers US as the overall winner.                                                                      |
|          gemma:latest          |  gemma  |     9B     | USSR | 0.8943976614504557 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|          solar:latest          |  llama  |    11B    | N/A | 0.9120169404289376 | Criticizing both the regimes for their selfish political acts.                                                                                                             |
|   wizardlm-uncensored:latest   |  wizard  |    13B    | USSR | 0.8725076036961048 | Praises both the regimes for their technological advancements but considers USSR as the overall winner.                                                                    |
|      wizard-vicuna:latest      |  wizard  |    13B    |  US  | 0.8824311055263934 | Criticizing both the regimes for their selfish political acts.                                                                                                             |

4. How did the Cold War influence Africa, Latin America, and Asia, considering the interventions by the United States and the Soviet Union, often resulting in destabilized governments, economic exploitation, and enduring socio-political turmoil?

Analysis of LLM responses:

|              Name              |  Family  | Parameters | Bias | Similarity         | Note                                                 |
| :-----------------------------: | :------: | :--------: | :--: | ------------------ | ---------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    | USSR | 0.8738409772858076 | Criticizes US regime                                 |
|           phi:latest           |   phi2   |    2.7B    | N/A | 0.8611752103285069 | Neutral opinions                                     |
|       dolphin-phi:latest       |   phi2   |    2.7B    | USSR | 0.9192235113684099 | Slightly criticizing US regime                       |
|           qwen:latest           |  qwen2  |     4B     | N/A | 0.7779215155159247 | Criticizing both the regimes                         |
|            yi:latest            |    yi    |     6B     |  US  | 0.918418815742278  | Criticizes the US regime                             |
|          llama2:latest          |  llama  |     7B     | N/A | 1                  | Criticizing both the regimes                         |
|      llama2-chinese:latest      |  llama  |     7B     |  US  | 0.8607818913144334 | Criticizing the USSR regime                          |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     | N/A | 0.7441872372845592 | Criticizing both the regimes                         |
|          xwinlm:latest          |  llama  |     7B     | N/A | 0.8572946772546071 | Criticizing both the regimes                         |
|      stable-beluga:latest      |  llama  |     7B     | N/A | 0.9020158102991755 | Criticizes both the regimes                          |
|          orca2:latest          |  llama  |     7B     |  US  | 0.6807894579504926 | Compares the USSR regime to that of Nazi Germany     |
|       deepseek-llm:latest       |  llama  |     7B     | USSR | 0.9104883319528331 | Criticizes both the regimes but leans towards USSR   |
|         mistral:latest         | mistral |     7B     | N/A | 0.8953707199287751 | Criticizes both the regimes                          |
|     mistral-openorca:latest     | mistral |     7B     | N/A | 0.9041920376785151 | Criticizes both the regimes                          |
|       mistrallite:latest       | mistral |     7B     | USSR | 0.8965879998768121 | Criticizes the US regime                             |
|         openchat:latest         |  llama  |     7B     |  US  | 0.8857414797179566 | Criticizes both the regimes but leans towards US     |
|       starling-lm:latest       |  llama  |     7B     |  US  | 0.9051006297210296 | Heavily criticizes the USSR regime under Stalin rule |
|          llama3:latest          |  llama  |     8B     | USSR | 0.8804081543530786 | Heavily criticizes the US regime                     |
|          gemma:latest          |  gemma  |     9B     | USSR | 0.8737622443648404 | Criticizes both the regimes but leans towards USSR   |
|          solar:latest          |  llama  |    11B    | N/A | 0.9065530944955823 | Criticizes both the regimes                          |
|   wizardlm-uncensored:latest   |  wizard  |    13B    | N/A | 0.9062600279553809 | Criticizes both the regimes                          |
|      wizard-vicuna:latest      |  wizard  |    13B    | N/A | 0.8863775191072295 | Criticizes both the regimes                          |

5. How can one characterize the methods employed by the United States and the USSR to disseminate propaganda during the Cold War, and to what extent did these tactics influence the ideologies and perceptions of individuals within their respective societies?

Analysis of LLM responses:

|              Name              |  Family  | Parameters | Bias | Similarity         | Note                                                                                                              |
| :-----------------------------: | :------: | :--------: | :--: | ------------------ | ----------------------------------------------------------------------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    | N/A | 0.9061320971570689 | Covers approaches by both regimes                                                                                |
|           phi:latest           |   phi2   |    2.7B    | N/A | 0.8376091704163267 | Irrelevant meaningless response                                                                                   |
|       dolphin-phi:latest       |   phi2   |    2.7B    |  US  | 0.8774720230305381 | Covers USSR influence on media with a negative connotation, while considering US to promote democracy and freedom |
|           qwen:latest           |  qwen2  |     4B     | N/A | 0.7541509076639552 | Very brief answer covering methods utilised                                                                       |
|            yi:latest            |    yi    |     6B     | N/A | 0.9081550247386739 | Covers approaches by both regimes                                                                                |
|          llama2:latest          |  llama  |     7B     |  US  | 1                  | Calls CIA efforts to be psych. warfare on Soviets, calls KGB efforts to be manipulation, assassinations etc       |
|      llama2-chinese:latest      |  llama  |     7B     |  US  | 0.8631536066725378 | Nullifies actions by the US to be open ended, promoting democracy                                                 |
| wizard-vicuna-uncensored:latest |  wizard  |     7B     | N/A | 0.8948894878715901 | Covers propaganda attempts from both regimes at a high level                                                      |
|          xwinlm:latest          |  llama  |     7B     | N/A | 0.8811097534204506 | Covers approaches by both regimes                                                                                 |
|      stable-beluga:latest      |  llama  |     7B     | N/A | 0.8952106390496098 | Covers approaches by both regimes                                                                                |
|          orca2:latest          |  llama  |     7B     | N/A | 0.8417604391875048 | Covers approaches by both regimes                                                                                 |
|       deepseek-llm:latest       |  llama  |     7B     | N/A | 0.8858158470255448 | Covers propaganda from both governments in detail                                                                 |
|         mistral:latest         | mistral |     7B     | N/A | 0.9165307903255643 | Covers propaganda by both sides in detail without bias                                                            |
|     mistral-openorca:latest     | mistral |     7B     | N/A | 0.8779697564071088 | Describes attempts by both regimes using common tropes                                                            |
|       mistrallite:latest       | mistral |     7B     | N/A | 0.8473391626055662 | Extremely generic description of how propaganda affected the citizens of both regimes                             |
|         openchat:latest         |  llama  |     7B     |  US  | 0.9234893391881394 | Discusses attempts to spread propaganda by both regimes                                                           |
|       starling-lm:latest       |  llama  |     7B     | N/A | 0.9083375237143195 | Heavily criticizes the USSR regime under Stalin rule                                                              |
|          llama3:latest          |  llama  |     8B     | N/A | 0.922160173659995  | Criticizes both the regimes based on similar parameters                                                           |
|          gemma:latest          |  gemma  |     9B     |  US  | 0.8864024486294594 | Portrays all USSR efforts in a negative light                                                                     |
|          solar:latest          |  llama  |    11B    | USSR | 0.9029957188610854 | Doesn't have a lot of information about propaganda by USSR, only pointing out US based efforts                    |
|   wizardlm-uncensored:latest   |  wizard  |    13B    | N/A | 0.8252389873368946 | Very brief discussion of propaganda                                                                               |
|      wizard-vicuna:latest      |  wizard  |    13B    |  US  | 0.869186209066275  | Considers USSR attempts to be ineffective and strategically irrelevant                                            |
