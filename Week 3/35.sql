--35. Get total number of cities per state

SELECT a.state, COUNT(DISTINCT city) AS city_count,
COUNT(CASE WHEN m.gender='1' THEN 1 END) AS female_count,
COUNT(CASE WHEN m.gender='0' THEN 1 END) AS male_count
FROM addressinfo a
JOIN memberinfo m ON a.memberinfo_member_id=m.member_id
GROUP BY a.state;
