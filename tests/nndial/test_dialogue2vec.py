import unittest
from nndial import dialogue2vec as d2v


class TestDialogue2Vec(unittest.TestCase):

    def test_generate_one_hot_vector_all_keys(self):
        keys = ['a', 'b', 'c', 'd']
        values = ['a', 'b', 'c', 'd']
        expected_vector = [1, 1, 1, 1]

        generated_vector = d2v.generate_one_hot_vector(keys, values)
        self.assertEqual(generated_vector, expected_vector, 'Wrong vector was generated')

    def test_generate_one_hot_vector_empty_values(self):
        keys = ['a', 'b', 'c', 'd']
        values = []
        expected_vector = [0, 0, 0, 0]

        generated_vector = d2v.generate_one_hot_vector(keys, values)
        self.assertEqual(generated_vector, expected_vector, 'Wrong vector was generated')

    def test_generate_one_hot_vector_one_value(self):
        keys = ['a', 'b', 'c', 'd']
        values = ['b']
        expected_vector = [0, 1, 0, 0]

        generated_vector = d2v.generate_one_hot_vector(keys, values)
        self.assertEqual(generated_vector, expected_vector, 'Wrong vector was generated')

    def test_generate_one_hot_vector_unknown_value(self):
        keys = ['a', 'b', 'c', 'd']
        values = ['d']
        expected_vector = [0, 1, 0, 0]

        generated_vector = d2v.generate_one_hot_vector(keys, values)
        self.assertEqual(generated_vector, expected_vector, 'Wrong vector was generated')

    def test_generate_one_hot_vector_empty_keys(self):
        keys = []
        values = ['a']
        expected_vector = []

        generated_vector = d2v.generate_one_hot_vector(keys, values)
        self.assertEqual(generated_vector, expected_vector, 'Wrong vector was generated')

    def test_value_str_to_list_no_values(self):
        self.assertListEqual(d2v.value_str_to_list(''), [], 'Result must contain no items')

    def test_value_str_to_list_one_space(self):
        self.assertListEqual(d2v.value_str_to_list(' '), [], 'Result must contain no items')

    def test_value_str_to_list_two_spaces(self):
        self.assertListEqual(d2v.value_str_to_list('  '), [], 'Result must contain no items')

    def test_value_str_to_list_three_spaces(self):
        self.assertListEqual(d2v.value_str_to_list('   '), [], 'Result must contain no items')

    def test_value_str_to_list_values_1(self):
        self.assertListEqual(d2v.value_str_to_list('a'), ['a'], 'Result must contain the value')

    def test_value_str_to_list_values_2(self):
        self.assertListEqual(d2v.value_str_to_list('a b'), ['a', 'b'], 'Result must contain two values in right order')

    def test_value_str_to_list_values_3(self):
        self.assertListEqual(d2v.value_str_to_list('a    b'), ['a', 'b'], 'Result must contain two values in right order')

    def test_value_str_to_list_values_4(self):
        self.assertListEqual(d2v.value_str_to_list(' a b '), ['a', 'b'], 'Result must contain two values in right order')

    def test_value_str_to_list_values_5(self):
        self.assertListEqual(d2v.value_str_to_list('a bc'), ['a', 'bc'], 'Result must contain two values in right order')

    def test_generate_user_turn_vector(self):
        turn = dict()
        turn['userField'] = 'a c '
        turn['userSA'] = 'f k'
        concepts = ['a', 'b', 'c', 'd']
        dialogue_act_types = ['e', 'f', 'g', 'h', 'i', 'j', 'k']
        expected_vector = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]

        self.assertListEqual(d2v.generate_user_turn_vector(turn, concepts, dialogue_act_types), expected_vector,
                             'Wrong user turn vector was generated')



