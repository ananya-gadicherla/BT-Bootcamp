--48. Diseases for high BP (120–180), sorted by gender

SELECT m.gender, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN diseasedetail d ON c.cardio_id=d.cardiodiagnosis_cardio_id
WHERE b.bloodpressure BETWEEN 120 AND 180
ORDER BY m.gender;