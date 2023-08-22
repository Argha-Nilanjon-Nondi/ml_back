
# ML BACK ( made with **Termux** in Smartphone)

## Welcome to ML BACK: Denoising Audio Files
**ML BACK** is an innovative Django project designed to tackle the challenge of audio denoising using machine learning techniques. Actually the project acts like a client . Real processing takes place in https://github.com/Argha-Nilanjon-Nondi/server .This repository serves as a comprehensive resource for anyone interested in enhancing the quality of audio recordings by removing unwanted noise. Whether you're a developer, researcher, or audio enthusiast, this project provides you with a powerful toolset to dive into the world of audio processing and machine learning

## Features

- Denoise Audio
- Super User Support
- Normal User Support
- User can only access own record

## Screenshots

- Run https://github.com/Argha-Nilanjon-Nondi/server in google colab and copy url from <span style="background-color: #f0f0f0"> your url is https://tiny-papers-relate.loca.lt/ </span>
 ![Screenshot 1](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/01.jpg?raw=true)
<br>

- Set main url as <span style="background-color: #f0f0f0"> https://tiny-papers-relate.loca.lt/ </span> in DENOISE_URL variable
 ![Screenshot 2](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/02.jpg?raw=true)
<br>


- Run django server
 ![Screenshot 3](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/03.jpg?raw=true)
<br>


- Run redis server ( As a message broker )
![Screenshot 4](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/04.jpg?raw=true)
<br>


- Run celery with watchfiles
![Screenshot 5](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/05.jpg?raw=true)

- Login to admin . You can use
| Email                | Password   | User Type |
| ---------------------- | ------------ | ----------- |
| super@django.com     | django1234 | Super     |
| normal@django.com    | django1234 | Regular   |

![Screenshot 6](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/06.jpg?raw=true)
<br>

- Music table
 ![Screenshot 7](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/07.jpg?raw=true)
<br>

- Submit a noisy audio
 ![Screenshot 8](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/08.jpg?raw=true)
<br>

- denoise process is completed and user is notified by email ( See yellow colored text )
 ![Screenshot 9](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/09.jpg?raw=true)
<br>

