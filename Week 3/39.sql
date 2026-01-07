--39. Get members and their diseases

SELECT m.firstname, m.lastname, d.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d ON c.cardio_id=d.cardiodiagnosis_cardio_id ;