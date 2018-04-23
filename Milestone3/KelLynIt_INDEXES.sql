--index for helping with query to get the reviews of friends
create index id_index on review (user_id, business_id)
