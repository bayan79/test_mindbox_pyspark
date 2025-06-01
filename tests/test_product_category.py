from unittest import TestCase

from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set

from method.product_category_join import get_product_with_category


class ProductCategoryJoinTest(TestCase):
    def setUp(self) -> None:
        self.spark: SparkSession = (
            SparkSession.builder.master("local[*]").appName("PySpark").getOrCreate()
        )

    def test_join_success(self):
        products = self.spark.read.csv(
            "tests/data/products.csv",
            header=True,
            inferSchema=True,
        )
        categories = self.spark.read.csv(
            "tests/data/categories.csv",
            header=True,
            inferSchema=True,
        )
        prod_cat = self.spark.read.csv(
            "tests/data/prod_cat.csv",
            header=True,
            inferSchema=True,
        )

        result = get_product_with_category(products, categories, prod_cat)
        result.show()

        # check all products are selected
        self.assertSetEqual(
            {
                "apple",
                "orange",
                "banana",
                "potato",
                "pineapple",
                "tomato",
                "wierd smelly thing",
            },
            set(result.select(collect_set("product_name")).first()[0]),
        )

        # check "nuts" cat not selected
        self.assertFalse(
            bool(result.filter(result.category_name.contains("nuts")).collect())
        )
