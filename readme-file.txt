
**TextQuest Setup and Run Guide**

**Step 1: Environment Setup**
1. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - On Unix/Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

**Step 2: Install Dependencies**
- Install required packages using pip:
  ```bash
  pip install flask numpy scikit-learn flask-talisman gunicorn
  ```

**Step 3: Prepare Directories**
- Create necessary directories for data and logs (if your application requires):
  ```bash
  mkdir -p data logs
  ```

**Step 4: Data Preparation**
- Ensure your `tfidf_model.pkl` and `output.json` (or equivalent data files) are placed in the `data` directory.

**Step 5: Run the Flask Application**
- Start the Flask server to serve your application:
  ```bash
  python3 search_api.py
  ```

**Step 6: Access the Application**
- Open a web browser and go to `http://localhost:5000` to interact with the TextQuest application.

**Optional Step: Clean Up**
- When you're done, deactivate the virtual environment and remove it if necessary:
  ```bash
  deactivate
  rm -rf venv
  ```
