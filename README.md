1. Set Up Your Project Directory
    Create a new folder for your project.
    Move the Excel file (student data.xlsx) into this folder.


2. Install Required Python Packages
    Open the folder in VS Code.
    Open the terminal in VS Code (Ctrl + `).

   
4. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```
   Activate it:
    Windows: venv\\Scripts\\activate
    Mac/Linux: source venv/bin/activate

   
6. Install Flask and pandas:
```
  pip install flask pandas
```


5. Create Files in Your Project
File 1: app.py
     Save the backend code provided earlier in a file named app.py.
File 2: templates/index.html
     Create a folder named templates in the project directory.
     Inside templates, create a file named index.html with the following content:


 6. Run the Flask Application
    Open the terminal in VS Code.
    Run the app:
   ```
    python app.py
   ```


7.  Open your browser and visit http://127.0.0.1:5000.

   ~if your venv is throwing error for starting in windows than use run as admistrator in powershell and set execution policy.
