문제1
CREATE TABLE posts(
	postId INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    PRIMARY KEY (postId)
);
문제2
ALTER TABLE posts
ADD (
	writer VARCHAR(100),
    created_at datetime
    );
문제3
ALTER TABLE posts
MODIFY
	content text;
문제4
ALTER TABLE posts
DROP COLUMN writer;
문제5
DROP TABLE posts;
문제6
CREATE TABLE IF NOT EXISTS posts(
	postId INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL,
    writer VARCHAR(20) NOT NULL,
    created_at datetime,
    PRIMARY KEY (postId)
);
문제7
DROP TABLE IF EXISTS posts;