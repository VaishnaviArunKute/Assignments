CREATE TABLE customer(
	customer_id INt PRIMARY KEY NOT NULL,
    customer_name VARCHAR(30)
);

INSERT INTO customer VALUES(1,'John');
INSERT INTO customer VALUES(2,'Smith');
INSERT INTO customer VALUES(3,'Ricky');
INSERT INTO customer VALUES(4,'Walsh');
INSERT INTO customer VALUES(5,'Stefen');
INSERT INTO customer VALUES(6,'Fleming');
INSERT INTO customer VALUES(7,'Thomson');
INSERT INTO customer VALUES(8,'David');
SELECT * FROM customer;

CREATE TABLE product(
	product_id INT PRIMARY KEY NOT NULL,
    product_name VARCHAR(30),
    product_price INT
);

INSERT INTO product VALUES(1,'Television',19000);
INSERT INTO product VALUES(2,'DVD',3600);
INSERT INTO product VALUES(3,'Washing Machine',7600);
INSERT INTO product VALUES(4,'Computer',35900);
INSERT INTO product VALUES(5,'Ipod',3210);
INSERT INTO product VALUES(6,'Panasonic Phone',2100);
INSERT INTO product VALUES(7,'Chair',360);
INSERT INTO product VALUES(8,'Table',490);
INSERT INTO product VALUES(9,'Sound System',12050);
INSERT INTO product VALUES(10,'Home Teatre',19350);
SELECT * FROM product;

CREATE TABLE orders(
	order_id INT PRIMARY KEY NOT NULL,
    customer_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

INSERT INTO orders VALUES(1,4,'2005-01-10');
INSERT INTO orders VALUES(2,2,'2006-02-10');
INSERT INTO orders VALUES(3,3,'2005-03-20');
INSERT INTO orders VALUES(4,3,'2006-03-10');
INSERT INTO orders VALUES(5,1,'2007-04-05');
INSERT INTO orders VALUES(6,7,'2006-12-13');
INSERT INTO orders VALUES(7,6,'2008-03-13');
INSERT INTO orders VALUES(8,6,'2004-11-29');
INSERT INTO orders VALUES(9,5,'2005-01-13');
INSERT INTO orders VALUES(10,1,'2007-12-12');
SELECT * FROM orders;

CREATE TABLE order_details(
	order_detail_id INt PRIMARY KEY NOT NULL,
    order_id INt NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

INSERT INTO order_details VALUES(1,1,3,1); 
INSERT INTO order_details VALUES(2,1,2,3); 
INSERT INTO order_details VALUES(3,2,10,2); 
INSERT INTO order_details VALUES(4,3,7,10); 
INSERT INTO order_details VALUES(5,3,4,2); 
INSERT INTO order_details VALUES(6,3,5,4); 
INSERT INTO order_details VALUES(7,4,3,1); 
INSERT INTO order_details VALUES(8,5,1,2); 
INSERT INTO order_details VALUES(9,5,2,1); 
INSERT INTO order_details VALUES(10,6,5,1); 
INSERT INTO order_details VALUES(11,7,6,1); 
INSERT INTO order_details VALUES(12,8,10,2); 
INSERT INTO order_details VALUES(13,8,3,1); 
INSERT INTO order_details VALUES(14,9,10,3); 
INSERT INTO order_details VALUES(15,10,1,1); 
SELECT * FROM order_details;

-- 1. Fetch all the Customer Details along with the product names that the customer has ordered.
	SELECT c.*, p.product_name
    FROM customer AS c, product AS p, orders AS o, order_details AS od
    WHERE c.customer_id = o.customer_id AND o.order_id = od.order_id AND p.product_id = od.product_id;

-- 2. Fetch Order_Id, Ordered_Date, Total Price of the order (product price*qty).
	SELECT o.order_id, o.order_date, (p.product_price * od.quantity) AS total_price
    FROM orders AS o, order_details AS od, product AS p
    WHERE o.order_id = od.order_id AND p.product_id = od.product_id;

-- 3.Fetch the Customer Name, who has not placed any order
	SELECT c.customer_name
    FROM customer AS c
    WHERE c.customer_id NOT IN (SELECT customer_id FROM orders);
    
-- 4. Fetch the Product Details without any order(purchase)
	SELECT p.*
    FROM product AS p
	WHERE p.product_id NOT IN (SELECT product_id FROM order_details);

-- 5.Fetch the Customer name along with the total Purchase Amount
	SELECT customer_name, (od.quantity * p.product_price) AS tot_price
    FROM customer AS c, orders AS o, product AS p, order_details AS od
    WHERE c.customer_id = o.customer_id AND o.order_id = od.order_id AND p.product_id = od.product_id
    GROUP BY c.customer_name;

-- 6. Fetch the Customer details, who has placed the first and last order
    select * from customer 
    where customer_id in (select customer_id from orders where order_id =(select min(order_id)from orders )) 
	union all select * from customer 
	where customer_id in (select customer_id from orders where order_id = (select max(order_id) from orders));
    
-- 7. Fetch the customer details , who has placed more number of orders 
    SELECT count(o.customer_id) , o.customer_id
    FROM orders AS o 
    GROUP BY o.customer_id
    HAVING count(o.customer_id) >  1;

-- 8. Fetch the customer details, who has placed multiple orders in the same year
	-- didn't get the expected output
	SELECT c.* , count(EXTRACT(YEAR FROM o.order_date)), EXTRACT(YEAR FROM o.order_date)AS dates
    FROM customer AS c, orders AS o
    WHERE c.customer_id = o.customer_id 
	GROUP BY EXTRACT(YEAR FROM o.order_date)
    HAVING count(EXTRACT(YEAR FROM o.order_date)) > 1
	;

	SELECT c.* , EXTRACT(YEAR FROM o.order_date)AS dates, EXTRACT(YEAR FROM o.order_date), COUNT(o.customer_id)
    FROM customer AS c, orders AS o
    WHERE c.customer_id = o.customer_id 
	GROUP BY  o.customer_id
    having  COUNT(o.customer_id) > 1
    -- HAVING count(EXTRACT(YEAR FROM o.order_date)) > 1
	;
    
    SELECT c.*, EXTRACT(YEAR FROM o.order_date) AS year
    FROM customer AS c, orders AS o
    WHERE c.customer_id = o.customer_id ;

-- 9. Fetch the name of the month, in which more number of orders has been placed
	SELECT COUNT(EXTRACT(MONTH FROM order_date)) AS no_month, monthname(order_date) AS month_name
    FROM orders
	GROUP BY EXTRACT(MONTH FROM order_date)
    ORDER BY COUNT(EXTRACT(MONTH FROM order_date)) DESC
	LIMIT 1;

-- 10. Fetch the maximum priced Ordered Product
	SELECT MAX(p.product_price)
    FROM product as p
    WHERE p.product_id IN (SELECT product_id FROM order_details); 
