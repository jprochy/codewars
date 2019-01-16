WITH team (actor1, actor2, starts)
AS
(
  SELECT 
    fa2.actor_id, 
    fa1.actor_id AS costar, 
    count(fa1.actor_id) AS starts
  FROM 
    film_actor fa1, 
    film_actor fa2
  WHERE 
    fa1.film_id = fa2.film_id
    AND fa1.actor_id <> fa2.actor_id
  GROUP BY 
    fa2.actor_id, 
    fa1.actor_id
  ORDER BY 
    starts DESC, 
    fa2.actor_id
  LIMIT 1
)

SELECT a1.first_name||' '||a1.last_name AS "first_actor",
      a2.first_name||' '||a2.last_name AS "second_actor",
      f.title
FROM 
  actor a1, 
  actor a2, 
  team t, 
  film f
WHERE 
  t.actor1 = a1.actor_id
  AND t.actor2 = a2.actor_id
  AND f.film_id IN (
    SELECT 
      fa1.film_id 
    FROM 
      film_actor fa1, 
      film_actor fa2
    WHERE 
      fa1.film_id = fa2.film_id
      AND fa1.actor_id = a1.actor_id
      AND fa2.actor_id = a2.actor_id
);