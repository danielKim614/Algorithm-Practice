def have_to_be_expired(today, date, duration):
    today_year_int, today_month_int, today_day_int = map(int, today.split("."))
    date_year_int, date_month_int, date_day_int = map(int, date.split("."))
    duration_int = int(duration)

    date_month_int = date_month_int + duration_int
    if date_month_int > 12:
        year, month = divmod(date_month_int, 12)
        if month == 0:
            year -= 1
            month = 12
        date_year_int += year
        date_month_int = month
    
    today_int = 10000 * today_year_int + 100 * today_month_int + today_day_int
    date_int = 10000 * date_year_int + 100 * date_month_int + date_day_int

    if today_int >= date_int:

        return True
    else:
        return False

def solution(today, terms, privacies):
    result = []
    # Define terms for dictionary
    term_dict = dict()
    for term in terms:
        privacy_type, duration = term.split(" ")
        term_dict[privacy_type] = duration

    # Calculate duration of privacies
    for i in range(len(privacies)):
        date, privacy_type = privacies[i].split(" ")
        duration = term_dict[privacy_type]
        if have_to_be_expired(today, date, duration):
            result.append(i + 1)

    return result