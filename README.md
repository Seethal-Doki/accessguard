# AccessGuard 🔐
### Automated Role-Based Access Validation Framework

Built with Selenium, Python, and pytest to validate that users 
only have access to features appropriate for their assigned role 
in financial services environments.

---

## 🎯 Problem Statement
Financial institutions manage thousands of employees across dozens 
of systems. One wrong permission is a compliance violation. 
AccessGuard automates access validation so compliance teams can 
catch issues before auditors do.

---

## 🏗️ Project Structure
accessguard/
├── pages/
│   ├── login_page.py      # Login page interactions
│   └── dashboard_page.py  # Dashboard & permission checks
├── tests/
│   └── test_access_validation.py  # Test suite
├── reports/               # Generated HTML reports
├── conftest.py            # Browser setup & fixtures
└── README.md
## 🛠️ Tech Stack
- Python 3.13
- Selenium 4
- pytest + pytest-html
- WebDriver Manager
- Page Object Model pattern
- Cross-browser: Chrome & Firefox

---

## 🚀 How to Run

**Run on Chrome (default):**
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

**Run on Firefox:**
```bash
pytest tests/ --browser=firefox --html=reports/report.html --self-contained-html
```

**Run a single test:**
```bash
pytest tests/test_access_validation.py::TestAccessValidation::test_readonly_cannot_transfer_funds -v
```

---

## ✅ What Gets Validated

| Role | Admin Panel | Approve | Reports | Transfer | Audit Log |
|------|-------------|---------|---------|----------|-----------|
| Admin | ✅ | ✅ | ✅ | ✅ | ✅ |
| Manager | ❌ | ✅ | ✅ | ✅ | ❌ |
| Read Only | ❌ | ❌ | ✅ | ❌ | ❌ |

---

## 🤖 AI Integration
This framework is designed to integrate with AI-powered testing 
for:
- Automated test case generation
- Intelligent test prioritization  
- Predictive defect detection
- Self-healing locators when UI changes

---

## 📊 Sample Report Output
After running, open `reports/report.html` in your browser to see 
a full pass/fail breakdown of all access validation tests.

---

*Built by Seethal Doki | Automated Testing & AI-Assisted QA*
