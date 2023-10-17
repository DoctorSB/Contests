import json


def build_category_tree(data):
    category_dict = {}
    root_id = 0

    for category in data:
        category_id = category['id']
        parent_id = category.get('parent', root_id)
        category_name = category['name']

        if category_id not in category_dict:
            category_dict[category_id] = {
                'name': category_name, 'id': category_id, 'next': []}

        if parent_id == root_id:
            category_dict[root_id]['next'].append(category_dict[category_id])
        else:
            if parent_id not in category_dict:
                category_dict[parent_id] = {'next': []}
            category_dict[parent_id]['next'].append(category_dict[category_id])

    return category_dict[root_id]['next']


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        data = []
        for _ in range(n):
            category_data = input().strip()
            category = json.loads(category_data)
            data.append(category)

        category_tree = build_category_tree(data)
        print(json.dumps(category_tree, indent=4))


if __name__ == "__main__":
    main()
