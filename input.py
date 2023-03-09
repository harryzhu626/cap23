
def user_input():
    origin_handle = 'company' # or any other company/entity handle

    domain_knowledge = [ # list of products/characters that belong to the company/entity 
        'product 1', 
        'product 2',
        'product 3',
    ]

    performance = { # company performance overtime, revenue, customer size, revenue per customer etc. 
        '01/2023': 120,
        '02/2023': 140,
        '03/2023': 170, 
    }

    return origin_handle, domain_knowledge, performance

if __name__ == '__main__':
    origin_handle, domain_knowledge, performance = user_input()