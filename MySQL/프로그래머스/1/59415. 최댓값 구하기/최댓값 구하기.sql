-- 가장 최근에 들어온 동물은 언제들어왔는지 조회
SELECT MAX(datetime) as '시간'
from ANIMAL_INS