- Go to url and you can see a the  denoised version of that audio
![Screenshot 10](https://github.com/Argha-Nilanjon-Nondi/ml_back/blob/master/screenshot/10.jpg?raw=true)
<br>

## Demo

[Original](https://github.com/Argha-Nilanjon-Nondi/ml_back/raw/master/sample/oiginal.mp3)

[Denoised](https://github.com/Argha-Nilanjon-Nondi/ml_back/raw/master/sample/denoised.wav)

## Setup

- Clone the project 
```bash
git clone https://github.com/Argha-Nilanjon-Nondi/ml_back
cd ml_back
```

- Install packages
```bash
pip install -r requirements.txt
```

- Set up https://github.com/Argha-Nilanjon-Nondi/server

- Get the api url from "server" project and set it in settings.py as below 
```bash
npx: installed 22 in 4.629s
your url is: https://busy-insects-mix.loca.lt
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 125-349-859
```
```python
  DENOISE_URL="https://busy-insects-mix.loca.lt/api/upload"
```
- Run Redis server
```bash
redis-server
````
- Run celery task with watchfiles (to stay update)
```bash
watchfiles --filter python "python -m celery -A ml_back worker -l info"
```
- Start django server
```bash
python manage.py runserver
```








    
## Tech Stack
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=flat-the-badge&logo=python)&nbsp;&nbsp;&nbsp;
![Django](https://img.shields.io/badge/Django-4.2.4-green?style=flat-the-badge&logo=django) &nbsp;&nbsp;&nbsp;
![django-api-admin](https://img.shields.io/badge/django--api--admin-1.1.5-green?style=flat-the-badge&logo=django) &nbsp;&nbsp;&nbsp;
![django-rest-framework](https://img.shields.io/badge/django--rest--framework-0.1.0-green?style=flat-the-badge&logo=django) &nbsp;&nbsp;&nbsp;
![djangorestframework](https://img.shields.io/badge/djangorestframework-3.14.0-green?style=flat-the-badge&logo=django) &nbsp;&nbsp;&nbsp;
![celery](https://img.shields.io/badge/celery-5.3.1-green?style=flat-the-badge&logo=celery) &nbsp;&nbsp;&nbsp;
![redis](https://img.shields.io/badge/redis-4.6.0-green?style=flat-the-badge&logo=redis) &nbsp;&nbsp;&nbsp;
![colorama](https://img.shields.io/badge/colorama-0.4.6-green?style=flat-the-badge&logo=python) &nbsp;&nbsp;&nbsp;
![crypto](https://img.shields.io/badge/crypto-1.4.1-green?style=flat-the-badge&logo=python) &nbsp;&nbsp;&nbsp;
![cryptography](https://img.shields.io/badge/cryptography-41.0.3-green?style=flat-the-badge&logo=python) &nbsp;&nbsp;&nbsp;
![watchfiles](https://img.shields.io/badge/watchfiles-0.19.0-green?style=flat-the-badge&logo=python)



## Future Plans
- Expose functionality as Rest API
- Remove password changing form in superuser administration
- Create a new Web UI
- Enhance celery error handling
## Lessons Learned

- Django is all about customization
- Basic of OOP is must to work with Django
-  If you don't like anything , just overwrite it ( Of course in project , not in actual framework) 
- Anything can be customized but has a limit
- Always read documentation carefully 
- Write comment in code , otherwise you will forget
- Test ai generated code before applying them in project
 - If you can't figure out anything , just leave it , take rest and back with a fresh mind












## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### You are free to:

- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material.

The licensor cannot revoke these freedoms as long as you follow the license terms.

### Under the following terms:

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- **NonCommercial**: You may not use the material for commercial purposes.

- **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

[Read the full license here](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

This license is intended to ensure that the project is used exclusively for educational and non-commercial purposes.



## Acknowledgements

### Documentation Websites

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Cryptography.io](https://cryptography.io/en/latest/)
- [Celery](https://docs.celeryq.dev/en/stable/django/index.html)


### Websites and Resources
- [Asynchronous Tasks with Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/#install-redis-as-your-celery-broker-and-database-back-end)
- [Educative: Override Django Admin Templates](https://www.educative.io/answers/how-to-override-django-admin-templates)
- [GeeksforGeeks: Django DateTimeField](https://www.geeksforgeeks.org/datetimefield-django-models/amp/)

- [Customize Django Admin with Python](https://realpython.com/customize-django-admin-python/)
- [Django Celery Auto-Reload](https://testdriven.io/courses/django-celery/auto-reload/)
- [Django Upload Outside of Media Root](https://stackoverflow.com/questions/1729051/django-upload-to-outside-of-media-root)
- [Facebook Research Denoiser](https://github.com/facebookresearch/denoiser)
- [Stack Overflow: ImportError Partially Initialized Module](https://stackoverflow.com/questions/64807163/importerror-cannot-import-name-from-partially-initialized-module-m)
- [Stack Overflow: Passing Django Model Instances to Celery](https://stackoverflow.com/questions/15079176/should-django-model-object-instances-be-passed-to-celery)
- [Stack Overflow: Passing Arguments to Celery Task](https://stackoverflow.com/questions/50245429/how-can-i-pass-argument-to-celery-task)
- [Stack Overflow: OSError when Uploading Files over NFS](https://stackoverflow.com/questions/36154362/oserror-when-uploading-files-over-a-nfs)
- [Stack Overflow: Django Rest Framework Admin Site](https://stackoverflow.com/questions/63652653/does-the-django-rest-framework-provide-an-admin-site-to-manage-models)
- [PyTZ](https://pypi.org/project/pytz/)
- [Auto-Expiring Token in Django Rest Framework](https://idiomaticprogrammers.com/post/how-to-implement-auto-expiring-token-in-django-rest-framework/)

I would like to acknowledge that during the development of this project, I received valuable coding assistance from AI and chatbot services. The services that contributed to my coding process include:

- [chat.openai.com](https://chat.openai.com/): This AI-powered chatbot service provided me with suggestions, explanations, and code snippets that helped me overcome coding challenges in various parts of the project.

- [perplexity.ai](https://perplexity.ai/): I utilized the capabilities of perplexity.ai to refine my code by evaluating its readability and complexity, ensuring that the codebase follows best practices.

These AI and chatbot services significantly enhanced my productivity and problem-solving capabilities. While the assistance from these services played a role in my development process, I reviewed, customized, and integrated all code in this repository to ensure its correctness and alignment with the project's goals.

I extend my gratitude to the developers and teams behind chat.openai.com and perplexity.ai for creating tools that provide innovative solutions for coding challenges.

