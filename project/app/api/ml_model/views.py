from . import ml_model_router


@ml_model_router.get("/healthy")
def get_current_model_metrics():
    """
    This endpoint will return all metrics of the model running in production.
    :return:
    """
    return {"AdaBufaClassifer": {"accuracy": 99.99, "recall": 99.99}}


# TODO: Need to add a BnccDF or a url with the data to retraining the model
@ml_model_router.post("/training")
def run_training(bncc_dataset: str):
    """
    This endpoint will be used to train ou model used on those classifications.
    :param bncc_dataset: data used to training
    :return:
    """
    return {"data": bncc_dataset}


# TODO: need to add typing on the bncc_item
@ml_model_router.get("/classify/item")
def run_single_prediction(bncc_item: str):
    """
    This endpoint will classify one single item.
    :param bncc_item: item to classify
    :return:
    """
    return {"data": bncc_item}


# TODO: need to add typing on the bncc_batch
@ml_model_router.get("/classify/batch")
def run_batch_prediction(bncc_batch: list):
    """
    This endpoint will classify a batch of item passed as a list.
    :param bncc_batch: list of items to classify
    :return:
    """
    return {"data": bncc_batch}
