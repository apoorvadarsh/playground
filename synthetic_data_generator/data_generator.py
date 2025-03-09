from .gemini_interface import generate_data_using_gemini
from .excel_exporter import export_to_excel
import io

def generate_data(number_of_rows: int):
    response= generate_data_using_gemini(number_of_rows)
    json_response = io.StringIO(response.text.replace("```json", "").replace("```", ""))
    export_to_excel(json_response)
