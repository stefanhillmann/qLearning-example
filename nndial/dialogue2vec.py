from enum import Enum


class DialoguePartner(Enum):
    user = 1,
    system = 2


def generate_one_hot_vector(keys, existing_values):
    v = list()  # create list representing the vector
    # append 1 to v for each key that is in existing values and 0 otherwise
    for key in keys:
        if key in existing_values:
            v.append(1)
        else:
            v.append(0)

    return v


def value_str_to_list(value_str):
    return value_str.strip().split()


def generate_user_turn_vector(turn, concept_names, act_type_names):
    concepts = value_str_to_list(turn['userField'])
    act_types = value_str_to_list(turn['userSA'])

    # generate one-hot vector representation
    v_concepts = generate_one_hot_vector(concept_names, concepts)
    v_act_types = generate_one_hot_vector(act_type_names, act_types)

    return v_concepts + v_act_types
