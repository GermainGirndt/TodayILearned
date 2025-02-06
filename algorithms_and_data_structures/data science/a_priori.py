transactions = [
    (1, {'beer', 'cola'}),
    (2, {'sausage', 'chips', 'peach'}),
    (3, {'beer', 'cola'}),
    (4, {'cheese', 'beer', 'cola'}),
    (5, {'bread', 'sausage', 'cheese'}),
    (6, {'bread', 'sausage', 'peach'}),
    (7, {'peach', 'bread'}),
    (8, {'sausage', 'bread', 'cola', 'peach'})
]


def find_unique_articles(transactions: list) -> set[str]:
    unique_articles = set()
    for _, items in transactions:
        unique_articles.update(items)
    return unique_articles


def find_support(article: str, transactions: list) -> int:
    return sum(1 for _, items in transactions if article in items)


def find_support_for_set(article_set: frozenset, transactions: list) -> int:
    return sum(1 for _, items in transactions if article_set.issubset(items))


def filter_articles_with_min_support(min_support: int, transactions: list, article_sets: set[frozenset[str]]) -> set[frozenset[str]]:
    return {article_set for article_set in article_sets if find_support_for_set(article_set, transactions) >= min_support}


def a_priori(min_support: int, transactions: list) -> list[set[frozenset[str]]]:
    print(f"Calculating itemsets with minimum support of {min_support}\n")

    unique_articles = find_unique_articles(transactions)
    unique_article_sets = {frozenset({article}) for article in unique_articles}

    f_1 = filter_articles_with_min_support(
        min_support, transactions, unique_article_sets)

    all_f_k: list[set[frozenset[str]]] = [f_1]
    k = 2

    while all_f_k[-1]:
        candidates: set[frozenset[str]] = set()

        f_k_minus_1 = all_f_k[-1]  # Last level frequent sets

        for article_a in f_k_minus_1:
            for article_b in f_k_minus_1:
                union_set = article_a | article_b  # Merge sets
                if len(union_set) == k:
                    candidates.add(union_set)

        f_k = filter_articles_with_min_support(
            min_support, transactions, candidates)

        if not f_k:
            break

        all_f_k.append(f_k)
        k += 1

    return all_f_k


# Run the algorithm
min_support = 3
articles = a_priori(min_support, transactions)

# Print results
print("\nAll transactions:")
for transaction in transactions:
    print(transaction)

print("\n------")
print("\n\nFrequent itemsets:\n")
for i, articles_set in enumerate(articles):
    print(f"Itemsets of size {i + 1} with support >= {min_support}:")
    for article_set in articles_set:
        print(article_set)
    print()
