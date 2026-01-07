--50. Avg age of heart attack patients per state & gender

SELECT a.state, m.gender, AVG(m.age) AS avg_age
FROM memberinfo m
JOIN addressinfo a ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c ON m.member_id = c.memberinfo_member_id
WHERE c.cardioarrestdetected=1
GROUP BY a.state, m.gender;