# inflearn_MakingInflearn
> '인프런'의 강의를 들으며 인프런 서비스를 구현해보았습니다.

![image](https://user-images.githubusercontent.com/81157873/147313690-abaebf71-3453-474d-96af-758841d03de1.png)

장고를 이용해 개발하였습니다.

인프런 서비스는 숙련된 연습을 위해 총 2차례 구현하였는데, 이 문서는 그 중 2번째 작업입니다.

## 주요 기능

-강의 글 쓰고 수정하기

-로그인 및 로그아웃

-수강평 생성 및 삭제

-강의보기 페이지

-관리자가 아닌 일반 사용자가 강의를 등록하고 수강할 수 있는 기능

## 설치 방법

IDE는 VS Code를 기준으로 합니다.

깃에서 초기 파일을 내려 받는 방법 (VS code에서 빈 폴더 생성 후)

```
$ git clone https://github.com/bosungpark/inflearn_MakingInflearn.git
```

가상환경 생성하기 및 켜기

```
$ cd 인프런만들기_2
$ python3 -m venv myvenv
$ source myvenv/bin/activate      //Mac
$ source myvenv/scripts/activate  // Windows
```

확인 및 실행

```
$ cd inflearn
$ python manage.py runserver
```

## 사용 예제

1.자유롭게 강의를 등록하고 수강할 수 있다.

2.원하는 카테고리의 강의를 모아 볼 수 있다.

3.로그인 및 회원가입 기능을 이용할 수 있다.

4.수강평을 자유롭게 작성할 수 있다.

## 개발 환경 설정

```
pip install Ckeditor
```

* 0.0.1
    * 작업 진행 중

## 정보

블로그에서 영상 확인하기 [@click](https://blog.naver.com/qkrqhtjd0806/222419179370) 

이메일: qkrqhtjd0806@naver.com

## 기여 방법

1. (<https://github.com/yourname/yourproject/fork>)을 포크합니다.
2. (`git checkout -b feature/fooBar`) 명령어로 새 브랜치를 만드세요.
3. (`git commit -am 'Add some fooBar'`) 명령어로 커밋하세요.
4. (`git push origin feature/fooBar`) 명령어로 브랜치에 푸시하세요. 
5. 풀 리퀘스트를 보내주세요.
