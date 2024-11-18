import os.path
import pickle

import paths

save_suffix = ".dat"


def save_data(
        filename: str,
        myobject: object,
        where: str = paths.save_folder,
        suffix: str = save_suffix
):
    with open(os.path.join(where, filename + suffix), "wb") as fo:
        pickle.dump(myobject, fo, protocol=pickle.HIGHEST_PROTOCOL)


def load_data(
        filename: str,
        where: str = paths.save_folder,
        suffix: str = save_suffix
):
    data_file = os.path.join(where, filename + suffix)

    with open(data_file, "rb") as fo:
        return pickle.load(fo)
