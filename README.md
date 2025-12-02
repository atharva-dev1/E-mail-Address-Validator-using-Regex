
# 📧 Email Validator in Python

A simple and efficient Python script that validates email addresses using **Regular Expressions (RegEx)**.
This project is perfect for beginners learning Python, RegEx, input validation, and basic pattern matching.

---
# Screenshot of the Code
<img width="1499" height="888" alt="image" src="https://github.com/user-attachments/assets/9e84ef27-d2dd-4e8f-90e7-ef9bd8ca32dd" />

---
## 🚀 Features

* ✔ Validates email format using a robust RegEx pattern
* ✔ Provides clear **VALID** / **NOT VALID** messages
* ✔ Beginner-friendly and easy to understand
* ✔ Works directly via terminal input
* ✔ Lightweight and dependency-free

---

## 🧠 How It Works

The script uses the Python `re` module to match the user-entered email against a predefined RegEx pattern.

### 📌 Regex Pattern Used:

```
^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$
```

### 📝 Breakdown of the pattern:

* `a-z, A-Z, 0-9` → Letters and numbers
* `[\._]?` → Optional dot or underscore
* `@` → Must contain @ exactly once
* `.` → Dot after domain
* `\w{2,3}` → 2–3 letter domain extension (e.g., .com, .in)

---

## 📂 Code Snippet

```python
import re

email_cond = "^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$"

user_mail = input("Enter your email address: ")

if re.search(email_cond, user_mail):
    print(f"Email address entered {user_mail} is VALID")
else:
    print(f"Email address entered {user_mail} is NOT valid")
```

---

## 💻 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project folder:

   ```bash
   cd your-repo-name
   ```
3. Run the script:

   ```bash
   python email_validator.py
   ```

---

## 📘 Learning Outcomes

By building this project, you will understand:

* How to use the **re** module in Python
* How to create and test **regular expressions**
* How to validate user input
* Basic scripting and string pattern matching

---

## 🔮 Future Enhancements (Optional Ideas)

* Add GUI using Tkinter
* Validate complex email formats
* Add multiple test cases
* Convert into a Python package
* Web-based email validator

---

## 🤝 Contributing

Pull requests are welcome!
If you find issues or want to suggest improvements, feel free to open an issue.

---

## ⭐ Show Your Support

If you found this useful, consider giving the repo a **star** ⭐ on GitHub!
It motivates me to build more beginner-friendly Python projects.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
