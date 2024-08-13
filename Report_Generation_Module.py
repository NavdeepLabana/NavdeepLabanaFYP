import os
from fpdf import FPDF
from MessageBoxes import show_success_message, show_error_message

class ReportGenerator:
    def __init__(self, questionnaire, text_edit):
        self.questionnaire = questionnaire
        self.text_edit = text_edit

    def generate_pdf_report(self):
        try:
            # Create a PDF instance
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            # Title
            pdf.set_font("Arial", style='B', size=16)
            pdf.cell(200, 10, txt="Questionnaire Report", ln=True, align='C')
            # Add total score
            pdf.set_font("Arial", size=12)
            pdf.ln(10)  # Add a line break
            pdf.cell(200, 10, txt=f"Total Score: {self.questionnaire.totalScore}", ln=True)

            # Add questionnaire results
            pdf.ln(10)
            pdf.cell(200, 10, txt="Results:", ln=True)
            results_text = self.text_edit.toPlainText()
            for line in results_text.split('\n'):
                pdf.multi_cell(0, 10, line)

            # Add pie chart
            pdf.ln(10)
            pdf.cell(200, 10, txt="Pie Chart:", ln=True)
            pie_chart_filename = os.path.join("Graph", "pie_chart.png")
            if os.path.exists(pie_chart_filename):
                pdf.image(pie_chart_filename, x=10, w=180)

            # Add line graph
            pdf.ln(10)
            pdf.cell(200, 10, txt="Line Graph:", ln=True)
            line_graph_filename = os.path.join("Graph", "line_graph.png")
            if os.path.exists(line_graph_filename):
                pdf.image(line_graph_filename, x=10, w=180)

            # Add graphs for categories with scores
            pdf.ln(10)
            pdf.cell(200, 10, txt="Category Graphs:", ln=True)
            graph_dir = "Graph"
            categories_scores = self.questionnaire.get_category_scores()
            for i, category in enumerate(categories_scores):
                if sum(category) > 0:  # Only include graphs for categories with scores
                    filename = os.path.join(graph_dir, f'bar_graph_category_{i+1}.png')
                    if os.path.exists(filename):
                        pdf.ln(5)
                        pdf.cell(200, 10, txt=f"Category {i+1} Graph:", ln=True)
                        pdf.image(filename, x=10, w=180)

            # Save PDF
            output_filename = "Questionnaire_Report.pdf"
            pdf.output(output_filename)

            show_success_message(f"PDF report generated: {output_filename}")

        except Exception as e:
            show_error_message(f"Error generating PDF report: {str(e)}")
