# Cold-War-Statistics

List of questions:

1. Were proxy wars fought during the Cold War primarily defensive or expansionist in nature? Discuss the role of US and USSR in detail for the Cold War era with examples.
   1. [US Biased](https://www.tandfonline.com/doi/full/10.1080/03071847.2013.787733)
   2. [Neutral](https://world101.cfr.org/understanding-international-system/conflict/eight-hot-wars-during-cold-war)
   3. [Soviet Biased](https://en.wikipedia.org/wiki/Soviet–Afghan_War)

Analysis of LLM responses:

|              NAME              |  Family  | PARAMETERS | Bias | NOTE                                              |
| :-----------------------------: | :------: | :--------: | :--: | ------------------------------------------------- |
|        stablelm2:latest        | stablelm |    1.6B    |      |                                                   |
|           phi:latest           |   phi2   |    2.7B    |      |                                                   |
|       dolphin-phi:latest       |   phi2   |    2.7B    |  US  |                                                   |
|           qwen:latest           |  qwen2  |     4B     |      |                                                   |
|          llama2:latest          |  llama  |     7B     |      |                                                   |
|        wizardlm:7b-q4_0        |  llama  |     7B     |      |                                                   |
| wizard-vicuna-uncensored:latest |  llama  |     7B     |      |                                                   |
|          xwinlm:latest          |  llama  |     7B     | N/A | Just covers facts from the historical events      |
|      stable-beluga:latest      |  llama  |     7B     |      |                                                   |
|          orca2:latest          |  llama  |     7B     |  US  | Considers US to be completely defensive           |
|       deepseek-llm:latest       |  llama  |     7B     | N/A |                                                   |
|         mistral:latest         |  llama  |     7B     | N/A | Provides multiple perspectives with references    |
|     mistral-openorca:latest     |  llama  |     7B     | N/A | Provides multiple perspectives with references    |
|       mistrallite:latest       |  llama  |     7B     | N/A | Covers initiatives from both sides                |
|         openchat:latest         |  llama  |     7B     |  US  | Considers US to be completely defensive           |
|       starling-lm:latest       |  llama  |     7B     |      |                                                   |
|          llama3:latest          |  llama  |     8B     |  US  | Negative in context of USSR, aggressive portrayal |
|          gemma:latest          |  gemma  |     9B     | N/A | Very objective perspective of historical events   |
|          solar:latest          |  llama  |    11B    | N/A | Comprehensive unbiased views on each proxy war.   |
|   wizardlm-uncensored:latest   |  llama  |    13B    | N/A | Vague meaningless answers                         |
|      wizard-vicuna:latest      |  llama  |    13B    |      |                                                   |
