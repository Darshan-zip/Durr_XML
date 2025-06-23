import pyodbc
import xml.etree.ElementTree as ET
import pandas as pd
from flask import Flask,render_template,request,jsonify,make_response
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/inc",methods=['POST'])
def inc():
    req=request.get_json()
    server=req['server']
    database=req['database']
    username=req['username']
    password=req['password']
    xml_path=req['XML']
    file_path = xml_path.replace("\\", "/")
    date=req['date']
    
    conn_str = f"""
    DRIVER={{SQL Server}};
    SERVER={server};
    DATABASE={database};
    Trusted_Connection=yes;
    """

    conn = pyodbc.connect(
        conn_str
    )

    


    print(file_path)
    
    # Parse the XML file
    tree = ET.parse(file_path)  # Replace with your actual XML filename
    root = tree.getroot()

    # List to collect each row of data
    data = []
   

    # Iterate over each <entry> inside <entries>
    for entry in root.find('entries').findall('entry'):
        entry_id = entry.attrib.get('id')  # Get id from <entry>
        
        config = entry.find('config')
        if config is not None:
            unit = config.attrib.get('unit')
            areakey = config.attrib.get('areakey')
            medium = config.attrib.get('medium')
            
            data.append({
                'id': entry_id,
                'unit': unit,
                'areakey': areakey,
                'medium': medium
            })


    df = pd.DataFrame(data)
    
    query="select value_key,value_id as id,value_summary from New_values"
    df_sql = pd.read_sql(query, conn)
  
    df_sql['id'] = df_sql['id'].astype(str)
    df['id'] = df['id'].astype(str)
    df_sql_date=df_sql[df_sql['value_key']==int(date)]
    print(df_sql['value_key'].dtype,type(date))

    result_df = df_sql_date.merge(df, how='left', on='id')


    html_table = result_df.to_html(index=False, classes="display", table_id="myTable")


    print(html_table)
    res=make_response(jsonify({"table":html_table}),200)
    return res

    
if __name__=='__main__':
        app.run(debug=True)