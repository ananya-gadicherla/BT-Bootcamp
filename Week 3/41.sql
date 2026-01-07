--41. Female members aged above 50 with cardio info

SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '1'
AND m.age > 50;