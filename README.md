# 프로젝트: ESTsoft-백엔드-부트캠프-프로젝트-3-Django REST Framework-도커화

## 주제: ChatGPT 기반 싱가포르 여행 계획 자동 생성 플래너 챗봇 - 백엔드

## 프로젝트 개요
이 프로젝트는 ChatGPT를 사용하여 싱가포르 여행 계획을 자동으로 생성하는 챗봇의 백엔드 서버를 구축하는 데 중점을 둡니다. 프로젝트는 OpenAI Chat Completions API와 Django REST Framework(DRF) 서버 간의 통신 설정, 그리고 백엔드와 프론트엔드 페이지 간의 통신을 용이하게 하는 작업을 포함합니다. 백엔드 서버는 AWS EC2, PostgreSQL, Gunicorn, Nginx, Docker를 사용하여 배포되었습니다.

## 목표
OpenAI Chat Completions 및 프론트엔드와 통신하는 백엔드 서버 구현
AWS EC2, PostgreSQL, Gunicorn, Nginx, Docker를 사용하여 백엔드 서버 배포


### Development Environment
![Django REST framework](https://img.shields.io/badge/Django_REST_framework-092E20?style=for-the-badge&logo=django&logoColor=white&logoWidth=20&logoHeight=20)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white&logoWidth=20&logoHeight=20)
![Nginx](https://img.shields.io/badge/Nginx-269539?style=for-the-badge&logo=nginx&logoColor=white&logoWidth=20&logoHeight=20)
![Gunicorn](https://img.shields.io/badge/Gunicorn-green?style=for-the-badge&logoWidth=20&logoHeight=20)
![docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white&logoWidth=20&logoHeight=20)
![aws](https://img.shields.io/badge/AmazonAWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white&logoWidth=20&logoHeight=20)


### 개발기간
- 2023.07.26 ~ 2023.08.02 (개발기간)
- 2023.08.10 ~ 2023.08.16 (도커 컨테이너를 사용하여 원래 프로젝트 재구성)

### 배포 URL
- http://bundletripbychat.com/

### ERD 기획
![ormi-django-project2](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/26a4dad7-a963-48b0-b07a-a05392a25204)
- 초기에는 텍스트-davinci-003 API를 사용하여 사용자 입력과 GPT 응답을 통합한 ERD 모델을 설계했습니다.
- 도중에 gpt-3.5-turbo가 포함된 ChatCompletion API로 전환하여  뷰와 모델을 새로운 API 형식에 맞추기 위해 ERD 모델을 조정했습니다. (원래 ERD 기획에는 반영되지 않았습니다.)

### 기능 기획
![django-rest-chatgpt-mindmap](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/fbfaf79e-45d9-4a63-ba19-d2d4b1ea6445)
- 초기에 JWT를 사용한 인증을 계획했지만, 세부적인 이해가 부족하여 필요한 기능 구현에 어려움을 겪었습니다.

### 기능 세부사항
- ChatGPT API와 프론트엔드와 통신하기 위해 챗봇 앱에 API를 구현했습니다.
- Simple JWT를 사용하여 회원 가입 API 및 로그인/토큰 갱신 API를 개발했습니다.
- view.py에서 JWT 유효성 검사 API를 구현하여 사용자 로그인 상태에 따라 로그아웃 버튼을 동적으로 표시/숨깁니다.

### 직면한 도전 과제
#### Monolithic vs. DRF:
- 모놀리식 아키텍처에서 Django REST Framework로 전환하는 것은 특히 프론트엔드와 백엔드 프로젝트를 분리하여 관리하는 데 어려움이 있었습니다.

#### JWT 인증:
- 사전 이해 없이 JWT 인증을 구현하면서 상당한 시행착오를 겪었습니다. Bearer 토큰을 적절히 처리하고 토큰 유효성을 검증하는 방법을 배웠습니다.

#### 배포:
- 초기에는 Uwsgi와 Nginx를 사용하여 AWS에 서버를 배포했지만, 현대적인 배포 방법을 배우기 위해 Docker를 학습할 필요성을 인식했습니다. 이후 Docker를 사용하여 배포했습니다. 이 단계에서 컨테이너화, Docker 이미지 빌드, 리눅스 유형(우분투, 알파인), Docker Compose에 대해 배웠습니다.

#### Custom Domain 이슈:
- 사용자 지정 도메인을 GitHub 페이지와 연결하는 데 어려움을 겪었고, 서버 통신을 위해 서브도메인을 설정해야 했습니다.

#### 비동기 통신:
- 비동기 통신을 위해 fetch, ajax, axios와 같은 다양한 방법을 탐색했으며, 초기에 깊이 있는 이해가 없어 어려움을 겪었습니다.

#### 동적 웹페이지:
- Django 템플릿 언어가 동적 웹 페이지에 적합하지 않다는 것을 배웠고, 로그인/로그아웃 버튼에 대한 조건부 렌더링을 구현하기 위해 토큰 기반 접근 방식을 사용했습니다.

#### HTTPS 구현:
- GitHub 페이지의 사용자 지정 도메인 URL에 HTTPS를 적용하는 데 어려움을 겪었습니다.

## 결론
- 이번 DRF 프로젝트를 하면서 API에 대한 이해가 많이 생겼던 것 같고, 동시에 저의 부족한 점을 많이 느꼈습니다. 장고 DRF를 구현하고, 프론트엔드 프로젝트와 백엔드 프로젝트를 연결시켜, 저만의 웹서비스를 구현할 수 있었던 좋은 경험이었습니다.
