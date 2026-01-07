--10. Get total number of blood tests done for Aberson

SELECT COUNT(*) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c on b.cardiodiagnosis_cardio_id=c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.lastname = 'Aberson';