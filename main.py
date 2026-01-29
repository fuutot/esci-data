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
# データのマージ
df_examples_products = pd.merge(
    df_examples,
    df_products,
    how="left",
    left_on=["product_locale", "product_id"],
    right_on=["product_locale", "product_id"],
)
# %%
# タスク1用データの抽出
df_task_1 = df_examples_products[df_examples_products["small_version"] == 1]
df_task_1_train = df_task_1[df_task_1["split"] == "train"]
df_task_1_test = df_task_1[df_task_1["split"] == "test"]

# %%
# 日本語のデータの抽出
df_task_1_train_ja = df_task_1_train[
    df_task_1_train["product_locale"] == "jp"
].reset_index(drop=True)
df_task_1_test_ja = df_task_1_test[
    df_task_1_test["product_locale"] == "jp"
].reset_index(drop=True)
df_task_1_train_ja


# %%
# 適合性ラベルの追加
# 適合性ラベルは以下のルールで付与
# 3: esci_labelが"E"(Exact)
# 2: esci_labelが"S"(Substitute)
# 1: esci_labelが"C"(Complement)
# 0: esci_labelが"I"(Irrelevant)
def map_esci_label_to_relevance(esci_label: str) -> int:
    if esci_label == "E":
        return 3
    elif esci_label == "S":
        return 2
    elif esci_label == "C":
        return 1
    elif esci_label == "I":
        return 0
    else:
        raise ValueError(f"Unknown esci_label: {esci_label}")


df_task_1_train_ja["relevance_label"] = df_task_1_train_ja["esci_label"].apply(
    map_esci_label_to_relevance
)
df_task_1_test_ja["relevance_label"] = df_task_1_test_ja["esci_label"].apply(
    map_esci_label_to_relevance
)
df_task_1_train_ja

# %%
# 必要なカラムの抽出
columns_to_keep = [
    "query",
    "query_id",
    "product_id",
    "product_title",
    "product_description",
    "relevance_label",
]
df_task_1_train_ja_final = df_task_1_train_ja[columns_to_keep]
df_task_1_test_ja_final = df_task_1_test_ja[columns_to_keep]
df_task_1_train_ja_final
# %%
# None値が含まれる行の削除
df_task_1_train_ja_final = df_task_1_train_ja_final.dropna().reset_index(drop=True)
df_task_1_test_ja_final = df_task_1_test_ja_final.dropna().reset_index(drop=True)
df_task_1_train_ja_final
# %%
# データの保存
output_dir = "output"
df_task_1_train_ja_final.to_csv(
    f"{output_dir}/task_1_train_ja.csv", index=False, encoding="utf-8"
)
df_task_1_test_ja_final.to_csv(
    f"{output_dir}/task_1_test_ja.csv", index=False, encoding="utf-8"
)
# %%
