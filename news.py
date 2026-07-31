import requests
from bs4 import BeautifulSoup



def get_today_news():


    url="https://www.forexfactory.com/calendar"



    headers={
        "User-Agent":
        "Mozilla/5.0"
    }



    try:


        r=requests.get(
            url,
            headers=headers,
            timeout=20
        )


        soup=BeautifulSoup(
            r.text,
            "lxml"
        )



        result=[]


        for row in soup.select(
            "tr.calendar__row"
        ):


            country=row.select_one(
                ".calendar__country"
            )


            impact=row.select_one(
                ".calendar__impact"
            )


            event=row.select_one(
                ".calendar__event"
            )



            if not country or not impact or not event:
                continue



            if "USD" in country.text:

                if "high" in str(impact).lower():


                    result.append(
                        "🔴 "+event.text.strip()
                    )



        if not result:

            return "امروز خبر قرمز مهم آمریکا وجود ندارد."



        return "\n".join(result)



    except Exception as e:

        return "خطای خبر: "+str(e)
