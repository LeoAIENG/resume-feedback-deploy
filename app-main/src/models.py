import config as cfg
import json
import aiohttp
from src.utils import get_prompt, get_gen_params
from guvicorn_logger import Logger


logger = Logger().configure()

class Models:
    async def inference(self, input, model_n, gen_params, res=None):
        """
        Perform inference using the specified model with the given input and generation parameters.

        Args:
            input (str): The resume text to be evaluated.
            model_n (str): The name/key of the model to use for inference.
            gen_params (dict): Generation parameters for the model (e.g., temperature, max_tokens).

        Returns:
            dict: A dictionary containing the model name as key and the response data as value.
                  Returns None if the request fails or encounters an error.

        Raises:
            aiohttp.ClientError: If there's an issue with the HTTP request.
        """
        logger.info("*"*100)
        logger.info("*"*100)
        logger.info(f"Generating Model {model_n}...")

        url = cfg.APP_ENDPOINTS[model_n]
        prompt = get_prompt(input, model_n, res=res)
        if not gen_params:
            gen_params = get_gen_params(model_n)
        
        # logger.info("*"*100)
        # logger.info(f"MODEL {model_n}:")
        # logger.info(f"PROMPT: \n {prompt}")

        inf_payload = cfg.INF_PAYLOAD
        if "prompt" in inf_payload:
            inf_payload["prompt"] = prompt
            inf_payload["gen_params"] = gen_params
        else:
            inf_payload["inputs"] = prompt
            inf_payload["parameters"] = gen_params

        payload = json.dumps(inf_payload)

        headers = {
            'Content-Type': 'application/json'
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, headers=headers, data=payload) as response:
                    response.raise_for_status()  # Raise an error for bad status codes

                    # Process the response
                    if response.status == 200:
                        response_data = await response.json()
                        logger.info("*"*100)
                        logger.info("*"*100)
                        logger.info(f"MODEL {model_n} Generated!")
                        # logger.info(f"MODEL {model_n}:")
                        # logger.info(f"RESULT: {response_data}")

                        return (model_n, response_data)
                    else:
                        print(f"Unexpected status code: {response.status}")
                        return None

            except aiohttp.ClientError as e:
                print(f"An error occurred: {e}")
                return None
    async def model_1(self):
        """"""
        pass

    async def model_2(self):
        """"""
        pass

    async def model_3(self):
        """"""
        pass

    async def model_4(self):
        """"""
        pass

    async def model_5(self):
        """"""
        pass