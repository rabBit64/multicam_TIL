- Github flow의 기본 원칙  
	커밋은 하나의 버전이다. *커밋 메세지는 명확하게 작성하기*
	master branch는 반드시 배포 가능한 상태여야 한다.
	pull request를 통해서 협업을 진행한다.

```
git branch (브랜치명)
git checkout (브랜치명)
git push origin (브랜치명)
```

- 매번 로그인 안하기
```
$ git config --global user.name "이름"
$ git config --global user.email 이메일@naver.com
$ git config --global credential.helper store
```

- 커밋 삭제하기
```
$ git reset HEAD^
```

- 에러와 상관없이 강제로 push
```
$ git push -u origin +master
```
![](./img/gitflow.png)
