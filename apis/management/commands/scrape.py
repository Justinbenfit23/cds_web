from datetime import date
from email.policy import default
from operator import index
from numpy import insert
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.core.management.base import BaseCommand, CommandError
from sqlalchemy import create_engine
import json
import pandas as pd
import os
from dotenv import load_dotenv
from apis.models import CMC ###### figure out a way to incorporate this with the Command class
from uuid import uuid4
import datetime

load_dotenv()
api_key = os.getenv("cmc_api_key")


table = 'apis_cmc'
conn_string = os.getenv('DATABASE_URL')
db = create_engine(conn_string)
conn = db.raw_connection()

class Command(BaseCommand):
    def handle(self, *args, **options):
        help = "collect listing data"

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
        }
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
        }
        session = Session()

        def pull_latest_listings(url, parameters, headers, session):

            session.headers.update(headers)
            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)['data']
                return data
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                return e

        def extract_and_push_to_df(data): 
            num = 0
            lst = []
            
            for d in data:
                id = str(uuid4())
                inserted_at = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                last_updated = d['quote']['USD']['last_updated']
                name = d['name']
                symbol = d['symbol']
                price = d['quote']['USD']['price']
                market_cap = d['quote']['USD']['market_cap']
                market_cap_dominance = d['quote']['USD']['market_cap_dominance']
                fully_diluted_market_cap = d['quote']['USD']['fully_diluted_market_cap']
                percent_change_1h = d['quote']['USD']['percent_change_1h']
                percent_change_24h = d['quote']['USD']['percent_change_24h']
                percent_change_30d = d['quote']['USD']['percent_change_30d']
                percent_change_60d = d['quote']['USD']['percent_change_60d']
                percent_change_7d = d['quote']['USD']['percent_change_7d']
                percent_change_90d = d['quote']['USD']['percent_change_90d']
                volume_24h = d['quote']['USD']['volume_24h']
                volume_change_24h = d['quote']['USD']['volume_change_24h']

                d = {"id": id,
                "inserted_at": inserted_at,
                "last_updated": last_updated,
                "name": name, 
                "symbol": symbol, 
                "price": price, 
                "market_cap": market_cap, 
                "market_cap_dominance": market_cap_dominance,
                'fully_diluted_market_cap' : fully_diluted_market_cap,
                "percent_change_1h": percent_change_1h,
                "percent_change_24h": percent_change_24h,
                "percent_change_30d": percent_change_30d,
                "percent_change_60d": percent_change_60d,
                "percent_change_7d": percent_change_7d,
                "percent_change_90d": percent_change_90d,
                "volume_24h": volume_24h,
                "volume_change_24h": volume_change_24h}
                lst.append(d)
                num += 1
            df = pd.DataFrame(lst)
            return df
        today_listings = pull_latest_listings(url, parameters, headers, session)
        df = extract_and_push_to_df(today_listings)
        # def insert_to_db(self, df):
        #     self.CMC.objects.create(df)
        # insert_to_db(self, df)
        
        def see_results(self, cur, table):
            print("complete")
            cur.execute(f"SELECT * from {table}")
            results = cur.fetchall()
            print(results)
                    
        def execute_values(self, conn, engine, df, table): 
            # print(df)
            sql1 = df.to_sql(table, engine, if_exists='append', index=False)
            conn.autocommit = True
            cur = conn.cursor()
            # see_results(self, cur, table)
        execute_values(self, conn, db, df, table)
    

         
    

