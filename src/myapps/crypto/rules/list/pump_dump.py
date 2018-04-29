# Calculate pump / dump pair information
def get_results(start_price, end_price):

    result = {}

    if (start_price * end_price) > 0:
        result['result'] = format(((end_price - start_price) / start_price) * 100, '.2f')
        if float(result['result']) > 0:
            result['move'] = 'up'
        elif float(result['result']) < 0:
            result['move'] = 'down'
        else:
            result['move'] = 'flat'
    else:
        result['result'] = None

    return result