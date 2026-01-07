--15. Get X-ray details for member with last name 'Dailley'

SELECT x.*
FROM xray x
JOIN cardiodiagnosis c ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m ON c.memberinfo_member_id = m.member_id
WHERE m.lastname = 'Dailley';