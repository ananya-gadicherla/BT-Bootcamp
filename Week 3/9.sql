--9. Get members from cities 'Burgos' and 'Flora'

SELECT DISTINCT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city IN ('Burgos', 'Flora');