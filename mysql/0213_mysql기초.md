- **HAVING**
WHERE은 그룹화 하기 전 데이터, HAVING은 그룹후 집계에 사용된다
```
SELECT Country, COUNT(*) AS Count
FROM Suppliers
GROUP BY Country
Having count>=3;
```
- **DISTINCT** 중복값 제거
```
SELECT Country, COUNT(DISTINCT CITY)
FROM Customers
GROUP BY Country;
```
- **LIMIT**
상위 몇개만 잘라오기
```
SELECT * from table
limit 5;
```
- 문자열 부분 가져오기
LEFT
```
LEFT(문자,가져올 갯수);
```