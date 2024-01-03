from api_connection import get_api_data
from functions import return_top_coins


if __name__ == "__main__":
    num_coins = input("Enter how mainy coins' data you would like to receive:  ")
    data = get_api_data(num_coins)
    top_blank = return_top_coins(data)
    print(top_blank)