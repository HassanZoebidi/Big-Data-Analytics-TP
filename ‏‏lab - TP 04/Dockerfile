FROM python:3.10-slim

WORKDIR /app
COPY TP_03.pbix .


RUN pip install flask


RUN echo "from flask import Flask, send_file\n\
app = Flask(__name__)\n\
@app.route('/')\n\
def home():\n\
    return '<h2>TP3 Power BI Report</h2><a href=\"/download\">Download TP3.pbix</a>'\n\
@app.route('/download')\n\
def download():\n\
    return send_file('TP3.pbix', as_attachment=True)\n\
if __name__ == '__main__':\n\
    app.run(host='0.0.0.0', port=5000)" > app.py

EXPOSE 5000
CMD ["python", "app.py"]
