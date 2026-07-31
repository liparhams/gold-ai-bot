import requests
from datetime import datetime


def get_today_news():

    try:

        url="https://nfs.faireconomy.media/ff_calendar_thisweek.json"

        data=requests.get(
            url,
            timeout=20
        ).json()


        today=datetime.utcnow().strftime("%Y-%m-%d")


        result=[]


        for x in data:

            if (
                x.get("country")=="USD"
                and x.get("impact")=="High"
                and today in x.get("date","")
            ):

                result.append(x)



        if not result:

            return "امروز خبر قرمز مهم USD وجود ندارد."


        text="📰 اخبار مهم امروز USD:\n\n"


        for x in result:

            text += f"""
⏰ {x.get('time','')}
🇺🇸 {x.get('title','')}
Actual: {x.get('actual','-')}
Forecast: {x.get('forecast','-')}
Previous: {x.get('previous','-')}

"""


        return text


    except:

        return "تقویم اقتصادی در دسترس نیست."
