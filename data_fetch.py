import requests;

def data_fetch():
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    response = requests.get(url)
    data = response.json()
    if 'products' in data:
        products = data['products'].values()
        # print(products)
        return list(products)
    else:
        raise ValueError("No 'products' key found in JSON data.")

if __name__ == "__main__":
    products = data_fetch() #lists of dictionaries
    print("Data is fetched successfully from API.")