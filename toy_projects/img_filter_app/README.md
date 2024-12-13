<!-- @format -->

## 1. 프로젝트 개요

### img_filter_app: 이미지 필터 애플리케이션

### 설명

- 이 프로젝트는 OpenCV를 활용하여 다양한 이미지 필터를 적용할 수 있는 간단한 애플리케이션입니다.

---

## 2. 주요 기능 (Features)

- 다양한 필터 효과 제공 (예: 그레이스케일, 블러, 엣지 감지 등)
- 실시간 결과 미리보기

---

## 3. 설치 및 실행 방법 (Installation & Usage)

### 요구사항

- node v20.11.0
- python 3.11.11
- poetry

### 설치 방법

1. clone repo
   ```bash
   git clone https://github.com/kimyw97/open_cv_practice.git
   cd open_cv_practice/toy_projects/img_filter_app
   ```
2. install package

   ```bash
   poetry install

   cd img-filter-app-client
   npm install
   ```

3. 애플리케이션을 실행합니다:

   ```bash
   # server
   # go root dict(img_filter_app)
   # active virtual env
   poetry shell

   poetry run python ./img_filter_app-server/hello.py

   #client
   cd img-filter-app-client
   npm run start
   ```

---

## 4. 데모 (Demo)

![App Demo](./demo.gif)
