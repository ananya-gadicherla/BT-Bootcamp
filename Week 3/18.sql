--18. Cardio diagnosis where first name starts with and ends with 'A'

SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'A%A';