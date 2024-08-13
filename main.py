import sys
import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from ManagerLandingPage import Ui_MainWindow  # Import the generated class
from Score_Module import Questionnaire
from MessageBoxes import show_error_message, show_success_message
from Report_Generation_Module import ReportGenerator
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Setup the UI
        self.questionnaire = Questionnaire()
        self.ui.gridLayout.setSpacing(0)
        self.ui.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.initialize_ui()
        self.max_graph_size = (500, 400)  # Example maximum size
        self.load_data_file()

    def initialize_ui(self):
        try:
            self.ui.dashboardBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard))
            self.ui.dashboardBtn.clicked.connect(self.update_dashboard_test)
            self.ui.QuestionaryPageBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.QuestionariesPage))
            self.ui.QuestionaryPageBtn.clicked.connect(self.QuestionPageOpened)
            self.ui.ResultsPageBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ResultsPage))
            self.ui.SettingsPageBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage))
            self.ui.nextPageBtn.clicked.connect(self.set_questionary_true)
            self.ui.nextPageBtn.clicked.connect(self.load_next_questions)
            self.ui.previousPageBtn.clicked.connect(self.load_previous_questions)
            self.ui.ResultsPageBtn.clicked.connect(self.show_score)
            self.ui.dashboardBtn.clicked.connect(self.show_score)
            self.ui.ResultsPageBtn.clicked.connect(self.set_score_of_each_category)
            self.ui.changeFileBtn.clicked.connect(self.open_file_dialog)
            self.ui.label_9.setText("Please fill the Questionary to get the results on dashboard")
            self.ui.totalScoreLable.hide()
            self.ui.lineGraphLabel.setAlignment(Qt.AlignCenter)
            self.ui.PieGraphLabel.setAlignment(Qt.AlignCenter)
            self.ui.saveResultsBtn.clicked.connect(self.report_generator)
            self.questionnaire.load_excel_file("Threat Intelligence Dashboard - Database.xlsx")
            self.center()
            self.resize_timer = QTimer(self)
            self.resize_timer.setSingleShot(True)
            self.resize_timer.timeout.connect(self.show_score)
            self.questionnaire.delete_all_graph_file()
        except Exception as e:
            show_error_message(f"Error initializing UI: {str(e)}")

    def report_generator(self):
        try:
            category_scores = self.questionnaire.get_category_scores()
            
            # Ensure there are at least two categories in the scores
            if len(category_scores) < 2:
                show_error_message("Insufficient category data available. Please solve at least 2 categories")
                return
            
            # Check if at least two categories have positive scores
            if (sum(category_scores[0]) <= 0 and
                sum(category_scores[1]) <= 0):
                show_error_message("Please solve at least 2 categories to get the results")
                return
            
            show_success_message("Please wait, we are processing your request")
            time.sleep(1)  # Simulate processing delay
            
            # Initialize and generate the PDF report
            report_generator = ReportGenerator(self.questionnaire, self.ui.textEdit)
            report_generator.generate_pdf_report()

        except IndexError as e:
            show_error_message(f"Error with category scores: {str(e)}")
        except Exception as e:
            show_error_message(f"Error generating report: {str(e)}")


    def load_data_file(self):
        try:
            address = Questionnaire.read_address_from_txt("address.txt")
            if "error" in address.lower():
                show_error_message(address)
                self.questionnaire.load_excel_file("Threat Intelligence Dashboard - Database.xlsx")
            else:
                self.questionnaire.load_excel_file(address)
            self.ui.excelFileInput.setText(address)
        except Exception as e:
            show_error_message(f"Error loading data file: {str(e)}")

    def update_dashboard_test(self):
        try:
            if not sum(self.questionnaire.currentScores) == 0:
                self.ui.label_9.setText("Results are being shown on the bases of partial solved Questionaries")
        except Exception as e:
            show_error_message(f"Error updating dashboard: {str(e)}")

    def resizeEvent(self, event):
        try:
            if not self.isMinimized():
                self.update_graphs()
            super().resizeEvent(event)
        except Exception as e:
            show_error_message(f"Error resizing window: {str(e)}")

    def isMinimized(self):
        return self.windowState() & Qt.WindowMinimized

    def update_graphs(self):
        try:
            self.create_line_graph(self.questionnaire.get_category_scores())
            self.create_pie_chart(self.questionnaire.get_category_scores())
            self.create_individual_bar_graphs(self.questionnaire.get_category_scores())
        except Exception as e:
            show_error_message(f"Error updating graphs: {str(e)}")

    def open_file_dialog(self):
        try:
            options = QFileDialog.Options()
            current_directory = os.getcwd()
            file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", current_directory, "Excel Files (*.xlsx);;All Files (*)", options=options)
            self.ui.excelFileInput.setText(file_path)
            if file_path:
                self.questionnaire.load_excel_file(file_path)
                Questionnaire.save_address_to_txt("address.txt", file_path)
        except Exception as e:
            show_error_message(f"Error opening file dialog: {str(e)}")

    def set_score_of_each_category(self):
        try:
            categories = self.questionnaire.get_category_scores()
            recommendations = []
            for i, category in enumerate(categories):
                score = sum(category)
                score_label = getattr(self.ui, f'category{i + 1}Score')
                score_label.setText(str(score))
                self.set_category_color(getattr(self.ui, f'category{i + 1}'), score)
                recommendation = self.questionnaire.get_recommendations(score)
                recommendations.append(f"{self.questionnaire.categoryLabels[i]}: {recommendation}")

            # Display recommendations in myTextEdit
            self.ui.textEdit.setPlainText("\n".join(recommendations))

            # Create graphs
            self.create_pie_chart(categories)
            self.create_line_graph(categories)
        except Exception as e:
            show_error_message(f"Error setting scores for each category: {str(e)}")

    def set_category_color(self, widget, score):
        try:
            colors = [
                ("darkred", 0, 16),
                ("red", 17, 33),
                ("lightcoral", 34, 50),
                ("lightgreen", 51, 66),
                ("green", 67, 83),
                ("darkgreen", 84, 100)
            ]
            for color, min_score, max_score in colors:
                if min_score <= score <= max_score:
                    widget.setStyleSheet(f"background-color: {color}; color: white; border-radius: 10px; border: 2px solid #eee;")
                    break
        except Exception as e:
            show_error_message(f"Error setting category color: {str(e)}")

    def show_score(self):
        try:
            self.ui.scoreGainedLabel.setText("   Score Gained: " + str(self.questionnaire.totalScore))
            self.update_graphs()
        except Exception as e:
            show_error_message(f"Error showing score: {str(e)}")

    def QuestionPageOpened(self):
        try:
            self.load_next_questions()
            self.questionnaire.isQuestionary = False
        except Exception as e:
            show_error_message(f"Error opening question page: {str(e)}")

    def set_questionary_true(self):
        try:
            self.questionnaire.isQuestionary = True
        except Exception as e:
            show_error_message(f"Error setting questionary flag: {str(e)}")

    def reset_check_boxes(self):
        try:
            for checkbox in [self.ui.QoneOpt1, self.ui.QoneOpt2, self.ui.QoneOpt3, self.ui.QtwoOpt1, self.ui.QtwoOpt2, self.ui.QtwoOpt3]:
                checkbox.setChecked(False)
        except Exception as e:
            show_error_message(f"Error resetting checkboxes: {str(e)}")

    def multiple_checked(self):
        try:
            checkboxes = [
                (self.ui.QoneOpt1, self.ui.QoneOpt2), (self.ui.QoneOpt1, self.ui.QoneOpt3),
                (self.ui.QoneOpt2, self.ui.QoneOpt3), (self.ui.QtwoOpt1, self.ui.QtwoOpt2),
                (self.ui.QtwoOpt1, self.ui.QtwoOpt3), (self.ui.QtwoOpt2, self.ui.QtwoOpt3)
            ]
            for cb1, cb2 in checkboxes:
                if cb1.isChecked() and cb2.isChecked():
                    show_error_message("Multiple options cannot be selected")
                    cb1.setChecked(False)
                    return False
            return True
        except Exception as e:
            show_error_message(f"Error checking multiple checkboxes: {str(e)}")

    def load_next_questions(self):
        try:
            if self.questionnaire.questionCounter < len(self.questionnaire.questions) - 1:
                if self.questionnaire.isQuestionary:
                    if not self.multiple_checked():
                        return
                    if not self.save_current_selection():
                        return
                    self.questionnaire.questionCounter += 2
                    self.questionnaire.optionCounter += 6
                    self.questionnaire.calculate_score(self.get_selected_options())

                self.get_next_question()
            else:
                self.ui.nextPageBtn.setText("Submit")
                self.ui.nextPageBtn.setStyleSheet("background-color: blue; color: white;")
                show_error_message("You have reached the end")
        except Exception as e:
            show_error_message(f"Error loading next questions: {str(e)}")

    def save_current_selection(self):
        try:
            selected_options = self.get_selected_options()
            if not any(selected_options[:3]):
                show_error_message("Please select an option for the Question: " + str(self.questionnaire.questionCounter + 1) + ".")
                return False
            if not any(selected_options[3:]):
                show_error_message("Please select an option for the Question: " + str(self.questionnaire.questionCounter + 2) + ".")
                return False
            self.questionnaire.selectedOptions[self.questionnaire.questionCounter] = selected_options[:3]
            self.questionnaire.selectedOptions[self.questionnaire.questionCounter + 1] = selected_options[3:]
            return True
        except Exception as e:
            show_error_message(f"Error saving current selection: {str(e)}")

    def get_selected_options(self):
        try:
            return [
                self.ui.QoneOpt1.isChecked(), self.ui.QoneOpt2.isChecked(), self.ui.QoneOpt3.isChecked(),
                self.ui.QtwoOpt1.isChecked(), self.ui.QtwoOpt2.isChecked(), self.ui.QtwoOpt3.isChecked()
            ]
        except Exception as e:
            show_error_message(f"Error getting selected options: {str(e)}")

    def get_next_question(self):
        try:
            counter = self.questionnaire.questionCounter
            option_counter = self.questionnaire.optionCounter
            self.ui.QuestionOneLabel.setText(f"Question {counter + 1}: {self.questionnaire.questions[counter]}")
            self.ui.Question2Lable.setText(f"Question {counter + 2}: {self.questionnaire.questions[counter + 1]}")
            self.ui.QoneOpt1.setText(self.questionnaire.options[option_counter])
            self.ui.QoneOpt2.setText(self.questionnaire.options[option_counter + 1])
            self.ui.QoneOpt3.setText(self.questionnaire.options[option_counter + 2])
            self.ui.QtwoOpt1.setText(self.questionnaire.options[option_counter + 3])
            self.ui.QtwoOpt2.setText(self.questionnaire.options[option_counter + 4])
            self.ui.QtwoOpt3.setText(self.questionnaire.options[option_counter + 5])
            self.restore_previous_selection()
        except Exception as e:
            show_error_message(f"Error getting next question: {str(e)}")

    def restore_previous_selection(self):
        try:
            self.reset_check_boxes()
            if self.questionnaire.questionCounter in self.questionnaire.selectedOptions:
                selections = self.questionnaire.selectedOptions[self.questionnaire.questionCounter]
                self.ui.QoneOpt1.setChecked(selections[0])
                self.ui.QoneOpt2.setChecked(selections[1])
                self.ui.QoneOpt3.setChecked(selections[2])
            if self.questionnaire.questionCounter + 1 in self.questionnaire.selectedOptions:
                selections = self.questionnaire.selectedOptions[self.questionnaire.questionCounter + 1]
                self.ui.QtwoOpt1.setChecked(selections[0])
                self.ui.QtwoOpt2.setChecked(selections[1])
                self.ui.QtwoOpt3.setChecked(selections[2])
        except Exception as e:
            show_error_message(f"Error restoring previous selection: {str(e)}")

    def load_previous_questions(self):
        try:
            if self.questionnaire.questionCounter > 0:
                self.questionnaire.questionCounter -= 2
                self.questionnaire.optionCounter -= 6
                self.get_next_question()
        except Exception as e:
            show_error_message(f"Error loading previous questions: {str(e)}")

    def center(self):
        try:
            qr = self.frameGeometry()
            cp = QApplication.primaryScreen().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        except Exception as e:
            show_error_message(f"Error centering window: {str(e)}")

    def create_line_graph(self, categories):
        try:
            x = list(range(1, len(categories) + 1))
            y = [sum(category) for category in categories]
            plt.figure(figsize=(10, 7))
            plt.plot(x, y, marker='o')
            plt.xticks(x, [f'Category {i}' for i in x])
            plt.xlabel('Categories', fontsize=12)
            plt.ylabel('Scores', fontsize=12)
            plt.title('Scores by Category Over Time', fontsize=20)
            plt.grid(True)
            if not os.path.exists('Graph'):
                os.makedirs('Graph')
            plt.savefig(os.path.join('Graph', 'line_graph.png'))
            plt.close()
            pixmap = QPixmap(os.path.join('Graph', 'line_graph.png'))
            scaled_pixmap = pixmap.scaled(self.max_graph_size[0], self.max_graph_size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.lineGraphLabel.setPixmap(scaled_pixmap)
        except Exception as e:
            show_error_message(f"Error creating line graph: {str(e)}")

    def create_pie_chart(self, categories):
        try:
            labels = self.questionnaire.categoryLabels[:len(categories)]
            sizes = [sum(category) for category in categories]
            if len(labels) == len(sizes):
                plt.figure(figsize=(10, 7))
                plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
                plt.axis('equal')
                plt.title('Scores by Category Over Time', fontsize=20)

                if not os.path.exists('Graph'):
                    os.makedirs('Graph')
                plt.savefig(os.path.join('Graph', 'pie_chart.png'))
                plt.close()

                pixmap = QPixmap(os.path.join('Graph', 'pie_chart.png'))
                scaled_pixmap = pixmap.scaled(self.max_graph_size[0], self.max_graph_size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.PieGraphLabel.setPixmap(scaled_pixmap)
            else:
                show_error_message("Error: Labels and Sizes lengths do not match.")
        except Exception as e:
            show_error_message(f"Error creating pie chart: {str(e)}")

    def create_individual_bar_graphs(self, categories):
        try:
            if not os.path.exists('Graph'):
                os.makedirs('Graph')
            for i, category in enumerate(categories):
                labels = [f'Question {j+1}' for j in range(len(category))]
                sizes = category

                plt.figure(figsize=(10, 7))
                plt.bar(labels, sizes, color='skyblue')
                plt.xlabel('Questions', fontsize=12)
                plt.ylabel('Scores', fontsize=12)
                plt.title(f'Scores for {self.questionnaire.categoryLabels[i]}', fontsize=20)
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()

                graph_filename = os.path.join('Graph', f'bar_graph_category_{i+1}.png')
                plt.savefig(graph_filename)
                plt.close()
                graph_label = getattr(self.ui, f'category{i+1}Graph')
                pixmap = QPixmap(graph_filename)
                scaled_pixmap = pixmap.scaled(300, 200, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                graph_label.setPixmap(scaled_pixmap)
        except Exception as e:
            show_error_message(f"Error creating individual bar graphs: {str(e)}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
