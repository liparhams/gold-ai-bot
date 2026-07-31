import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz



def get_today_news():

    url = "https://www.forexfactory.com/calendar"


    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }


    try:

        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )


        soup = BeautifulSoup(
            r.text,
            "lxml"
        )


        news = []


        rows = soup.select(
            "tr.calendar__row"
        )


        for row in rows:

            impact = row.select_one(
                ".calendar__impact"
            )


            country = row.select_one(
                ".calendar__country"
            )


            title = row.select_one(
                ".calendar__event"
            )


            if not impact or not country or not title:
                continue



            # فقط آمریکا

            if "USD" not in country.text:
                continue



            # فقط قرمز

            if "high" not in str(impact).lower():
                continue



            news.append(
                {
                "country":"USD",
                "event":title.text.strip()
                }
            )


        if not news:

            return "امروز خبر قرمز مهم آمریکا پیدا نشد."


        text = "📰 اخبار مهم امروز آمریکا:\n\n"


        for n in news:

            text += (
                f"🔴 {n['event']}\n"
                f"اثر احتمالی: بررسی روی دلار و XAUUSD\n\n"
            )


        return text



    except Exception as e:

        return f"خطا در اخبار: {e}"
