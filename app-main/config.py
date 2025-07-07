import random
from pathlib import Path

# ARGS
RUN_TYPE = "container"


# MODELS
APP_MODELS_STEP_1 = [1,2,3,4,6]
APP_MODELS_STEP_2 = [5]


# ENDPOINTS
APP_ENDPOINTS = {
    1 : "<APP_1_ENDPOINT>",
    2 : "<APP_2_ENDPOINT>",
    3 : "<APP_3_ENDPOINT>",
    4 : "<APP_4_ENDPOINT>",
    5 : "<APP_5_ENDPOINT>",
    6 : "<APP_6_ENDPOINT>",
}

# INFERENCE
MODEL_MAX_TOKENS = {
    1: 80,
	2: 150,
    3: 100,
    4: 350,
    5: 50,
    6: 350,
}

GEN_PARAMS = {
    "temperature": 0.58,
    "max_new_tokens": 300,
    "top_p": 0.94,
    "repetition_penalty": 1.15
}

PAYLOAD = {
    "container": 
        {
            "inputs": ...,
            "parameters": ...,
        },
    "debug":
        {
            "prompt": ...,
            "gen_params": ...,
        }
}
INF_PAYLOAD = PAYLOAD[RUN_TYPE]


# APP
TEMPLATE_PATH = Path().cwd() / "templates.yaml"