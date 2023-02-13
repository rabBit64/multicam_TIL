문제1
SELECT distinct country FROM customers
ORDER BY country;	

문제2
SELECT distinct state from customers
ORDER BY state DESC;

문제3
SELECT customerNumber,customerName,country FROM customers
WHERE country NOT IN ("USA")
ORDER BY customerNumber DESC;

문제4
SELECT * from offices
WHERE city="Paris";

문제5
SELECT customerNumber,customerName,country,state
from customers
where country="USA" and state="CA"
order by customerName DESC;

문제6
SELECT customerNumber, customerName, country, state
from customers
WHERE country="USA" and state="CA" or state="NY"
order by customerName DESC;

문제7
SELECT customerNumber, customerName, state
from customers
WHERE state="CA" or state="NY" or state="CT" or state="PA"
order by customerName DESC;

문제8
SELECT productCode,productName,quantityInStock
from products
WHERE quantityInStock<1000
order by quantityInStock;

문제9
SELECT productCode, productName, quantityInStock
from products
WHERE 2000<=quantityInStock and quantityInStock<=3000
order by quantityInStock DESC;

문제10
SELECT customerNumber, customerName, phone
from customers
WHERE phone LIKE '%555'
order by customerName DESC;

문제11
SELECT productCode, quantityInStock
from products
order by quantityInStock DESC
limit 5;

문제12
SELECT jobTitle, count(jobTitle) as count_job
from employees
group by jobTitle
order by count_job DESC, jobTitle DESC;

문제13
SELECT country, count(country) as count_country
from customers
group by country
order by count_country DESC, country DESC;

문제14 
SELECT orderNumber, sum(quantityOrdered * priceEach) as total
from orderdetails
group by orderNumber
order by total DESC;

문제15
SELECT LEFT(orderDate,4) as year, count(LEFT(orderDate,4)) as 'COUNT(orderNumber)'
from orders
group by year;

문제16 
SELECT productLine,max(quantityInStock) as 'max_stock' FROM products
group by productLine
having max(quantityInStock)<9000;

문제17
SELECT orderNumber,sum(quantityOrdered) as itemsCount, sum(priceEach*quantityOrdered) as total
from orderdetails
group by orderNumber
having itemsCount>=500 and total>=50000;
