# 코딩테스트 대비 문제 풀이

* 이것이 코딩 테스트이다
* BOJ
* programmers


## functional
|no|requirements|useCase|
|:---:|:---|:---|
|1|사용자의 이름, 주민번호, 주소, 이메일과 id/password를 입력받는다.|회원가입 하기|
|2|회원은 등록한 상품이 하나도 없는 상태에서 탈퇴할 수 있다.|탈퇴 하기|
|3|id/password를 이용하여 로그인 할 수 있다.|로그인 하기|

2. 상품 판매 및 판매내역 조회
|no|requirements|useCase|
|:---:|:---|:---|
|1|상품명, 제작회사명, 가격, 수량, 추가상품, 추가상품 가격, 판매 종료일 등의 정보를  입력받아 상품을 판매할 수 있다.|판매 상품 등록| 
|2|자신이 등록한 판매 중인 의류 상품 리스트를  조회 할 수 있다.|판매 상품 조회| 
|3|자신이 등록한 판매 중인 의류 상품을 수정 할 수 있다.|판매 상품 수정| 
|4|자신이 판매 완료한 의류 상품을 조회할 수 있다.|판매완료 상품 조회|
|5|판매 완료한 상품은 판매 종료일이 지났거나 남은 수량이 0이 된 상품을 의미한다.|Not applicable| 

## non-functional
|no|requirements|
|:---:|:---|
|1|사용자는 의류 쇼핑 사이트 사용 권한을 얻기 위해서 회원가입을 해야한다.|
|2|회원이 로그아웃하면 프로그램은 자동으로 종료된다.|
|3|탈퇴와 동시에 사용 권한은 소멸된다.|

