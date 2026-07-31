import requests
from datetime import datetime, timezone


def get_today_news():

    try:

        # Forex Factory calendar API alternative
        url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )


        data = response.json()


        today = datetime.now(
            timezone.utc
        ).strftime("%Y-%m-%d")


        today_news = []


        week_news = []


        for item in data:


            currency = item.get(
                "country",
                ""
            )


            impact = item.get(
                "impact",
                ""
            )


            date = item.get(
                "date",
                ""
            )


            title = item.get(
                "title",
                ""
            )


            if currency == "USD" and impact == "High":


                week_news.append(item)



                if today in date:


                    today_news.append(item)



        # اگر امروز خبر قرمز داشت

        if today_news:


            text = "📰 اخبار مهم امروز USD:\n\n"


            for n in today_news:


                text += (
                    f"⏰ {n.get('time','')}\n"
                    f"🇺🇸 {n.get('title','')}\n"
                    f"Actual: {n.get('actual','-')}\n"
                    f"Forecast: {n.get('forecast','-')}\n"
                    f"Previous: {n.get('previous','-')}\n\n"
                )


            return text



        # اگر امروز خبری نبود

        text = (
            "📰 اخبار مهم امروز USD:\n\n"
            "امروز خبر قرمز مهمی برای دلار آمریکا وجود ندارد.\n\n"
        )


        if week_news:


            text += "آخرین خبرهای مهم هفته:\n\n"


            for n in week_news[:3]:


                text += (
                    f"🇺🇸 {n.get('title','')}\n"
                    f"📅 {n.get('date','')}\n\n"
                )



        return text



    except Exception as e:


        return (
            "📰 اخبار اقتصادی:\n\n"
            "دریافت تقویم اقتصادی موقتاً ناموفق بود.\n"
        )
