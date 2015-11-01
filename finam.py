import urllib2
import time
import datetime

def get_date_from_to(st_date, end_date):
   from_day =  str(st_date.day)
   from_month = str(st_date.month-1)
   from_year = str(st_date.year)
   from_date = str(from_day + "." + from_month + "." + from_year)

   to_day = str(end_date.day)
   to_month = str(end_date.month-1)
   to_year = str(end_date.year)
   to_date = str(to_day + "." + to_month + "." + to_year)

   from_dt = "&df=" + from_day + "&mf=" + from_month + "&yf=" + from_year + "&from=" + from_date
   to_dt = "&dt=" + to_day + "&mt=" + to_month + "&yt=" + to_year + "&to=" + to_date

   return from_dt + to_dt

start_date = datetime.date(2014, 3, 17)
end_date = datetime.date(2014, 6, 15)
instrument_code = 'SPFB.RTS-6.14'
instrument_id = 82553




def load_from_finam(instrument_id, instrument_code, start_date, end_date):

    url = 'http://195.128.78.52/'
    print '*** Start downloading reports from %d.%d.%d' % (start_date.day, start_date.month, start_date.year)

    report_st_iterate_date = start_date
    week = datetime.timedelta(days=7)
    week_plus_one = datetime.timedelta(days=8)
    while report_st_iterate_date < end_date:
        report_end_iterate_date = report_st_iterate_date + week
        if report_end_iterate_date > end_date: report_end_iterate_date = end_date

        file_name = instrument_code + "_" + str(report_st_iterate_date) + "-" + str(report_end_iterate_date)
        print "*** *** dowloading " + file_name + "..."
        request = file_name + "?market=14&em="+str(instrument_id)+"&code=" + instrument_code + \
                  get_date_from_to(report_st_iterate_date, report_end_iterate_date) + "&p=2&f=" + file_name + \
                  "&e=.csv&cn="+ instrument_code + "&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1"

        response = urllib2.urlopen(url + request)
        response = response.read().decode('utf8')

        s_file = open('data/' + file_name + ".csv", 'wb')
        s_file.write(response)
        s_file.close()

        report_st_iterate_date += week_plus_one
        time.sleep(5)


load_from_finam(instrument_id, instrument_code, start_date, end_date)