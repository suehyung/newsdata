#!/usr/bin/env python2.7.12

import psycopg2


def top3_articles():
    # Returns most popular 3 articles of all time by page views
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("select articles.title, count(*) as views from log join \
        articles on log.path = concat('/article/', articles.slug) where \
        log.status = '200 OK' group by articles.title order by views desc \
        limit 3")

    # Fetch results
    rows = c.fetchall()

    # Print results
    print
    print "Top 3 Articles By Views"
    for row in rows:
        print("Article: {:<40} Views: {:<8}".format(*row))

    db.close()


def top_authors():
    # Returns most popular authors of all time by page views
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("select authors.name, count(*) as views from log join \
        articles on log.path = concat('/article/', articles.slug) \
        join authors on authors.id = articles.author where log.status = \
        '200 OK' group by authors.name order by views desc")

    # Fetch results
    rows = c.fetchall()

    # Print results
    print
    print("Most Popular Authors By Views")
    for row in rows:
        print("Author: {:<30} Views: {:<8}".format(*row))

    db.close()


def error_days():
    """Returns days where > 1% of requests lead to errors"""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("create view errortable as select date(log.time) as day, \
        count(*) as errorcount from public.log where log.status != '200 OK' \
        group by date(log.time) order by day")
    c.execute("create view totaltable as select date(log.time) as day, \
        count(*) as totalcount from public.log group by date(log.time) \
        order by day")
    c.execute("create view percenttable as select totaltable.day as day, \
        round(errortable.errorcount * 100.0 / totaltable.totalcount, 1) as \
        errorpercent from totaltable join errortable on totaltable.day = \
        errortable.day order by totaltable.day")
    c.execute("select day, errorpercent from percenttable where errorpercent \
        > 1.0 order by errorpercent desc")

    # Fetch results
    rows = c.fetchall()

    # Print results
    print
    print("Days With > 1 Percent Error Rate on Requests")
    for row in rows:
        print("Date: {:%B %d, %Y}       Error Rate: {:>4.1f}%".format(*row))

    db.close()


if __name__ == "__main__":
    top3_articles()
    top_authors()
    error_days()
