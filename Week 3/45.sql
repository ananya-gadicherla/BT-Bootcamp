--45. Count of members from Mountain Province aged 50–60

SELECT COUNT(*) AS member_count
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province'
AND m.age BETWEEN 50 AND 60;