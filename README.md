# 🧾 Customer Billing System

A simple terminal-based Python application to manage customer billing, allowing users to add customer details, manage purchases, and generate formatted invoices — complete with dates and billing summaries.

---

## 🚀 Features

- 📥 Add new customers and their purchased items.
- 🛍️ Dynamically enter product names, quantities, and unit prices.
- 🧮 Calculates total bill amount automatically.
- 📅 Auto-generates current date and timestamp.
- 📄 Nicely formatted invoice output (print-ready).

---

## 🛠️ Technologies Used

- **Python 3.x**
- Standard libraries:
  - `datetime`
  - `os`
  - `sys`

No external dependencies required!

---

## 📂 File Structure

```
customer_billing_system/
│
├── customer_billing_system.py   
└── README.md                    
```

---

## 📸 Sample Output

```
Enter the number of customers: 1

Enter customer name: John Doe
Enter the number of products: 2

Enter name of product 1: Keyboard
Enter quantity of product 1: 2
Enter unit price of product 1: 750

Enter name of product 2: Mouse
Enter quantity of product 2: 1
Enter unit price of product 2: 500

--------------------------------------------------
                 ABC Retail Store                 
--------------------------------------------------
Date: 2024-04-04
Time: 15:21:30
Customer Name: John Doe
--------------------------------------------------
Product         Quantity        Unit Price      Total
--------------------------------------------------
Keyboard        2               750             1500
Mouse           1               500             500
--------------------------------------------------
Total Amount Payable: Rs. 2000
--------------------------------------------------
```

---

## ▶️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hardikagarwal2026/customer_billing_system.git
   cd customer_billing_system
   ```

2. **Run the script**:
   ```bash
   python customer_billing_system.py
   ```

---

## 📌 TODO / Future Improvements

- [ ] Export invoice to PDF or text file.
- [ ] Store customer data in a database.
- [ ] Add input validation & error handling.
- [ ] GUI version using Tkinter or PyQt.
- [ ] GST/tax calculation support.

---

## 🙌 Acknowledgments

Developed as a beginner-friendly Python project to practice file I/O, data structures, and user interaction in the terminal.

---

