
# Flask Web Service
A web interface that processes files and sends results via email.
* **Setup**: 
  1. Create a `.env` file in the `part-3` folder:
     ```env
     EMAIL_ADDRESS=your_email@gmail.com
     EMAIL_PASSWORD=your_gmail_app_password
     ```
  2. Install Web Requirements: `pip install flask python-dotenv`
  3. Run App: `cd part-3 && python app.py`
* **Output**: The app will generate a `result.csv` and mail it to the recipient.

---

## Screenshots
### Web Interface (Part 3)
![Form Screenshot](./part-3/screenshot_form.png)

### Email/Success Output
![Success Screenshot](./part-3/screenshot_success.png)

---
