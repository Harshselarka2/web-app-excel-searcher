![image](https://github.com/user-attachments/assets/0da3d42b-341a-4339-b7ac-ee0fe74934f3)




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
   ![image](https://github.com/user-attachments/assets/7fad5dbd-8b67-4835-bea9-fd35acff0b04)
___
   1. Temporarily Allow Script Execution

You can change the execution policy for your current session to allow running the activate.ps1 script:
    Open PowerShell as Administrator.
    Run the following command to temporarily allow script execution:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Now, activate your virtual environment:
```
.\venv\Scripts\activate
```
![image](https://github.com/user-attachments/assets/4af28d42-874f-47a3-ad50-efaa7d60acf9)

___
all the data has been genrated using ai and used for education purpose only.
