-- fish_info 테이블에서 잡은 물고기 중
-- 가장 큰 물고기 -> max
-- 길이를 cm를 붙여 출력하는 sql을 작성하시오.
-- 컬럼명은 max_length로 지정하시오.

select CONCAT(MAX(LENGTH), 'cm') as MAX_LENGTH
from FISH_INFO