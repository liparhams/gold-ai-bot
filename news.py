import requests
from datetime import datetime, timedelta


IRAN_OFFSET = timedelta(hours=3, minutes=30)


def iran_time(utc_time):

    try:

        dt = datetime.strptime(
            utc_time,
            "%Y-%m-%dT%H:%M:%S"
        )

        iran = dt + IRAN_OFFSET

        return iran.strftime(
            "%H:%M"
        )

    except:

        return "-"



def get_today_news():

    try:

        url = (
            "https://nfs.faireconomy.media/"
            "ff_calendar_thisweek.json"
        )


        r = requests.get(
            url,
            timeout=20
        )


        events = r.json()



        today = datetime.utcnow().strftime(
            "%Y-%m-%d"
        )



        news = []



        for e in events:


            if (
                e.get("country") == "USD"
                and e.get("impact") == "High"
                and today in e.get("date","")
            ):


                news.append(e)



        if not news:

            return """
📰 اخبار مهم USD امروز

✅ امروز خبر قرمز مهم آمریکا وجود ندارد.
"""



        text = """
📰 اخبار قرمز USD امروز

"""



        for e in news:


            time = iran_time(
                e.get("date","")
            )


            text += f"""
🔴 {e.get('title','')}

⏰ ساعت ایران: {time}

📊 پیش‌بینی: {e.get('forecast','-')}
📌 قبلی: {e.get('previous','-')}

"""



        return text



    except Exception as ex:


        return f"""
📰 اخبار USD

❌ خطا در دریافت تقویم اقتصادی
"""
