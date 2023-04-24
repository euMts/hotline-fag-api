DROP DATABASE IF EXISTS game_db_construct;
CREATE DATABASE game_db_construct;
USE game_db_construct;

CREATE TABLE users(
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name varchar(255) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    experience int,
    PRIMARY KEY (user_id)
);

CREATE TABLE ranking(
    ranking_id INT NOT NULL AUTO_INCREMENT,
    created_at DATETIME,
    new_experience int,
    user_id int,
    user_name varchar(255),
    PRIMARY KEY (ranking_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Criando usuários
INSERT INTO users(user_name, created_at, updated_at, experience) VALUES ('Matheus', '2023-02-28 12:52:10', '2023-02-28 12:52:10', 0);
INSERT INTO users(user_name, created_at, updated_at, experience) VALUES ('Daniel', '2023-02-28 12:52:10', '2023-02-28 12:52:10', 0);
INSERT INTO users(user_name, created_at, updated_at, experience) VALUES ('Luis', '2023-02-28 12:52:10', '2023-02-28 12:52:10', 0);

-- Adicionar ao ranking pelo nome:
INSERT INTO ranking(created_at, new_experience, user_id, user_name) VALUES ('2023-02-28 12:54:10', 0, (SELECT user_id FROM users WHERE users.user_name = "Matheus"), "Matheus");
INSERT INTO ranking(created_at, new_experience, user_id, user_name) VALUES ('2023-02-28 12:54:10', 1, (SELECT user_id FROM users WHERE users.user_name = "Matheus"), "Matheus");
INSERT INTO ranking(created_at, new_experience, user_id, user_name) VALUES ('2023-02-28 12:54:10', 1, (SELECT user_id FROM users WHERE users.user_name = "Daniel"), "Daniel");
INSERT INTO ranking(created_at, new_experience, user_id, user_name) VALUES ('2023-02-28 12:54:10', 1, (SELECT user_id FROM users WHERE users.user_name = "Luis"), "Luis");
INSERT INTO ranking(created_at, new_experience, user_id, user_name) VALUES ('2023-02-28 12:54:10', 1, (SELECT user_id FROM users WHERE users.user_name = "Luis"), "Luis");

-- Verificar ranking:
-- SELECT * FROM ranking WHERE 1 = 1 ORDER BY ranking.new_experience DESC LIMIT 5;

-- Adicionar xp ao experience pelo nome:
-- UPDATE users SET users.experience = users.experience + 10 WHERE users.user_name = 'Matheus';

-- Remover xp do experience pelo nome:
-- UPDATE users SET users.experience = users.experience - 10 WHERE users.user_name = 'Matheus';

-- Verificar xp pelo nome
-- SELECT users.experience FROM users WHERE users.user_name = 'Matheus';