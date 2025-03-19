SELECT DISTINCT DEV.ID, DEV.EMAIL, DEV.FIRST_NAME, DEV.LAST_NAME
FROM DEVELOPERS DEV
    JOIN SKILLCODES SKILL ON DEV.SKILL_CODE & SKILL.CODE
WHERE SKILL.NAME IN ('Python', 'C#')
ORDER BY DEV.ID ASC