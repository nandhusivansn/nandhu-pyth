radius=int(input("enter the radius of the circle"))
area=3.14*radius*radius
perimeter=2*3.14*radius
print(f"area of a circle is:{area}")
print(f"perimeter is :{perimeter}")
Data for locations:-

INSERT INTO locations (location_id,street_address,postal_code,city, state_province,country_id) VALUES ('1400', '2014 Jabberwocky Rd','26192', 'Southlake', 'Texas', 'US'), ('1500', '2011 Interiors Blvd', '99236', 'South San Francisco', 'California', 'US'), ('1700', '2004 Charade Rd', '98199',' Seattle', 'Washington', 'US'), ('1800','147 Spadina Ave','M5V 2L7', 'Toronto', 'Ontario', 'CA'), ('2400','8204 Arthur St', NULL, 'London', NULL, 'UK'), ('2500', 'Magdalen Centre, The Oxford Science Park', 'OX99ZB', 'Oxford', 'Oxford','UK'), ('2700', 'Schwanthalerstr. 7031', '80925', 'Munich', 'Bavaria', 'DE');

Data for jobs:-

INSERT INTO jobs(job_id,job_title,min_salary,max_salary) VALUES ('1', 'Public Accountant', 4200.00,9000.00), ('2', 'Accounting Manager', 8200.00,16000.00), ('3', 'Administration Assistant', 3000.00,6000.00), ('4', 'President', 20000.00,40000.00), ('5', 'Administration Vice President', 15000.00,30000.00), ('6', 'Accountant', 4200.00,9000.00), ('7', 'Finance Manager', 8200.00,16000.00), ('8', 'Human Resources Representative', 4000.00,9000.00), ('9', 'Programmer', 4000.00,10000.00), ('10', 'Marketing Manager', 9000.00,15000.00), ('11', 'Marketing Representative', 4000.00,9000.00), ('12', 'Public Relations Representative', 4500.00,10500.00), ('13', 'Purchasing Clerk', 2500.00,5500.00), ('14', 'Purchasing Manager', 8000.00,15000.00), ('15', 'Sales Manager', 10000.00,20000.00), ('16','Sales Representative', 6000.00,12000.00), ('17', 'Shipping Clerk', 2500.00,5500.00), ('18', 'Stock Clerk', 2000.00,5000.00), ('19', 'Stock Manager', 5500.00,8500.00);