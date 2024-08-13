import pandas as pd
import glob
from Report_Generation_Module import os

class Questionnaire:
    def __init__(self):
        self.excelFilePath = ''
        self.questions = []
        self.options = []
        self.optionScores = []
        self.questionIds = []
        self.currentScores = []
        self.totalScore = 0
        self.selectedOptions = {}
        self.questionCounter = 0
        self.optionCounter = 0
        self.isQuestionary = False
        self.categoryLabels=['Understanding and Implementing GDPR Compliance','Information Security Management','Training and Awareness','Documentation and Policy Management','Technical and Organizational Measures','Compliance and Audit']

    def load_excel_file(self, file_path):
        df = pd.read_excel(file_path, header=1).dropna()
        for index, row in df.iterrows():
            self.questionIds.append(row['QuestionID'])
            self.questions.append(row['QuestionText'])
            self.options.extend([row['Option 1'], row['Option 2'], row['Option 3']])
            self.optionScores.extend([row['Option1 (Score)'], row['Option 2 (Score)'], row['Option 3 (Score)']])

    def delete_all_graph_file(self):
        
        files = glob.glob('Graph/*')
        for f in files:
            os.remove(f)

    def calculate_score(self, selected_options):
        current_scores = []
        for i, selected in enumerate(selected_options):
            if selected:
                current_scores.append(self.optionScores[self.optionCounter + i])
        self.currentScores.extend(current_scores)
        self.totalScore += sum(current_scores)

    def get_category_scores(self):
        categories = [self.currentScores[i:i+10] for i in range(0, len(self.currentScores), 10)]
        return categories

    def get_recommendations(self, score):
        if score < 17:
            return "Consider improving your knowledge in this area."
        elif score < 34:
            return "You have some understanding, but there's room for improvement."
        elif score < 51:
            return "Good knowledge, but keep refining your skills."
        elif score < 67:
            return "Very good! You are quite proficient in this area."
        elif score < 84:
            return "Excellent work! You have strong expertise in this area."
        else:
            return "Outstanding! You are an expert in this category."

    @staticmethod
    def read_address_from_txt(file_path):
        try:
            with open(file_path, 'r') as file:
                address = file.readline().strip()
            return address
        except FileNotFoundError:
            return f"Error: The file {file_path} does not exist."
        except Exception as e:
            return f"Error: An unexpected error occurred: {e}"
        
    @staticmethod
    def save_address_to_txt(file_path, address):
        try:
            with open(file_path, 'w') as file:
                file.write(address)
            print(f"Address saved to {file_path}")
        except Exception as e:
            return f"Error: An unexpected error occurred: {e}"
