from . import ml_model_router
from project.app.bncc_classifier import prediction


@ml_model_router.get("/classify/item")
def run_single_prediction(item: str):
    """
    This endpoint will classify one single item.
    :param bncc_item: item to classify
    :return:
    """

    output = prediction.predict(item)
    return output
