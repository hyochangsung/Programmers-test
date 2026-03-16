-- 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하시오
-- 이름이 Null인 경우는 집계x
-- 중복되는 이름은 하나로 칩니다 -> distinct

SELECT COUNT(distinct NAME) as count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL