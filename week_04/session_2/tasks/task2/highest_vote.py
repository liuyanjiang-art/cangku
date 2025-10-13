# Week 4, Session 2: Task 2

def most_frequent_string(votes):
    """
    This function identifies the string that appears most frequently
    (highest count) in the votes argument and returns it along with the count
    of its occurrences. It assumes there is a single most frequent string
    (i.e., no ties for the highest count)

    Args:
        votes (list): A list of strings representng votes,
        e.g. ['apples', 'bananas', 'grapes', 'tomatoes']

    Returns:
        - tuple: (str, int) where str is the string with the highest count,
        and int is the count of its occurences
        - None, None: if votes is empty.
    """

    # Your task is the complete the body of the function based on the
    # details in docstring.


Leeds = ['date', 'apple', 'cherry', 'date', 'apple', 'apple', 'elderberry',
         'date', 'elderberry', 'elderberry', 'date', 'banana']
Manchester = ['Jesy', 'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jade',
              'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jesy', 'Jade',
              'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne',
              'Leigh-Anne', 'Jade', 'Jesy', 'Jade', 'Perrie', 'Jade',
              'Jade', 'Jesy', 'Perrie', 'Perrie', 'Jade', 'Leigh-Anne',
              'Jesy', 'Jesy', 'Perrie', 'Jesy']


# Check if correct output is produced
print(most_frequent_string(Leeds))          # ('date', 4)
print(most_frequent_string(Manchester))     # ('Leigh-Anne', 10)
print(most_frequent_string([]))             # (None, None)

# Once completed, update the function to return all items that ties for the
# highest count in a list, e.g  (['apples', 'bananas'], 9). If there is no
# ties, return a single string and a value as usual, e.g ('apples, 9).
