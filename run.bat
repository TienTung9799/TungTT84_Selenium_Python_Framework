:: Run Test and Create Report 

echo === Run Test Case and Create Log json File ===

pytest tests/logintest.py --alluredir=reports/allure-results

echo === Generate HTML From allure-results ===

allure serve reports/allure-results

echo === Open Report HTML File ===

start "" "reports/allure-report/index.html"
