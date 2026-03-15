-- 판매 중인 상품 중 가장 높은 판매가를 출력하는 SQL을 작성하시오
-- MAX_PRICE로 지정해주세요.

SELECT MAX(PRICE) as MAX_PRICE
FROM PRODUCT