SELECT * FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON users2.id = friendships.friend_id;

-- INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
-- VALUE
-- (10, 11, NOW(), NOW()),
-- (10, 13, NOW(), NOW()),
-- (10, 15, NOW(), NOW()),
-- (11, 10, NOW(), NOW()),
-- (11, 12, NOW(), NOW()),
-- (11, 14, NOW(), NOW()),
-- (12, 11, NOW(), NOW()),
-- (12, 14, NOW(), NOW()),
-- (13, 12, NOW(), NOW()),
-- (14, 10, NOW(), NOW()),
-- (14, 15, NOW(), NOW()),
-- (15, 11, NOW(), NOW()),
-- (15, 12, NOW(), NOW());

-- SELECT
-- users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name as friend_last_name
-- FROM user-- 
-- JOIN friendships ON users.id = friendships.user_id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

-- SELECT COUNT(id) FROM friendships;

SELECT
users.first_name,
users.last_name,
users2.first_name AS friend_first_name,
users2.last_name as fkriend_last_name
FROM users JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;