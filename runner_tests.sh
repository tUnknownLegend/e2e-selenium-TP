export EMAIL="test@reazon.com"
export PASSWORD="reazon"
export LOGIN_A="you@example.com"
export PWD_A="kXkjc728dnAD#@"
export LOGIN_B="test@test"
export PWD_B="123456"

pytest --alluredir=allure-results hw/code/test*.py
