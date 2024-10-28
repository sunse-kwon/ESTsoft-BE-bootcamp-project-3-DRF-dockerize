# Project: ESTsoft-Backend-bootcamp-project-3-Django REST Framework- dockerize

## Subject: ChatGPT-based Singapore Travel Plan Auto-generation Planner Chatbot - Backend

## Project Overview
This project focuses on creating a backend server for a chatbot that automatically generates travel plans for Singapore using ChatGPT. The project involves setting up communication between the OpenAI Chat Completions API and a Django REST Framework (DRF) server, as well as facilitating communication between the backend and a frontend page. The backend server was deployed using AWS EC2, PostgreSQL, Gunicorn, and Nginx, Docker.


## Objectives
Implement a backend server that communicates with OpenAI Chat Completions and the frontend.
Deploy the backend server using AWS EC2, PostgreSQL, Gunicorn, and Nginx, Docker.


### Development Environment
![Django REST framework](https://img.shields.io/badge/Django_REST_framework-092E20?style=for-the-badge&logo=django&logoColor=white&logoWidth=20&logoHeight=20)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white&logoWidth=20&logoHeight=20)
![Nginx](https://img.shields.io/badge/Nginx-269539?style=for-the-badge&logo=nginx&logoColor=white&logoWidth=20&logoHeight=20)
![Gunicorn](https://img.shields.io/badge/Gunicorn-green?style=for-the-badge&logoWidth=20&logoHeight=20)
![docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white&logoWidth=20&logoHeight=20)
![aws](https://img.shields.io/badge/AmazonAWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white&logoWidth=20&logoHeight=20)


### Development Period
- 2023.07.26 ~ 2023.08.02 (Original development)
- 2023.08.10 ~ 2023.08.16 (Rebuild original project using Docker Container)

### Deploy URL
- http://bundletripbychat.com/

### ERD Planning
![ormi-django-project2](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/26a4dad7-a963-48b0-b07a-a05392a25204)
- Initially designed the ERD model using text-davinci-003 API, integrating user input and GPT responses.
- Adjusted the ERD model when switching to ChatCompletion API with gpt-3.5-turbo, leading to modifications in the view and model to match the new API format.

### Feature Planning
![django-rest-chatgpt-mindmap](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/fbfaf79e-45d9-4a63-ba19-d2d4b1ea6445)
- Initially planned to use JWT for authentication but lacked detailed understanding, which posed challenges in implementing the required features.

### Feature Details
- Implemented an API in the chatbot app to communicate with the ChatGPT API and the frontend.
- Developed a user app with signup API and login/token refresh API using Simple JWT.
- Implemented JWT validation API in view.py to dynamically show/hide logout buttons based on user login status.

### Challenges Faced
#### Monolithic vs. DRF:
- Transitioning from a monolithic architecture to Django REST Framwork was challenging, especially managing separate frontend and backend projects.
#### JWT Authentication:
- Implementing JWT authentication without prior understanding led to significant trial and error. Learned to properly handle Bearer tokens and implement token validation.

#### Deployment:
- Initially deployed the server using Uwsgi and Nginx on AWS but recognized the need to learn Docker for modern deployment practices. Later, deployed using Docker. During this phase, learned about containerization, building Docker images, Linux types (Ubuntu, Alpine), and Docker Compose YAML files.


#### Custom Domain Issues:
- Faced difficulties linking a custom domain with GitHub pages, resolving the need to set up a subdomain for server communication.

#### Asynchronous Communication:
- Explored various methods like fetch, ajax, and axios for async communication, initially struggling without a deep understanding.

#### Dynamic Webpages:
- Learned that Django template language isn’t suitable for dynamic web pages, leading to the implementation of token-based conditional rendering for login/logout buttons.

#### HTTPS Implementation:
- Encountered issues with applying HTTPS to custom domain URLs on GitHub pages.

## Conclusion
This DRF project significantly enhanced my understanding of APIs and backend development while highlighting areas for improvement. Successfully connecting frontend and backend projects and deploying a functional web service was a valuable learning experience, exposing me to real-world challenges and modern development practices. By presenting these detailed aspects of the project, I aim to demonstrate my capability to handle complex backend development tasks and my commitment to continuous learning and improvement in the field of data engineering.






