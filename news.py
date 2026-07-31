import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_today_news():

    try:

        url = "https://www.forexfactory.com/calendar"

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }


        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )


        if response.status_code != 200:

            return (
                "⚠️ دسترسی به تقویم اقتصادی ممکن نیست."
            )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        events = []


        rows = soup.select(
            "tr.calendar__row"
        )


        for row in rows:


            text = row.get_text(
                " ",
                strip=True
            )


            # فقط خبرهای آمریکا و مهم
            if (
                "USD" in text
                and
                (
                    "High"
                    in text
                    or
                    "red"
                    in str(row)
                )
            ):

                events.append(text)



        if not events:

            return (
                "📰 امروز خبر قرمز مهم USD پیدا نشد."
            )



        result = "📰 اخبار مهم امروز USD:\n\n"


        for item in events[:5]:

            result += (
                "🔴 "
                + item
                + "\n\n"
            )


        return result



    except Exception as e:


        return (
            "❌ خطای تقویم اقتصادی: "
            + str(e)
        )
