-- 동물 보호소에 가장 먼저 들어온 -> min(DATETIME)
-- 동물은 언제 들어왔는지 조회하는 SQL문을 작성해주세요.

SELECT min(DATETIME) as 시간
from ANIMAL_INS