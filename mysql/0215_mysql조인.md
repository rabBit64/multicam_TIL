- 3개 이상의 테이블 INNER JOIN
```
select x.컬럼이름A, 
    y.컬럼이름B,
    z.컬럼이름C, ...
from 테이블이름X x, 테이블이름Y y, 테이블이름Z z, ...
where x.컬럼이름M=y.컬럼이름N
  and y.컬럼이름O=z.컬럼이름Q;
```
