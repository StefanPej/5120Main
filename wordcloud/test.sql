create table order_fact as
select suburb as location,
    quarter_id,
    age_id,
    store_id,
    o.order_id,
    round(count(o.order_id) * weight_factor) as number_of_orders,
    sum(quantity * list_price) as total_order_cost
from order_temp o
    join monstore.order_items i on o.order_id = i.order_id
    join order_dim d on i.order_id = d.order_id
group by suburb,
    quarter_id,
    age_id,
    store_id,
    o.order_id,
    weight_factor
order by o.order_id;