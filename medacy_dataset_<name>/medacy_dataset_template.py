from pkg_resources import resource_listdir, resource_string, resource_filename, resource_isdir
from medacy.data import Dataset
from os.path import join

package_name = __name__


def load():
    """
    Loads a medaCy compatible Dataset comprised of training and evaluation sets with meta-data.
    :return: Two medaCy Dataset objects corresponding to training and evaluation data respectively, meta_data.
    """

    meta_data = {
        'entities': ['CAD', 'Diabtetes', 'Obese Status', 'Hyperlimidemia', 'Hypertension', 'Medication',
                     'Smoker Status', 'Family History'],
        'relations': ['mention', 'event', 'test', 'symptom', 'ALC', 'glucose', 'BMI', 'high LDL', 'high chol',
                      'high bp'],  # set to None if no relations
    }

    return get_training_dataset(), get_evaluation_dataset(), meta_data


def get_training_dataset():
    """
    :return: a medaCy Dataset object containing this Dataset's designated training data.
    """
    return Dataset(resource_filename(package_name, 'data/training'))


def get_evaluation_dataset():
    """
    Leave the evaluation folder empty if no evaluation data is provided.

    :return: a medaCy Dataset object containing this Dataset's designated evaluation data.
    """
    # if evaluation is empty return None.
    if not resource_isdir(package_name, join('data', 'evaluation')) or not resource_listdir(package_name,
                                                                                            join('data', 'evaluation')):
        return None

    return Dataset(resource_filename(package_name, 'data/evaluation'))
