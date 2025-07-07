import yaml
import config as cfg
from yaml import Loader

def get_templates():
    '''Get templates for Main APP'''
    templates_d = yaml.load((cfg.TEMPLATE_PATH).read_text(), Loader=Loader)
    return templates_d

def get_prompt(input, model_n, res=None):
    templates_d = get_templates()
    base = templates_d["base"]["general"]
    instruction = templates_d["instruction"][f"model_{model_n}"]

    if model_n==5:
        input = templates_d["input"][f"model_{model_n}"]
        intro=res[1]
        summary=res[2]
        key_words=res[3]
        
        work_history=res[4].get("Introduction", "") + " " + res[4].get("Screen Out", "")
        
        input = input.format(
            intro=intro,
            summary=summary,
            key_words=key_words,
            work_history=work_history
        )
    elif model_n==3:
        base = templates_d["base"]["model_3"]

    prompt = base.format(
        instruction=instruction,
        input=input
    )
    return prompt

def get_gen_params(model_n: int):
    gen_params = cfg.GEN_PARAMS
    gen_params["max_new_tokens"] = cfg.MODEL_MAX_TOKENS[model_n]
    return gen_params