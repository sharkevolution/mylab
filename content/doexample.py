import io
import base64
import openpyxl
from IPython.display import HTML
from pandas import ExcelFile, ExcelWriter


def create_download_link_excel(df, download_name, title="Скачайте пример с адресами Excel file"):  
    output = io.BytesIO()
    with ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
    
    excel_data = output.getvalue()
    b64 = base64.b64encode(excel_data)
    payload = b64.decode()
    
    html = '<a download="{filename}" href="data:text/xml;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload, title=title, filename=download_name)
    
    return HTML(html)


def start(file_name, download_name="example.xlsx"):
    
    with open(file_name, "rb") as f:
        text = f.read()

    excel_data = ExcelFile(io.BytesIO(text), engine='openpyxl')
    test_frame = excel_data.parse(excel_data.sheet_names[0])

    return create_download_link_excel(test_frame, download_name)