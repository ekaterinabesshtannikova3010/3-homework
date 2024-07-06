def get_mask_card_number(number) -> str:
    """
    Вызываем функцию для создания маски
    """
    number_list = []
    string = str(number)
    for i in range(len(string)):
        number_list.append(string[i])
        if i in range(6, 12):
            number_list[i] = "*"
    number_string = "".join(number_list)
    fin = number_string[0:4] + " " + number_string[4:8] + " " + number_string[8:12] + " " + number_string[12:16]
    return fin


def get_mask_account(score) -> str:
    """
    Вызываем функцию для создания маски
    """
    score_list = []
    string = str(score)
    for i in range(len(string)):
        score_list.append(string[i])
        if i in range(0, 16):
            score_list[i] = "*"
    score_string = "".join(score_list)
    final_string = "**" + score_string[-4:]
    return final_string
