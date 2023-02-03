# LearnLg 🚀

Side project to keep a history of translations by category (EN-ES). This was done using the Django framework with mostly class-based views. This open-source part shows the implementation of the following functions:

- Account creation (With or without Google CAPTCHA)
- Log in (With or without Google CAPTCHA)
- Log out
- Delete account
- Setting up a custom file for 404 and 403 errors

[The complete project](https://learnlg.pythonanywhere.com/)
## ➡️ Tech Stack

**Client:** Tailwind CSS, Vanilla JS

**Server:** Python 3.10 (Django 4.0)


**API**: Google CAPTCHA, (and for complete version DeepL API)


## ➡️ Required

- Have at least python 3.10 on your computer
- If you want to use Google CAPTCHA: have a public key and a private key for using Google CAPTCHA. [Here is a video showing how to create this](https://www.youtube.com/watch?v=KqDW69BSdEo) (it is not mandatory I have planned to launch the project without also)

## ➡️ Running

#### Introduction

Clone the project and check if everything is correct
```bash
git clone https://github.com/ChristopheKADJO/learnlg.git

cd learnlg/

ls

// You should see:

README.md  requirements.txt  run_linmac.sh  run_windows.sh  run_without_captcha.sh  src/

// If this is the case, it means that everything is ok, we go to the next step!
```



#### 1. Setting up your API keys OR without CAPTCHA

#### With CAPTCHA:

Replace public and private with your real keys. If this is not done, the CAPTCHA error will always occur.

```bash
/learnlg/src/learnlg/.env


3 RECAPTCHA_PUBLIC_KEY = 'public'
4 RECAPTCHA_PRIVATE_KEY = 'private'
```

#### Without CAPTCHA:

Run this command:
```bash
/learnlg/

sh run_without_captcha.sh
```


#### 2. Windows / Linux or MacOS
For windows run this command:
```bash
/learnlg/

sh run_windows.sh

Runserver will run automatically:
You can launch: http://127.0.0.1:8000/
```

For Linux or MacOS run this command:
```bash
/learnlg/

sh run_linmac.sh

Runserver will run automatically:
You can launch: http://127.0.0.1:8000/
```