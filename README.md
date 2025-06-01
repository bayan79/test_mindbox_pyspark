### Method to join products with categories
## Task
```
В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. 

Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.
```

## install
```
pip install -r requirements.txt
```

## tests
```
python -m unittest discover -s tests/
```

### example result
```
+------------------+-------------+
|      product_name|category_name|
+------------------+-------------+
|             apple|        fruit|
|            orange|        fruit|
|            banana|        fruit|
|            potato|    vegerable|
|         pineapple|        fruit|
|            tomato|    vegerable|
|wierd smelly thing|         NULL|
+------------------+-------------+
```