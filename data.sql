PRAGMA foreign_keys=ON;

-- Populate members
INSERT INTO members VALUES('davood@abc.com','Davood Rafiei','780-111-3333','123');
INSERT INTO members VALUES('joe@gmail.com','Joe Anderson','780-111-2222','123');
INSERT INTO members VALUES('mary@abc.com','Mary Smith','780-222-3333','123');
INSERT INTO members VALUES('ajohn@gmail.com','ajohn aduo','780-333-4441','123');
INSERT INTO members VALUES('bjohn@gmail.com','bjohn aduo','780-333-4442','123');
INSERT INTO members VALUES('cjohn@gmail.com','cjohn aduo','780-333-4443','123');
INSERT INTO members VALUES('djohn@gmail.com','djohn aduo','780-333-4444','123');
INSERT INTO members VALUES('ejohn@gmail.com','ejohn aduo','780-333-4445','123');
INSERT INTO members VALUES('fjohn@gmail.com','fjohn aduo','780-333-4446','123');
INSERT INTO members VALUES('gjohn@gmail.com','gjohn aduo','780-333-4447','123');
INSERT INTO members VALUES('hjohn@gmail.com','hjohn aduo','780-333-4448','123');
INSERT INTO members VALUES('ijohn@gmail.com','ijohn aduo','780-333-4449','123');
INSERT INTO members VALUES('paul@a.com','John Paul','780-333-4444','123');
INSERT INTO members VALUES('ljohn@gmail.com','l john','777','123');
INSERT INTO members VALUES('mjohn@gmail.com','m john','123','123');
INSERT INTO members VALUES('njohn@gmail.com','n john','12334','123');
INSERT INTO members VALUES('ojohn@gmail.com','o john','12334','123');
INSERT INTO members VALUES('pjohn@gmail.com','p john','34242','123');
INSERT INTO members VALUES('q8@gmail.com','user question8','19376','123'); 
INSERT INTO members VALUES('q81@gmail.com','user2 question8','19377','123');

-- Populate cars
INSERT INTO cars VALUES(1,'Aston Martin','DB5',1964,1,'davood@abc.com');
INSERT INTO cars VALUES(2,'Honda','Civic',2017,4,'joe@gmail.com');
INSERT INTO cars VALUES(3,'Nissan','Rogue',2018,4,'mary@abc.com');
INSERT INTO cars VALUES(4,'Honda','DB5',2016,1,'ajohn@gmail.com');
INSERT INTO cars VALUES(5,'Honda','Civic',2017,4,'ajohn@gmail.com');
INSERT INTO cars VALUES(6,'Nissan','Rogue',2018,3,'ajohn@gmail.com');
INSERT INTO cars VALUES(7,'Nissan','Rogue',2019,5,'davood@abc.com');
INSERT INTO cars VALUES(8,'Nissan','Rogue',2000,5,'cjohn@gmail.com');
INSERT INTO cars VALUES(9,'Honda','Rogue',2001,4,'cjohn@gmail.com');
INSERT INTO cars VALUES(10,'Honda','Rogue',2001,4,'djohn@gmail.com');
INSERT INTO cars VALUES(11,'Honda','Rogue',2002,4,'djohn@gmail.com');
INSERT INTO cars VALUES(12,'Honda','Rogue',2003,4,'djohn@gmail.com');
INSERT INTO cars VALUES(20,'','','',4,'ljohn@gmail.com');
INSERT INTO cars VALUES(21,'','','',4,'mjohn@gmail.com');
INSERT INTO cars VALUES(13,'','','',5,'mjohn@gmail.com');
INSERT INTO cars VALUES(22,'','','','','pjohn@gmail.com');

-- Populate locations
INSERT INTO locations VALUES('ab1','Edmonton','Alberta','UofA LRT st');
INSERT INTO locations VALUES('ab2','Edmonton','Alberta','Century LRT st');
INSERT INTO locations VALUES('ab3','Edmonton','Alberta',NULL);
INSERT INTO locations VALUES('ab4','Calgary','Alberta','111 Edmonton Tr');
INSERT INTO locations VALUES('ab5','Calgary','Alberta','Airport');
INSERT INTO locations VALUES('ab6','Red Deer','Alberta','City Hall');
INSERT INTO locations VALUES('ab7','Red Deer','Alberta','Airport');
INSERT INTO locations VALUES('bc1','Vancouver','British Columbia','Stanley Park');
INSERT INTO locations VALUES('bc2','Vancouver','British Columbia','Airport');
INSERT INTO locations VALUES('bc888','Vancouver','British Columbia','BC Place');
INSERT INTO locations VALUES('bc999','Vancouver','British Columbia','Burrard Street');
INSERT INTO locations VALUES('on300','Toronto','Ontario','Bay Street');
INSERT INTO locations VALUES('on301','Ottawa','Ontario','Ahearn Avenue');

