from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def get_product_with_category(products: DataFrame, categories: DataFrame, prod_cat: DataFrame):
    """
    Предполагаю структуру датафреймов (см тесты):

    products: product_id int64, product_name str
    categories: category_id int64, category_name str
    prod_cat: product_id int64, category_id int64

    """
    products_with_categories = (
        products.join(
            prod_cat,
            on="product_id",
            how="left"
        )
        .join(
            categories,
            on="category_id",
            how="left"
        )
        .select(
            col("product_name"),
            col("category_name")
        )
    )
    return products_with_categories