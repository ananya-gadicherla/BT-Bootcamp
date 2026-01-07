--44. Male members (<40) with diseases and symptoms

SELECT DISTINCT m.firstname,m.lastname,m.age ,d.*, s.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN symptom s ON c.cardio_id = s.cardiodiagnosis_cardio_id
JOIN diseasedetail d ON c.cardio_id=d.cardiodiagnosis_cardio_id
WHERE m.gender = '0'
AND m.age < 40;