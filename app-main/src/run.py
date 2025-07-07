import asyncio
import config as cfg
from guvicorn_logger import Logger
from src.models import Models
from src.postprocess import model_output, adjust_passive

# LOGGING
logger = Logger().configure()

models = Models()

async def run(input: str, gen_params: dict):
    logger.info("Generating Critique..")

    # Run all models concurrently
    res = await asyncio.gather(
        *[models.inference(input, m_n, gen_params) for m_n in cfg.APP_MODELS_STEP_1]
    )

    # Post-Processing
    n_res = {}
    for model_n, output in res:
        n_res[model_n] = model_output(output, model_n)

    n_res[4] = adjust_passive(n_res[4], n_res[6])
    
    # Conclusion Model 5
    model_n = 5
    f_res = await models.inference(input, model_n, gen_params, n_res)
    n_res[model_n] = model_output(f_res[1], model_n)

    # Final Json
    output_json = {
        "introduction": n_res[1],
        "summary": n_res[2],
        "skills": n_res[3],
        "work_history": n_res[4],
        "conclusion": n_res[5]
    }

    logger.info("Finished generating resume")
    return output_json