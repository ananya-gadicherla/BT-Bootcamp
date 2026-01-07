--40. Get females diagnosed with heart attack

SELECT m.*
FROM memberinfo m
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '1'
AND c.cardioarrestdetected = 1;