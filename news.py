import requests
from bs4 import BeautifulSoup
from datetime import datetime



def get_today_news():


    try:

        url = (
            "https://www.forexfactory.com/calendar"
        )


        headers = {

            "User-Agent":
            "Mozilla/5.0"

        }


        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )


        soup = BeautifulSoup(
            r.text,
            "html.parser"
        )


        today = datetime.utcnow().strftime(
            "%b %d"
        )


        news = []


        rows = soup.find_all(
            "tr"
        )


        for row in rows:


            text = row.get_text(
                " ",
                strip=True
            )


            if (
                "USD" in text
                and
                "High" in text
            ):

                news.append(
                    text
                )



        if news:

            return "\n".join(
                news[:5]
            )


        return "امروز خبر قرمز مهم USD پیدا نشد."



    except Exception as e:


        return (
            "خطا در دریافت خبر: "
            + str(e)
        )
