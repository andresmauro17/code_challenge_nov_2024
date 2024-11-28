"""
Overview:
Create a Python script that demonstrates key Python skills, including making 
an HTTP GET request, using list comprehension with a conditional filter, type 
checking, and utilizing f-strings.

Requirements:
Fetch Data: 
Write a Python script to perform an HTTP GET request to fetch JSON data from a 
public API (example URL: https://jsonplaceholder.typicode.com/todos).


Process Data with Conditional List Comprehension:
Extract titles from the JSON data, but only include those that contain a 
specific string (e.g., 'qui').
Implement this using list comprehension.


Display Results with f-Strings:
Format and print the filtered titles using f-strings.
Ensure that each printed title is a string.


Type Checking:
Demonstrate checking whether one of the extracted titles is of type int.


Notes:
Aim for clear, efficient, and concise code.
Basic error handling is encouraged, but focus on the core functionalities.
You can use online resources for reference, but ensure the coding is your own 
work.

Please record your coding session using a screen recorder, explaining your
thought process as you write the script.

Provide the result in a publicly viewable Google Doc link, with the link to 
the session recording included inside.

"""

import requests


def fetch_data():
    """
    this function is to get a request from the endpoint
    json_ data = fetch_data()
    """
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            timeout=5
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("An error occurs trying to do a get request")
        print(e)


def filter_data(json_data, query_string):
    """
    filtering the data according the querystring
    filtered_data = filter_data(json_data, 'qui')
    """
    return [item for item in json_data if query_string in item["title"]]


def display_results(json_data):
    """
    display the results
    """
    for item in json_data:
        print(f"item {item['id']} | user: {item['userId']} | {item['title']}")


def check_if_exists_an_integer_title(json_data):
    """
    check if in the list exists an title that is an integer
    exists = check_if_exists_an_integer_title(json_data)
    """
    is_an_integer = False
    for item in json_data:
        if isinstance(item["title"], int):
            is_an_integer = True
    return is_an_integer


def main():
    """
    main function
    """
    print("fetching data......")
    json_data = fetch_data()
    if json_data:
        print(len(json_data))
        filtered_data = filter_data(json_data, "qui")
        print(len(filtered_data))
        print("displaying the results")
        display_results(json_data)

        print("exists an integer title:")
        exists = check_if_exists_an_integer_title(json_data)
        print("yes") if exists else print("no")
    print("something went wrong")


if __name__ == "__main__":
    main()
