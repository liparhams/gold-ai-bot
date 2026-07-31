import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_today_news():

    try:

        url = "https://www.forexfactory.com/calendar"

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


        news = []

        rows = soup.select(
            "tr.calendar__row"
        )


        today = datetime.now().strftime(
            "%Y-%m-%d"
        )


        for row in rows:

            impact = row.select_one(
                ".impact"
            )

            currency = row.select_one(
                ".calendar__currency"
            )

            event = row.select_one(
                ".calendar__event"
            )


            if not impact or not currency or not event:
                continue


            # فقط آمریکا
            if currency.text.strip() != "USD":
                continue


            # فقط خبر قرمز
            if "red" not in impact.get(
                "class",
                []
            ):
                continue


            news.append(
                f"🔴 USD | {event.text.strip()}"
            )


        if not news:
            return "امروز خبر قرمز مهم آمریکا پیدا نشد."


        return "\n".join(news[:10])


    except Exception as e:

        return (
            "خطا در دریافت اخبار: "
            + str(e)
        )