-- Populate rides
INSERT INTO rides VALUES(100,30,'2018-11-12',3,'small bag','ab1','ab4','joe@gmail.com',2);
INSERT INTO rides VALUES(101,30,'2018-11-13',3,'small bag','ab1','ab4','joe@gmail.com',2);
INSERT INTO rides VALUES(102,40,'2018-11-12',3,'small bag','ab1','ab4','cjohn@gmail.com',8);
INSERT INTO rides VALUES(103,50,'2018-11-12',3,'small bag','ab1','ab4','djohn@gmail.com',12);
INSERT INTO rides VALUES(104,50,'2017-11-12',3,'','ab1','ab4','joe@gmail.com',2);
INSERT INTO rides VALUES(105,50,'2018-12-12',3,'','ab1','ab4','joe@gmail.com',2);
INSERT INTO rides VALUES(106,50,'2018-11-12',3,'','ab1','bc1','joe@gmail.com',2);
INSERT INTO rides VALUES(107,50,'2018-11-12',3,'','bc1','ab4','joe@gmail.com',2);
INSERT INTO rides VALUES(108,50,'2018-11-20',3,'','ab4','ab1','joe@gmail.com',2);
INSERT INTO rides VALUES(109,200,'2018-10-1',4,'','ab4','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(110,300,'2018-10-1',4,'','ab4','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(111,310,'2018-10-1',4,'','ab4','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(112,150,'2018-11-1',4,'','ab4','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(113,140,'2017-11-1',4,'','ab4','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(114,130,'2016-9-1',4,'','ab4','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(115,120,'2018-10-1',4,'','ab4','bc1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(116,110,'2018-10-1',4,'','bc1','ab1','hjohn@gmail.com',13);
INSERT INTO rides VALUES(117,100,'2018-10-1',4,'','bc1','bc2','hjohn@gmail.com',13);
INSERT INTO rides VALUES(118,10,'2015-11-11',2,'','ab1','ab2','ljohn@gmail.com',20);
INSERT INTO rides VALUES(119,10,'2015-10-11',2,'','ab1','ab2','ljohn@gmail.com',20);
INSERT INTO rides VALUES(120,10,'2015-09-11',2,'','ab1','ab2','ljohn@gmail.com',20);
INSERT INTO rides VALUES(121,10,'2015-08-11',2,'','ab1','ab2','ljohn@gmail.com',20);
INSERT INTO rides VALUES(122,30,'2018-12-10',3,'','ab1','ab4','mjohn@gmail.com',21);
INSERT INTO rides VALUES(123,30,'2017-12-10',3,'','ab1','ab4','mjohn@gmail.com',21);
INSERT INTO rides VALUES(124,30,'2018-10-10',3,'','ab1','ab4','mjohn@gmail.com',21);
INSERT INTO rides VALUES(131,20,'2018-10-14',3,'','ab1','ab4','mjohn@gmail.com',21);
INSERT INTO rides VALUES(132,10,'2018-10-15',4,'','ab1','ab4','mjohn@gmail.com',21);
INSERT INTO rides VALUES(125,30,'2018-12-10',3,'','ab1','bc1','mjohn@gmail.com',21);
INSERT INTO rides VALUES(126,30,'2018-12-10',3,'','bc1','ab4','mjohn@gmail.com',21);
INSERT INTO rides VALUES(127,10,'2018-12-12','','','bc1','ab1','pjohn@gmail.com',22);
INSERT INTO rides VALUES(128,10,'2018-12-12','','','bc1','ab3','pjohn@gmail.com',22);
INSERT INTO rides VALUES(129,10,'2018-12-12','','','bc1','ab4','pjohn@gmail.com',22);
INSERT INTO rides VALUES(130,10,'2018-12-12','','','bc1','ab5','pjohn@gmail.com',22);
INSERT INTO rides VALUES(914,10,'2018-08-08','','','bc888','bc1','q8@gmail.com',22);
INSERT INTO rides VALUES(915,10,'2018-08-09','','','bc888','bc2','q8@gmail.com',22);
INSERT INTO rides VALUES(916,10,'2018-08-10','','','bc999','bc888','q8@gmail.com',22);
INSERT INTO rides VALUES(917,10,'2018-08-11','','','bc888','bc999','q8@gmail.com',22);
--INSERT INTO rides VALUES(601,20,'2018-06-01','','','ab6','ab4','pjohn@gmail.com',22);
INSERT INTO rides VALUES(918,10,'2012-01-20','','','ab2','ab1','q81@gmail.com',22);
INSERT INTO rides VALUES(919,10,'2014-01-20','','','ab1','ab2','q81@gmail.com',22);
INSERT INTO rides VALUES(920,10,'2015-01-20','','','ab1','ab3','q81@gmail.com',22);
INSERT INTO rides VALUES(921,10,'2017-03-23','','','ab2','ab4','q81@gmail.com',22);
INSERT INTO rides VALUES(777,20,'2018-11-07','','','ab3','ab5','pjohn@gmail.com',22);
INSERT INTO rides VALUES(778,20,'2018-11-07','','','ab3','ab5','pjohn@gmail.com',22);
INSERT INTO rides VALUES(308,20,'2014-12-16','','','on300','on301','ljohn@gmail.com',20);
INSERT INTO rides VALUES(309,20,'2014-12-17','','','on300','on301','ljohn@gmail.com',20);
INSERT INTO rides VALUES(310,20,'2014-12-18','','','on300','on301','ljohn@gmail.com',20);
INSERT INTO rides VALUES(1002,55,'2018-12-01',1,'no luggage','ab2','ab5','joe@gmail.com',2);
INSERT INTO rides VALUES(1003,60,'2018-12-13',3,'light','ab1','ab5','mjohn@gmail.com',21);
INSERT INTO rides VALUES(1005,10,'2018-12-29',2,'no luggage','ab2','ab5','pjohn@gmail.com',2);


-- Populate bookings
INSERT INTO bookings VALUES(10,'davood@abc.com',100,NULL,1,'ab2',NULL);
INSERT INTO bookings VALUES(12,'davood@abc.com',101,28,1,'ab2','ab5');
INSERT INTO bookings VALUES(14,'paul@a.com',100,NULL,1,NULL,NULL);
INSERT INTO bookings VALUES(15,'joe@gmail.com',100,10,2,'ab1','ab4');
INSERT INTO bookings VALUES(16,'fjohn@gmail.com',100,10,2,'ab1','ab4');
INSERT INTO bookings VALUES(17,'ejohn@gmail.com',104,10,1,'ab1','ab4');
INSERT INTO bookings VALUES(18,'ejohn@gmail.com',105,10,1,'ab1','ab4');
INSERT INTO bookings VALUES(19,'ejohn@gmail.com',106,10,1,'ab1','bc1');
INSERT INTO bookings VALUES(20,'ejohn@gmail.com',107,10,1,'bc1','ab4');
INSERT INTO bookings VALUES(21,'ejohn@gmail.com',108,10,1,'ab4','ab1');
INSERT INTO bookings VALUES(22,'ejohn@gmail.com',122,10,3,'ab1','ab4');
INSERT INTO bookings VALUES(23,'ejohn@gmail.com',124,10,2,'ab1','ab4');
INSERT INTO bookings VALUES(24,'ejohn@gmail.com',125,10,1,'ab1','ab4');
INSERT INTO bookings VALUES(25,'ejohn@gmail.com',111,10,3,'ab1','ab4');
INSERT INTO bookings VALUES(26,'ejohn@gmail.com',112,10,2,'ab1','ab4');
INSERT INTO bookings VALUES(27,'ejohn@gmail.com',113,10,1,'ab1','ab4');
INSERT INTO bookings VALUES(28,'ejohn@gmail.com',115,10,2,'ab1','ab4');
INSERT INTO bookings VALUES(29,'ejohn@gmail.com',132,10,6,'ab1','ab4');
INSERT INTO bookings VALUES(30,'pjohn@gmail.com',777,12,4,'ab2','ab4');
INSERT INTO bookings VALUES(31,'pjohn@gmail.com',778,12,4,'ab2','ab4');
INSERT INTO bookings VALUES(102,'pjohn@gmail.com',1003,60,3,'ab1','ab5');
INSERT INTO bookings VALUES(105,'ejohn@gmail.com',1002,55,2,'ab1','ab4');
INSERT INTO bookings VALUES(106,'ejohn@gmail.com',1005,55,1,'ab2','ab5');

-- Populate requests
INSERT INTO requests VALUES(1,'paul@a.com','2018-12-22','ab3','bc1',80);
INSERT INTO requests VALUES(2,'davood@abc.com','2018-12-24','ab1','ab7',30);
INSERT INTO requests VALUES(3,'fjohn@gmail.com','2018-12-13','ab1','ab4',50);
INSERT INTO requests VALUES(4,'fjohn@gmail.com','2018-12-12','ab1','ab4',60);
INSERT INTO requests VALUES(5,'fjohn@gmail.com','2018-12-12','ab1','ab4',40);
INSERT INTO requests VALUES(6,'fjohn@gmail.com','2018-12-12','ab2','ab4',50);
INSERT INTO requests VALUES(7,'fjohn@gmail.com','2018-12-12','bc1','ab4',50);
INSERT INTO requests VALUES(8,'fjohn@gmail.com','2018-12-12','ab1','ab5',50);
INSERT INTO requests VALUES(9,'fjohn@gmail.com','2018-12-12','ab1','ab6',50);

-- Populate enroute
INSERT INTO enroute VALUES(122, 'ab3'); -- Rashed (Q6)
INSERT INTO enroute VALUES(116, 'bc2'); -- Rashed (Q6)