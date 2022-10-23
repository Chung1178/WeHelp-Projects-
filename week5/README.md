### 目標三

**利⽤要求⼆建立的資料庫和資料表，寫出能夠滿⾜以下要求的 SQL 指令：**

1. 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
CREATE database websitetest;
USE websitetest;
CREATE TABLE member(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count int unsigned NOT NULL default 0,
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO member(name, username, password, follower_count) VALUES ('Allen', 'test', 'test', 100);
INSERT INTO member(name, username, password, follower_count) VALUES ('Ethan', 'aa', 'aa', 200);
INSERT INTO member(name, username, password, follower_count) VALUES ('Vicky', 'bb', 'bb', 300);
INSERT INTO member(name, username, password, follower_count) VALUES ('Craig', 'cc', 'cc', 400);
INSERT INTO member(name, username, password, follower_count) VALUES ('Zoe', 'dd', 'dd', 500);
```
2. 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
SELECT * FROM member;
```
![image3-1](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/3-1.png?raw=true)

3. 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```
SELECT * FROM member ORDER BY time desc;
```
![image3-2](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/3-2.png?raw=true)

4. 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
SELECT * FROM member ORDER BY time desc LIMIT 1,3;
```
![image3-3revise](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/3-3revise.png?raw=true)

5. 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```
SELECT * FROM member WHERE username='test';
```
![image3-4](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/3-4.png?raw=true)

6. 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT * FROM member WHERE username='test' and password='test';
```
![image3-5](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/3-5.png?raw=true)

7. 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```
UPDATE member SET name='test2' WHERE username='test';
```
![image3-6](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/3-6.png?raw=true)

---

### 目標四

**利⽤要求⼆建立的資料庫和資料表，寫出能夠滿⾜以下要求的 SQL 指令：**

1. 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
SELECT COUNT(id) FROM member;
```
![image4-1](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/4-1.png?raw=true)

2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
SELECT SUM(follower_count) FROM member;
```
![image4-2](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/4-2.png?raw=true)

3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
SELECT AVG(follower_count) FROM member;
```
![image4-3](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/4-3.png?raw=true)

---

### 目標五

**建立message並insert資訊**
```
CREATE TABLE message(
	id BIGINT PRIMARY KEY auto_increment,
    member_id BIGINT NOT NUll,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME DEFAULT current_timestamp,
    FOREIGN KEY (member_id)
    REFERENCES member(id)
);
INSERT INTO message(member_id, content, like_count) VALUES (1, '嗨', 5);
INSERT INTO message(member_id, content, like_count) VALUES (2, '你好', 10);
INSERT INTO message(member_id, content, like_count) VALUES (3, '安安', 8);
INSERT INTO message(member_id, content, like_count) VALUES (4, '哈囉', 6);
INSERT INTO message(member_id, content, like_count) VALUES (5, '掰掰', 1);
INSERT INTO message(member_id, content, like_count) VALUES (1, '又是我', 6);
INSERT INTO message(member_id, content, like_count) VALUES (1, '來騙讚', 8);
INSERT INTO message(member_id, content, like_count) VALUES (1, '呵呵呵', 2);
```
![image5-1](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/5-1.png?raw=true)
![image5-1-2](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/5-1-2.png?raw=true)

1. 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
```
SELECT member.name, message.content FROM member 
INNER JOIN message ON member.id=message.member_id;
```
![image5-2](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/5-2.png?raw=true)

2. 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
```
SELECT member.name, message.content FROM member 
INNER JOIN message ON member.id=message.member_id WHERE member.username="test";
```
![image5-3](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/5-3.png?raw=true)

3. 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
```
SELECT AVG(message.like_count) FROM member 
INNER JOIN message ON member.id=message.member_id WHERE member.username="test";
```
![image5-4](https://github.com/Chung1178/WeHelp-Projects-/blob/main/week5/5-4.png?raw=true)

---
