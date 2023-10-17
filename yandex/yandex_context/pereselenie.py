def read_file(file):
    with open(file, "r") as fl:
        count = fl.read()
        return count


city_count = read_file("input.txt")
city_count = city_count.split()
price = list(map(int, city_count[1:]))
city_count = int(city_count[0])
answer = []
