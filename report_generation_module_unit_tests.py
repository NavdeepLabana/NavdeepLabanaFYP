import os
import unittest
from unittest.mock import Mock, patch
from fpdf import FPDF
from Report_Generation_Module import ReportGenerator

class TestReportGenerator(unittest.TestCase):

    @patch('Report_Generation_Module.show_success_message')
    @patch('Report_Generation_Module.show_error_message')
    @patch('fpdf.FPDF.output')
    @patch('os.path.exists')
    @patch('fpdf.FPDF.image')
    def test_generate_pdf_report_success(self, mock_image, mock_exists, mock_output, mock_error_message, mock_success_message):
        # Arrange
        questionnaire_mock = Mock()
        questionnaire_mock.totalScore = 85
        questionnaire_mock.get_category_scores.return_value = [[5, 10], [0, 0], [15, 20]]

        text_edit_mock = Mock()
        text_edit_mock.toPlainText.return_value = "Question 1: Yes\nQuestion 2: No\nQuestion 3: Maybe"

        mock_exists.side_effect = lambda filename: filename in [
            os.path.join("Graph", "pie_chart.png"),
            os.path.join("Graph", "line_graph.png"),
            os.path.join("Graph", "bar_graph_category_1.png"),
            os.path.join("Graph", "bar_graph_category_3.png"),
        ]

        report_generator = ReportGenerator(questionnaire_mock, text_edit_mock)

        # Act
        report_generator.generate_pdf_report()

        # Assert
        mock_output.assert_called_once_with("Questionnaire_Report.pdf")
        mock_success_message.assert_called_once_with("PDF report generated: Questionnaire_Report.pdf")
        mock_error_message.assert_not_called()
        self.assertEqual(mock_image.call_count, 4)  # 1 pie chart, 1 line graph, 2 category graphs

    @patch('Report_Generation_Module.show_success_message')
    @patch('Report_Generation_Module.show_error_message')
    @patch('fpdf.FPDF.output')
    @patch('os.path.exists')
    @patch('fpdf.FPDF.image')
    def test_generate_pdf_report_no_graphs(self, mock_image, mock_exists, mock_output, mock_error_message, mock_success_message):
        # Arrange
        questionnaire_mock = Mock()
        questionnaire_mock.totalScore = 85
        questionnaire_mock.get_category_scores.return_value = [[0, 0], [0, 0], [0, 0]]

        text_edit_mock = Mock()
        text_edit_mock.toPlainText.return_value = "Question 1: Yes\nQuestion 2: No\nQuestion 3: Maybe"

        mock_exists.return_value = False

        report_generator = ReportGenerator(questionnaire_mock, text_edit_mock)

        # Act
        report_generator.generate_pdf_report()

        # Assert
        mock_output.assert_called_once_with("Questionnaire_Report.pdf")
        mock_success_message.assert_called_once_with("PDF report generated: Questionnaire_Report.pdf")
        mock_error_message.assert_not_called()
        mock_image.assert_not_called()  # No images should be added

    @patch('Report_Generation_Module.show_success_message')
    @patch('Report_Generation_Module.show_error_message')
    @patch('fpdf.FPDF.output')
    @patch('os.path.exists')
    def test_generate_pdf_report_error(self, mock_exists, mock_output, mock_error_message, mock_success_message):
        # Arrange
        questionnaire_mock = Mock()
        questionnaire_mock.totalScore = 85
        questionnaire_mock.get_category_scores.side_effect = Exception("Test exception")

        text_edit_mock = Mock()
        text_edit_mock.toPlainText.return_value = "Question 1: Yes\nQuestion 2: No\nQuestion 3: Maybe"

        report_generator = ReportGenerator(questionnaire_mock, text_edit_mock)

        # Act
        report_generator.generate_pdf_report()

        # Assert
        mock_output.assert_not_called()
        mock_success_message.assert_not_called()
        mock_error_message.assert_called_once_with("Error generating PDF report: Test exception")

if __name__ == '__main__':
    unittest.main(verbosity=2)
