# 検索用データの前処理

Amazonが提供するShopping Queries Datasetを検索モデル学習用にいい感じに書き換える

## Dataset

We provide two different versions of the data set. One for task 1 which is reduced version in terms of number of examples and ones for tasks 2 and 3 which is a larger.

The training data set contain a list of query-result pairs with annotated E/S/C/I labels. The data is **multilingual** and it includes queries from **English**, **Japanese**, and **Spanish** languages. The examples in the data set have the following fields: `example_id`, `query`, `query_id`, `product_id`, `product_locale`, `esci_label`, `small_version`, `large_version`, `split`, `product_title`, `product_description`, `product_bullet_point`, `product_brand`, `product_color` and  `source`

The Shopping Queries Data Set is a large-scale manually annotated data set composed of challenging customer queries.

There are 2 versions of the dataset. The reduced version of the data set contains `48,300 unique queries` and `1,118,011 rows` corresponding each to a `<query, item>` judgement. The larger version of the data set contains `130,652 unique queries` and `2,621,738 judgements`. The reduced version of the data accounts for queries that are deemed to be **“easy”**, and hence filtered out. The data is stratified by queries in two splits train, and test.

A summary of our Shopping Queries Data Set is given in the two tables below showing the statistics of the reduced and larger version, respectively. These tables include the number of unique queries, the number of judgements, and the average number of judgements per query (i.e., average depth) across the three different languages.

|       | Total | Total | Total | Train | Train | Train | Test | Test | Test |
| ------------- | ---------- | ------------- | ---------- | ---------- | ------------- | ---------- | ---------- | ------------- | ---------- |
| Language      | \# Queries | \# Judgements | Avg. Depth | \# Queries | \# Judgements | Avg. Depth | \# Queries | \# Judgements | Avg. Depth |
| English (US)  | 29,844     | 601,354       | 20.15      | 20,888     | 419,653       | 20.09      | 8,956      | 181,701       | 20.29      |
| Spanish (ES)  | 8,049      | 218,774       | 27.18      | 5,632      | 152,891       | 27.15      | 2,417      | 65,883        | 27.26      |
| Japanese (JP) | 10,407     | 297,883       | 28.62      | 7,284      | 209,094       | 28.71      | 3,123      | 88,789        | 28.43      |
| Overall       | 48,300     | 1,118,011     | 23.15      | 33,804     | 781,638       | 23.12      | 14,496     | 336,373       | 23.20      |

***Table 1**: Summary of the Shopping queries data set for task 1 (reduced version) - the number of unique queries, the number of judgements, and the average number of judgements per query.*

|       | Total | Total | Total | Train | Train | Train | Test | Test | Test |
| ------------- | ---------- | ------------- | ---------- | ---------- | ------------- | ---------- | ---------- | ------------- | ---------- |
| Language      | \# Queries | \# Judgements | Avg. Depth | \# Queries | \# Judgements | Avg. Depth | \# Queries | \# Judgements | Avg. Depth |
| English (US)  | 97,345     | 1,818,825     | 18.68      | 74,888     | 1,393,063     | 18.60      | 22,458     | 425,762       | 18.96      |
| Spanish (ES)  | 15,180     | 356,410       | 23.48      | 11,336     | 263,063       | 23.21      | 3,844      | 93,347        | 24.28      |
| Japanese (JP) | 18,127     | 446,053       | 24.61      | 13,460     | 327,146       | 24.31      | 4,667      | 118,907       | 25.48      |
| Overall       | 130,652    | 2,621,288     | 20.06      | 99,684     | 1,983,272     | 19.90      | 30,969     | 638,016       | 20.60      |

***Table 2**: Summary of the Shopping queries data set for tasks 2 and 3 (larger version) - the number of unique queries, the number of judgements, and the average number of judgements per query.*


## Cite

Please cite original paper if you use this dataset for your own research:

```BibTeX
@article{reddy2022shopping,
title={Shopping Queries Dataset: A Large-Scale {ESCI} Benchmark for Improving Product Search},
author={Chandan K. Reddy and Lluís Màrquez and Fran Valero and Nikhil Rao and Hugo Zaragoza and Sambaran Bandyopadhyay and Arnab Biswas and Anlu Xing and Karthik Subbian},
year={2022},
eprint={2206.06588},
archivePrefix={arXiv}
}
```
## License

This project is licensed under the Apache-2.0 License.
