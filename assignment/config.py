#starting url
url = "https://www.commerce.wa.gov.au/labour-relations/public-holidays-western-australia"


#pandas df column names
columns = ['Holiday', 'Year', 'Date']


#connection parameters
db = 'db'
table_name = 'holidays'


#test parameters
holidays_test_list = ["New Year's Day", 'Labour Day', 'Australia Day', 'Easter Sunday', 'Good Friday',  'Easter Monday', 'Anzac Day', 'Western Australia Day', "Queen's Birthday #", 'Christmas Day', 'Boxing Day']
years_test_list = ['2024', '2023', '2022']
page_title = 'Public holidays in Western Australia | Department of Mines, Industry Regulation and Safety'