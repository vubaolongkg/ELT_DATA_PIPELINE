-- Dòng này báo cho dbt biết: "Hãy tạo bảng này từ bảng raw_products"
{{ config(materialized='table') }}

SELECT
    id as product_id,
    title as product_name,
    price,
    category,
    description,
    image,
    -- Ép kiểu dữ liệu (casting) nếu cần
    rating_rate::float as rating,
    rating_count::int as review_count
FROM
    raw_products
WHERE
    id IS NOT NULL