create table weather
(
    eventdate date,
    temp      int
);
create table ice_types
(
    id   int,
    name  varchar
);

create table sales
(
    eventdate date,
    shop_id   int,
    ice_type_id int
);

