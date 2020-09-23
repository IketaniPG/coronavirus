from covid import Covid

covid = Covid()

def search_country(country_name : str):
    cases = covid.get_status_by_country_name(country_name)
    return cases