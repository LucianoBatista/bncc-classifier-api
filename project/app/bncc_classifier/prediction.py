from project.app.bncc_classifier import preprocessing
import pickle


def predict(text: str) -> str:
    preprocessing_text = preprocessing.PreProcessing(text)
    preprocessing_text.prepro()

    with open("project/resources/ml_model/lr.bin", "rb") as lr:
        pipe = pickle.load(lr)

    with open("project/resources/ml_model/lr_second_model.bin", "rb") as lr_sec:
        pipe_sec = pickle.load(lr_sec)

    input_text = preprocessing_text.clean_df

    result_first = pipe.predict(input_text["clean_item"])
    result_second = pipe_sec.predict(input_text["clean_item"])

    mapping_first_classes = {
        "Arte": 0,
        "Biologia": 1,
        "Ciências": 2,
        "Educação Física": 3,
        "Ensino Religioso": 4,
        "Física": 5,
        "Geografia": 6,
        "História": 7,
        "Inglês": 8,
        "Língua Portuguesa": 9,
        "Matemática": 10,
        "Química": 11,
    }

    mapping_second_classes = {
        "Fundamental I": 0,
        "Fundamental II": 1,
        "Médio & Pré-Vestibular": 2,
    }

    bncc_know_area = [
        key
        for key in mapping_first_classes.keys()
        if mapping_first_classes.get(key) == result_first[0]
    ]

    school_phase = [
        key
        for key in mapping_second_classes.keys()
        if mapping_second_classes.get(key) == result_second[0]
    ]

    payload = {"bncc_know_area": bncc_know_area, "school_phase": school_phase}
    return payload
