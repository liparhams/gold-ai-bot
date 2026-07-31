import requests
from datetime import datetime


def get_today_news():

    try:

        url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


        response = requests.get(
            url,
            timeout=20
        )


        events = response.json()


        today = datetime.utcnow().strftime(
            "%Y-%m-%d"
        )


        important = []


        for event in events:

            if (
                event.get("country") == "USD"
                and event.get("impact") == "High"
                and today in event.get("date","")
            ):

                important.append(event)



        if not important:

            return (
                "📰 اخبار امروز USD\n\n"
                "امروز خبر قرمز مهم آمریکا وجود ندارد."
            )



        text = "📰 اخبار مهم امروز USD\n\n"



        for x in important:


            text += f"""
⏰ {x.get('time','')}
🇺🇸 {x.get('title','')}

Actual: {x.get('actual','-')}
Forecast: {x.get('forecast','-')}
Previous: {x.get('previous','-')}

"""


        return text



    except Exception as e:


        return (
            "📰 اخبار امروز USD\n\n"
            "تقویم اقتصادی در دسترس نیست."
        )
