import pandas as pd

teams = {
    "Динамо": 45,
    "Шахтар": 52,
    "Зоря": 38,
    "Дніпро-1": 41,
    "Олександрія": 33,
    "Ворскла": 29,
    "Колос": 24,
    "Верес": 19,
    "Металіст": 27,
    "Чорноморець": 22
}


df = pd.DataFrame(list(teams.items()), columns=["Команда", "Очки"])


df["Матчі"] = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
df["Перемоги"] = [14, 16, 12, 13, 10, 9, 7, 5, 8, 6]

print(df.head(3))

print("\nТипи даних:")
print(df.dtypes)

print("\nРозмір DataFrame (рядки, стовпці):")
print(df.shape)

print("\nОписова статистика:")
print(df.describe())


df["Очки за матч"] = df["Очки"] / df["Матчі"]
print("\nDataFrame з новим стовпцем 'Очки за матч':")
print(df)


print("\nКоманди з очками більше 30:")
print(df[df["Очки"] > 30])


print("\nКоманди від найкращих за очками:")
print(df.sort_values(by="Очки", ascending=False))

grouped = df.groupby("Перемоги")["Очки"].mean().reset_index()
print("\nСереднє значення очок за кількістю перемог:")
print(grouped)

max_points = df.groupby("Матчі")["Очки"].max().reset_index()
unique_teams = df["Команда"].nunique()

print("\nМаксимальна кількість очок для кожної кількості матчів:")
print(max_points)

print("\nКількість унікальних команд:", unique_teams)
