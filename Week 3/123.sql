-- 1. Get all the predictions
SELECT * FROM cardiodiagnosis

-- 2. Get all the predictions for the day.
SELECT * FROM cardiodiagnosis c
WHERE c.date = CURRENT_DATE

--3. Get all the predictions for the day and sort them based on the highest probability percentage at
--the top
SELECT *
FROM cardiodiagnosis cd
WHERE cd.date = CURRENT_DATE
ORDER BY cd.cardioarrestdetected DESC;
