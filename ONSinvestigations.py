import covid_data_retrievers as cvd
import matplotlib.pyplot as plt
import pandas as pd
import datetime

data = cvd.ONSData()

def formatRange(dateRange: str):
    return datetime.datetime.strptime(dateRange.split(' to ')[0].strip(), '%d %B %Y')

def plotSummaryPositivityAndIncidence(data: cvd.ONSData):
    pData = data.summaryPositivity()
    iData = data.summaryIncidence()
    fig = plt.figure(figsize=(10, 8))
    gs = fig.add_gridspec(2, hspace=0)
    axs = gs.subplots(sharex=True)
    fig.suptitle('Graphs of Summary Rates over Time Periods')

    pDates = list(map(formatRange, pData['England']['Time period']))
    axs[0].plot(pDates, pData['England']['Estimated average % of the population that had COVID-19'])
    axs[0].set_ylabel('Estimated Percentage of the\nPopulation Positive for Covid-19')
    axs[0].fill_between(pDates, pData['England']['95% Lower confidence/credible Interval'], pData['England']['95% Upper confidence/credible Interval'],
        alpha=0.5)

    iDates=list(map(formatRange,iData['England']['Time period']))
    axs[1].plot(iDates, iData['England']['Estimated COVID-19 incidence rate per 10,000 people per day'])
    axs[1].set_ylabel('Number of Incidences\nper 10,000 people per day')
    axs[1].fill_between(iDates, iData['England']['95% Lower confidence/credible Interval'], iData['England']['95% Upper confidence/credible Interval'],
        alpha=0.5)

    axs[1].set_xlabel('Time period')
    labels = [d.strftime('%d %b %y') for d in pDates]
    axs[1].set_xticks(pDates[::5])
    axs[1].set_xticklabels(labels[::5], rotation=45)

    fig.tight_layout()
    plt.savefig('graphs/SummaryPositivityAndIncidenceRatesEngland.jpg')
    plt.show()

def plotPositivityByAgeGroup(data: cvd.ONSData):
    d = data.dailyPositivityByAgeGroup()
    meanCol = 'Modelled % testing positive for COVID-19'
    dates = d['Date']['Unnamed: 0_level_1']
    
    fig = plt.figure(figsize=(8, 8))

    fig.suptitle('Modelled Percentage of the Population Positive for Covid-19\nGrouped by Age Groups')
    
    line0,=plt.plot(dates, d['Age 2 to School Year 6'][meanCol])
    line1,=plt.plot(dates, d['School Year 7 to School Year 11'][meanCol])
    line2,=plt.plot(dates, d['School Year 12 to Age 24'][meanCol])
    line3,=plt.plot(dates, d['Age 25 to Age 34'][meanCol])
    line4,=plt.plot(dates, d['Age 35 to Age 49'][meanCol])
    line5,=plt.plot(dates, d['Age 50 to Age 69'][meanCol])
    line6,=plt.plot(dates, d['Age 70+'][meanCol])
    
    plt.ylabel('Estimated Percentaged Within the Age Group Positive for Covid-19 /%')
    labels = [d.strftime('%d %b %y') for d in dates]
    plt.xticks(dates[::5], labels[::5], rotation=45)

    plt.legend([line0, line1, line2, line3, line4, line5, line6],
        ['Age 2 - School Year 6', 'School Years 7 - 11', 'School Year 12 - Age 24', 'Ages 25 - 34', 'Ages 35 - 49', 'Ages 50 - 69', 'Ages 70+'])

    fig.tight_layout(pad=1)
    plt.savefig('graphs/PositivityByAgeGroup.jpg')
    plt.show()


def plotWeighted14DayByAgeGroup(data: cvd.ONSData):
    d = data.weighted14DayPositivityByAgeGroup()
    meanCol = 'Estimated % testing positive for Covid-19'
    dates = list(map(formatRange, d['Time period']['Unnamed: 0_level_1']))
    
    fig = plt.figure(figsize=(8, 8))

    fig.suptitle('Estimates of the Percentage of the Population Positive for Covid-19\nover Non-Overlapping 14 Day Windows Grouped by Age Groups')
    
    line0,=plt.plot(dates, d['Age 2 - Age 10/11\n(Age 2 - School year 6)'][meanCol])
    line1,=plt.plot(dates, d['Age 11/12 - Age 15/16\n(School Year 7 - School Year 11)'][meanCol])
    line2,=plt.plot(dates, d['Age 16/17 - Age 24\n(School Year 12 - Age 24)'][meanCol])
    line3,=plt.plot(dates, d['Age 25 - Age 34'][meanCol])
    line4,=plt.plot(dates, d['Age 35 - Age 49'][meanCol])
    line5,=plt.plot(dates, d['Age 50 - Age 69'][meanCol])
    line6,=plt.plot(dates, d['Age 70+'][meanCol])
    
    plt.ylabel('Estimated Percentaged Positive for Covid-19 /%')
    labels = [d.strftime('%d %b %y') for d in dates]
    plt.xticks(dates[::5], labels[::5], rotation=45)

    plt.legend([line0, line1, line2, line3, line4, line5, line6],
        ['Age 2 - School Year 6', 'School Years 7 - 11', 'School Year 12 - Age 24', 'Ages 25 - 34', 'Ages 35 - 49', 'Ages 50 - 69', 'Ages 70+'])

    fig.tight_layout(pad=1)
    plt.savefig('graphs/14DayWeightedPositivityByAgeGroups.jpg')
    plt.show()

plotSummaryPositivityAndIncidence(data)
plotPositivityByAgeGroup(data)
plotWeighted14DayByAgeGroup(data)

