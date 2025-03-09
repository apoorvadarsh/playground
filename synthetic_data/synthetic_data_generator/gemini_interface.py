import synthetic_data_generator

def generate_data_using_gemini(number_of_rows: int):
    response = synthetic_data_generator.get_genai_client().models.generate_content(
        model="gemini-2.0-flash",
        contents= f""" you are a data engineer.
                      You have to create a sample data set of products. The data set must contain
                      the following columns: id, name, category, brand, price, unsold_quntity, sold_quantity, availiable_since.
                      The data set must contain uniform data acorss categories with each category having
                      equal number of products.
                      The data set must contain at least {number_of_rows} rows of data. The data set must be in JSON format.""")
    return response



