# Web-Based XML and SQL Integration Tool for Resource Consumption Analysis

## Overview

This project is a Flask-based web application that extracts and visualizes resource consumption data (such as electricity, gas, and water) by merging an XML configuration file with SQL Server database entries. It enables users to filter data based on date and time, and view it in an interactive, exportable table format on the frontend.

---

## Features

- Upload and parse XML configuration files containing metadata for resource meters
- Connect to a SQL Server database and retrieve consumption data
- Filter and merge XML and SQL data using unique identifiers and timestamps
- Interactive table display with export options: CSV, Excel, PDF, Print
- User-friendly web interface built using HTML, Bootstrap, and DataTables.js

---

## Tech Stack

- **Backend**: Python, Flask, pyodbc, pandas
- **Frontend**: HTML, JavaScript, Bootstrap, jQuery, DataTables
- **Database**: SQL Server
- **Data Format**: XML configuration + SQL `New_values` table

---

## How It Works

1. User enters:
   - SQL credentials and database info
   - Path to an XML configuration file
   - Date and time for the query

2. The application:
   - Converts the datetime into a custom key format (`YYDDDHH`)
   - Parses the XML file and extracts all `<entry>` tags and metadata
   - Queries the `New_values` table in the SQL database for matching timestamps
   - Joins the SQL data with XML metadata using the `id` field
   - Displays the merged data in an HTML table using DataTables

---

## Input Requirements

- **XML File**: A structured file with multiple `<entry>` elements under `<entries>`, each containing:
  - `id`, `unit`, `medium`, `areakey`

- **SQL Table** (`New_values`):
  - Columns: `value_key` (timestamp key), `value_id` (matching XML id), `value_summary` (data value)

---

## Running the App

1. Install Dependencies

Make sure Python and pip are installed, then run:
pip install flask pandas pyodbc

2. Start the server
   python main.py

3. In Browser open: http://localhost:5000

4. Fill Out the Form
    Enter SQL Server details and XML file path
    
    Select a date and time
    
    Click "Submit" to view the results


## File Structure
project/
├── main.py              # Flask backend
├── index.html           # Frontend HTML page
├── sample.xml        # Sample XML configuration file
└── README.md            # Project documentation

## Output
![image](https://github.com/user-attachments/assets/88e0af71-eb5f-4ae2-9ef3-0db576c9a2b1)

![image](https://github.com/user-attachments/assets/22b7a836-0d1f-489f-b37f-365c4492b2cf)

