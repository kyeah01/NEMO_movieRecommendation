# Movie Recommendation project

## Backend setup

- model 작업을 위한 migration이 필요합니다.
  `backend` > `manage.py` 파일을 실행시킵니다.

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

- 서버를 구동시킵니다.

  ```bash
  $ python manage.py runserver
  ```

  

## Data setup

- Backend 서버가 켜진 상태에서 `data` > `movie-lens100K` > `movie.py`파일을 실행시킵니다.

    ```bash
    $ python movie.py
    ```

