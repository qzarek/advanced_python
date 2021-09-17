def parse(query: str) -> dict:
    my_dict = {}
    try:
        split_str = query.split("?")[1].split("&")
        for key_ in split_str:
            split_key = key_.split("=")
            if len(split_key) > 1:
                my_dict.update({split_key[0]: split_key[1]})
    except IndexError:
        my_dict = {}
    return my_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    my_dict = {}
    try:
        split_str = query.split(";")
        for key_ in split_str:
            split_key = key_.split("=", 1)
            if len(split_key) > 1:
                my_dict.update({split_key[0]: split_key[1]})
    except IndexError:
        my_dict = {}
    return my_dict



if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
