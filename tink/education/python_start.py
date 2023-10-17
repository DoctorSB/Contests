# 0) Для генерации данных в random необходимо установить seed = "АДВИ_2023", длина каждого списка N = 1000;


import pandas as pd
import random


def random_list(n):
    random.seed("АДВИ_2023")
    return [random.randint(0, 1000) for _ in range(n)]


print(len(random_list(1000)))

# 1) index колонка: создать список из N последовательных целых элементов от 1 до 1000 включительно, далее, с помощью специальной функции random перемешать его;


def index_column(n):
    return random.sample(range(1, n + 1), n)


print(len(index_column(1000)))

# 2) groups колонка: создать список из N элементов, состоящий из значений из списка ["группа_1", "группа_2", "группа_3", "группа_4", "группа_5"], необходимо использовать функцию из random которая возвращает список элементов длины k, выбранных из последовательности population с перестановкой элементов;


def groups_column(n):
    return random.choices(["группа_1", "группа_2", "группа_3", "группа_4", "группа_5"], k=n)


# 3) uniform колонка: создать список из N элементов, состоящий из целых значение из равномерного распределения [50, 100] ;

def uniform_column(n):
    return [random.randint(50, 100) for _ in range(n)]

# 4) gauss_1, gauss_2, gauss_3 колонки: Создать 3 списка из N элементов каждый, заполненные значениями из нормальных распределений с параметрами:
# n = 0, o2 = 1 -> gauss_1 третья колонка
# n = 0, o2 = 144 -> gauss_2 четвертая колонка
# n = 50, o2 = 81 -> gauss_3 пятая колонка


def gauss_column(n):
    return [random.gauss(0, 1) for _ in range(n)]


def gauss_column_2(n):
    return [random.gauss(0, 12) for _ in range(n)]


def gauss_column_3(n):
    return [random.gauss(50, 9) for _ in range(n)]

# 5) Создать pandas DataFrame, где (1) будет индексом, (2)-(4) колонки, названия колонок ["groups", "uniform", "gauss_1", "gauss_2", "gauss_3"] соответственно, не забывая проверить, что типы колонок должны соответствовать заявленным типам данных;


def create_dataframe(n):
    df = pd.DataFrame({"index": index_column(n), "groups": groups_column(n), "uniform": uniform_column(
        n), "gauss_1": gauss_column(n), "gauss_2": gauss_column_2(n), "gauss_3": gauss_column_3(n)})
    return df


df = create_dataframe(1000)

# 6) Для колонок gauss_1 и gauss_2 заменить значения на None: Для gauss_1, если индекс у значение делится на 121 без остатка; Для gauss_2, если дробная часть больше 0.95;


def replace_gauss_1(df):
    df.loc[df["index"] % 121 == 0, "gauss_1"] = None
    return df


def replace_gauss_2(df):
    df.loc[df["gauss_2"] % 1 > 0.95, "gauss_2"] = None
    return df


df = replace_gauss_1(df)
df = replace_gauss_2(df)

# 7) Теперь, для пропущенных значений gauss_1 и gauss_2: Для gauss_2 None заменить на среднее по колонке; Удалить строчки из таблицы, где gauss_1 == None.


def replace_gauss_2_mean(df):
    df["gauss_2"] = df["gauss_2"].fillna(df["gauss_2"].mean())
    return df


def delete_gauss_1(df):
    df = df.dropna(subset=["gauss_1"])
    return df


df = replace_gauss_2_mean(df)

df = delete_gauss_1(df)
print(df)

# Для колонки gauss_2 посчитать среднее и среднеквадратическое отклонение,


def mean_and_std(df):
    return round(df["gauss_2"].mean(), 2), round(df["gauss_2"].std(), 2)


print(mean_and_std(df))

# посчитать какая группа встречается чаще всего


def most_popular_group(df):
    return df["groups"].value_counts().idxmax()


print(most_popular_group(df))

# какой самый ранний индекс в 5 группе


def first_in_group(df):
    return df[df["groups"] == "группа_5"]["index"].min()


print(first_in_group(df))

# Сколько записей из колонки uniform имеют значение не ниже значения 90% перцентиля?


def count_uniform(df):
    return df[df["uniform"] >= df["uniform"].quantile(0.9)].shape[0]


print(count_uniform(df))


# У какой группы наибольшее значение медианы для gauss_3?

def group_with_max_median(df):
    return df.groupby("groups")["gauss_3"].median().idxmax()


print(group_with_max_median(df))

# У какой группы наибольшее минимальное значение uniform?


def min_max_value(df):
    return df.groupby('groups')['uniform']["gauss_2"]


print(min_max_value(df))
