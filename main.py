# データセットを検索タスク用の形式にして保存するスクリプト


# %%
# データの読み込み
import pandas as pd

dataset_dir = "shopping_queries_dataset"

# 読み込みで失敗する場合，Git LFSでpullしてから再度実行してください
# 参考: https://zenn.dev/medicalforce/articles/2daf62952100a1
df_examples = pd.read_parquet(
    f"{dataset_dir}/shopping_queries_dataset_examples.parquet",
    engine="fastparquet",
)
df_products = pd.read_parquet(
    f"{dataset_dir}/shopping_queries_dataset_products.parquet",
    engine="fastparquet",
)
df_sources = pd.read_csv(f"{dataset_dir}/shopping_queries_dataset_sources.csv")
# %%
