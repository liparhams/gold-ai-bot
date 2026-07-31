import requests
from datetime import datetime, timedelta


IRAN_TIME = timedelta(
    hours=3,
    minutes=30
)



def convert_iran_time(date):

    try:

        dt = datetime.fromisoformat(
            date.replace("Z","")
        )

        dt = dt + IRAN_TIME

        return dt.strftime(
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


        data = r.json()



        today = datetime.utcnow().strftime(
            "%Y-%m-%d"
        )



        result = []



        for item in data:


            if (

                item.get("country") == "USD"

                and item.get("impact") == "High"

                and today in item.get("date","")

            ):

                result.append(item)




        if not result:


            return """

📰 اخبار مهم USD امروز

✅ امروز خبر قرمز مهم آمریکا وجود ندارد.

"""



        text = """

📰 اخبار قرمز USD امروز

"""



        for n in result:


            text += f"""

🔴 {n.get('title','')}

⏰ ساعت ایران:
{convert_iran_time(n.get('date',''))}


📊 Forecast:
{n.get('forecast','-')}

📌 Previous:
{n.get('previous','-')}


"""



        return text[:3000]



    except Exception:


        return """

📰 اخبار USD امروز

❌ تقویم اقتصادی در دسترس نیست.

"""
