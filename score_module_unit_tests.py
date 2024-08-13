import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from Score_Module import Questionnaire

class TestQuestionnaire(unittest.TestCase):

    def setUp(self):
        self.q = Questionnaire()
        
    def test_initialization(self):
        self.assertEqual(self.q.excelFilePath, '')
        self.assertEqual(self.q.questions, [])
        self.assertEqual(self.q.options, [])
        self.assertEqual(self.q.optionScores, [])
        self.assertEqual(self.q.questionIds, [])
        self.assertEqual(self.q.currentScores, [])
        self.assertEqual(self.q.totalScore, 0)
        self.assertEqual(self.q.selectedOptions, {})
        self.assertEqual(self.q.questionCounter, 0)
        self.assertEqual(self.q.optionCounter, 0)
        self.assertFalse(self.q.isQuestionary)
        self.assertEqual(self.q.categoryLabels, [
            'Understanding and Implementing GDPR Compliance',
            'Information Security Management',
            'Training and Awareness',
            'Documentation and Policy Management',
            'Technical and Organizational Measures',
            'Compliance and Audit'
        ])

    @patch('pandas.read_excel')
    def test_load_excel_file(self, mock_read_excel):
        data = {
            'QuestionID': [1, 2],
            'QuestionText': ['What is GDPR?', 'What is data security?'],
            'Option 1': ['Option 1A', 'Option 1B'],
            'Option 2': ['Option 2A', 'Option 2B'],
            'Option 3': ['Option 3A', 'Option 3B'],
            'Option1 (Score)': [1, 2],
            'Option 2 (Score)': [2, 3],
            'Option 3 (Score)': [3, 4]
        }
        df = pd.DataFrame(data)
        mock_read_excel.return_value = df
        
        self.q.load_excel_file('fake_path.xlsx')
        
        self.assertEqual(self.q.questionIds, [1, 2])
        self.assertEqual(self.q.questions, ['What is GDPR?', 'What is data security?'])
        self.assertEqual(self.q.options, ['Option 1A', 'Option 2A', 'Option 3A', 'Option 1B', 'Option 2B', 'Option 3B'])
        self.assertEqual(self.q.optionScores, [1, 2, 3, 2, 3, 4])

    def test_calculate_score(self):
        self.q.optionScores = [1, 2, 3, 4, 5, 6]
        selected_options = [True, False, True]
        
        self.q.calculate_score(selected_options)
        
        self.assertEqual(self.q.currentScores, [1, 3])
        self.assertEqual(self.q.totalScore, 4)

    def test_get_category_scores(self):
        self.q.currentScores = list(range(30))
        
        categories = self.q.get_category_scores()
        
        self.assertEqual(len(categories), 3)
        self.assertEqual(categories[0], list(range(10)))
        self.assertEqual(categories[1], list(range(10, 20)))
        self.assertEqual(categories[2], list(range(20, 30)))

    def test_get_recommendations(self):
        self.assertEqual(self.q.get_recommendations(10), "Consider improving your knowledge in this area.")
        self.assertEqual(self.q.get_recommendations(20), "You have some understanding, but there's room for improvement.")
        self.assertEqual(self.q.get_recommendations(40), "Good knowledge, but keep refining your skills.")
        self.assertEqual(self.q.get_recommendations(60), "Very good! You are quite proficient in this area.")
        self.assertEqual(self.q.get_recommendations(80), "Excellent work! You have strong expertise in this area.")
        self.assertEqual(self.q.get_recommendations(90), "Outstanding! You are an expert in this category.")

    @patch('builtins.open', new_callable=mock_open, read_data="123 Main St")
    def test_read_address_from_txt(self, mock_file):
        address = self.q.read_address_from_txt('fake_path.txt')
        self.assertEqual(address, "123 Main St")

    @patch('builtins.open', new_callable=mock_open)
    def test_read_address_from_txt_file_not_found(self, mock_file):
        mock_file.side_effect = FileNotFoundError
        address = self.q.read_address_from_txt('fake_path.txt')
        self.assertEqual(address, "Error: The file fake_path.txt does not exist.")

    @patch('builtins.open', new_callable=mock_open)
    def test_read_address_from_txt_unexpected_error(self, mock_file):
        mock_file.side_effect = Exception('Unexpected error')
        address = self.q.read_address_from_txt('fake_path.txt')
        self.assertEqual(address, "Error: An unexpected error occurred: Unexpected error")

    @patch('builtins.open', new_callable=mock_open)
    def test_save_address_to_txt(self, mock_file):
        result = self.q.save_address_to_txt('fake_path.txt', "123 Main St")
        mock_file.assert_called_once_with('fake_path.txt', 'w')
        mock_file().write.assert_called_once_with("123 Main St")
        self.assertIsNone(result)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_address_to_txt_unexpected_error(self, mock_file):
        mock_file.side_effect = Exception('Unexpected error')
        result = self.q.save_address_to_txt('fake_path.txt', "123 Main St")
        self.assertEqual(result, "Error: An unexpected error occurred: Unexpected error")

if __name__ == '__main__':
    unittest.main(verbosity=2)
