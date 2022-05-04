from requests_html import HTMLSession


class GetPublicHolidays:
        def __init__(self, url):
            self.url=url

        def get_page(self):

            s = HTMLSession()

            url = self.url
            r = s.get(url)

            return r
        
        def get_page_title(self):
            r = self.get_page()

            title = r.html.find('title')[0].text

            with open("output/title.txt", "w") as f:
                f.write(title)


        def get_table_data(self):

            url = self.url
            r = self.get_page()

            # table = r.html.find('table')[2]
            table = r.html.find('#main table')[0]
            tabledata = []

            dates = [[c.text.replace('\n', ', ').replace('&,', '&').replace('\xa0', ' ') for c in row.find('td')] for row in table.find('tr')][1:]
            holidays = [c.text for c in table.find('strong')][1:]
            years = [[c.text for c in row.find('th')] for row in table.find('tr')][0][1:]

            return [dates, holidays, years]


        def get_final_table(self):

            final_list = []

            dates, holidays, years = self.get_table_data()

            for i in range(len(dates)):
                for l in range(len(dates[i])):
                    l = [holidays[i], years[l], dates[i][l]]
                    final_list.append(l)

            return final_list





