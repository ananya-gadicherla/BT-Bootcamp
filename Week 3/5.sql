--5. Get all members from city 'Burgos'

SELECT m.*
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';
