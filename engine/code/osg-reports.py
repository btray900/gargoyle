#!/usr/bin/env python
import re
import argparse
import time
import sys
import base64
from getpass import getpass
from fpdf import FPDF
from elasticsearch import Elasticsearch, ElasticsearchException
from elasticsearch.helpers import scan
from collections import Counter

#Handlers
from DbHandler import DbHandler
from CheckHandler import CheckHandler

class PDF(FPDF):

    def header(self):

        # self.set_title(self.title)
        # https: // pyfpdf.readthedocs.io / en / latest / Tutorial / index.html
#        self.image('assets/images/image_small.jpg', 10, 8, 44)
        self.ln(20)
        # Arial bold 15
        self.set_font('Arial', 'B', 25)
        self.set_line_width(1)
        # Title
        # Line break
        self.ln(10)

    def summary(self, report_title, pass_fail, host_count, gte, lte):
        # set title font
        self.set_font('Arial', 'B', 15)
        # move right to center title
        self.set_draw_color(211,211,211)
        self.cell(80)

        # write title
        self.cell(30, 10, report_title, 0, 0, 'C')
        # line break
        self.ln(15)
        # Background color
        self.set_fill_color(0, 159, 219)
        # Title
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, '  SUMMARY', 0, 1, 'L', 1)
        self.set_text_color(0, 0, 0)
        self.ln(2)
        self.set_font('Arial', '', 10)

        self.set_font('Arial', 'B', 10)
        self.cell(40, 10, 'Fail Issues:', 1, 0, 'L', 1)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, str(pass_fail), 1, 1, 'C')

        self.set_font('Arial', 'B', 10)
        self.cell(40, 10, 'Hosts Scanned:', 1, 0, 'L', 1)
        self.set_font('Arial', '', 10)
        self.cell(40, 10, str(len(host_count)), 1, 0, 'C')

        report_gen_dt = time.strftime("%m/%d/%y %H:%m")
        self.set_font('Arial', 'B', 10)
        self.cell(40, 10, 'Report Generated at:', 1, 0, 'L', 1)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, report_gen_dt, 1, 1, 'C', )

        self.set_font('Arial', 'B', 10)
        self.cell(40, 10, 'Report Start Date:', 1, 0, 'L', 1)
        self.set_font('Arial', '', 10)
        self.cell(40, 10, gte, 1, 0, 'C')

        self.set_font('Arial', 'B', 10)
        self.cell(40, 10, 'Report End Date:', 1, 0, 'L', 1)
        self.set_font('Arial', '', 10)
        self.cell(0, 10, lte, 1, 1, 'C')
        self.set_fill_color(255,255,255)
        self.ln(10)

    def details(self):
        self.set_fill_color(0, 159, 219)
        self.set_draw_color(211,211,211)
        self.set_font('Arial', 'B', 15)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, '  DETAILS', 0, 1, 'L', 1)
        self.set_fill_color(255,255,255)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, 'This report is generated using information from the Openstack Security Guide. Visit the links below for check info.', 1, 1, 'L')
        self.ln(10)



    def results(self):
        self.set_fill_color(0, 159, 219)
        self.set_draw_color(211,211,211)
        self.set_font('Arial', 'B', 15)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, '  RESULTS', 0, 1, 'L', 1)
        self.set_fill_color(255,255,255)
        self.set_text_color(0, 0, 0)
        self.ln(2)


    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 5, 'Page ' + str(self.page_no()) + '/{nb}', 0, 1, 'C')
        self.cell(0, 5, 'https://github.com/punkinnovation/gargoyle.git', 0, 0, 'C')


    def linkCell(self, width, text):
        checkUrl = 'https://docs.openstack.org/security-guide/'
        self.set_text_color(0,0,255)
        self.set_font('Arial', 'U', 10)
        self.cell(width, 10, text, 1, 0, 'C', 0, '%s/%s/checklist.html' % (checkUrl, text))
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)


    def statusCell(self, width, status):
        if 'Fail' in status or 'bad' in status:
            self.set_fill_color(255,0,0)
            self.set_draw_color(255,0,0)
        if 'Pass' in status or 'good' in status:
            self.set_fill_color(0,255,0)
            self.set_draw_color(0,255,0)
        self.cell(width, 10, '', 1, 0, 'C', 1) # empty cell
        self.set_draw_color(211,211,211)
        self.set_fill_color(242,242,242)


def build_pdf(report_on, data, gte, lte, component):
    '''
    Function to generate PDF using pyFPDF

    :param tuple report: Data from mySQL db about checkTask report is running for
    :param str report_on: Show only Failures, Passes or All in Report Summary [Pass, Fail, All]
    :param list: data Response from Elastic Search q
    :param str gte: Date start range for report
    :param str lte: Date end range for report
    :return:
    '''

    report_gen_day = time.strftime("%Y%m%d")
    match = report_on

    if 'cloudpassage' in index:
        host_count = Counter(sublist[1] for sublist in data)
        pass_fail = Counter(sublist[7] for sublist in data)
        zone_count = Counter(sublist[8] for sublist in data)
        pass_fail_count = pass_fail['bad']

        report_subject = component
        report_title = 'CloudPassage %s Report' % (report_subject.title())


    if 'gargoyle' in index:
        host_count = Counter(sublist[3] for sublist in data)
        pass_fail = Counter(sublist[6] for sublist in data)
        zone_count = Counter(sublist[11] for sublist in data)
        pass_fail_count = pass_fail['Fail']

        if component:
            report_subject = component

        if report_type:
           first = re.findall('^[a-z]*', report_type)
           rest = re.findall('[A-Z][a-z]*', report_type)
           reportTitle = '%s %s' % (first[0], ' '.join(rest))
           report_subject = reportTitle

        report_title = 'SVT %s Report' % (report_subject.title())


    title = '%s_%s.pdf' % (report_title.replace(' ','-'), report_gen_day)

    if len(data) == 0:
        print "No data found to report"
        sys.exit()


    # start build of PDF file output
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    pdf.summary(report_title, pass_fail_count, host_count, gte, lte)

    pdf.details()

    pdf.results()

    # remove duplicate node entries if multiple entries are found for the same node
    # Result Details

    # always print fails first

    for d in data:
        if 'Fail' in d[6]:
            printSvtIssues(pdf, d, 'Fail')

    if 'All' in match:
        for d in data:
            if 'Pass' in d[6]:
                printSvtIssues(pdf, d, 'Pass')

    pdf.output(title, 'F')
    return


def printSvtIssues(pdf, d, imageName):
# lame double tab TODO fix

        pdf.set_fill_color(242,242,242)

        # row 1
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(17, 10, 'Status', 1, 0, 'C', 1)
        pdf.cell(75, 10, 'Check', 1, 0, 'C', 1)
        pdf.cell(0, 10, 'Target', 1, 1, 'C', 1)

        # row 2
        pdf.set_font('Arial', '', 10)
        pdf.statusCell(17, d[6])
        pdf.linkCell(75, d[8]) # check type
        pdf.cell(0, 10, '%s' % d[5], 1, 1, 'C') #target

        # row 3
        pdf.set_font('Arial', 'B', 10)
        pdf.statusCell(17, d[6])
        pdf.cell(75, 10, 'Expected', 1, 0, 'C', 1)
        pdf.cell(0, 10, 'Actual', 1, 1, 'C', 1)

        # row 4
        pdf.set_font('Arial', '', 10)
        pdf.statusCell(17, d[6])
        # expected
        eString = d[18]
        if len(d[18]) > 32:
            eString = '%s [.snip.]' % d[18][:26]
        pdf.cell(75, 10, eString, 1, 0, 'C')
        # actual
        aString = d[0]
        if len(d[0]) > 32:
            aString = '%s [.snip.]' % d[0][:26]
        pdf.cell(0, 10, aString, 1, 1, 'C')

        # row 5
        pdf.set_font('Arial', 'B', 10)
        pdf.statusCell(17, d[6])
        pdf.cell(75, 10, 'Host', 1, 0, 'C', 1)
        pdf.cell(0, 10, 'Zone Info', 1, 1, 'C', 1)

        # row 6
        pdf.set_font('Arial', '', 10)
        pdf.statusCell(17, d[6])
        pdf.cell(75, 10, '%s' % d[3], 1, 0, 'C') # host
        pdf.cell(0, 10, '%s (%s) : %s : %s : %s' % (d[13], d[17], d[16], d[14], d[15]), 1, 1, 'C') # zone info

        pdf.cell(0, 10, '', 0, 1, 'L')

#        print d

        return # printIssues


def es_query(elastic_ip, report_type, gte, lte, component, index):
    '''
    Elasticsearch query function

    Generic elasticsearch query function.
    :param str elastic_ip: IP of Elastic Search Endpoint
    :param str report_type: Report type to execute corresponding Elasticsearch query
    :param str gte: report start date range
    :param str lte: report end date rage
    :return:
    '''

    es = Elasticsearch([elastic_ip], port=9200)
    data_resp = []
    query_body_hkc = {
        "_source": ["gargoyle*", "zoneJson*"],
        "query": {
            "bool": {
                "must": [
                    {"range": {"gargoyleTimestamp": {"gte": gte, "lte": lte}}},
                    {"match": {"gargoyleComponent": component}}
                ]
            }
        }
    }

    try:
        query_resp = scan(es, index="%s-*" % index, query=query_body_hkc)

    except ElasticsearchException as e:
        print e
        sys.exit()


    for r in query_resp:
        base = r['_source']

        if 'gargoyle' in index:

            # placeholder to send extra data if needed
            extra_val = ''
            gargoyle_actual = ''
            if base['gargoyleActual'] == '':
                gargoyle_actual = 'No data to report.'
            else:
                gargoyle_actual = base['gargoyleActual']
            # build new response object
            new_resp = [
                #base['gargoyleActual'],
                # base['gargoyleExpected'],
                gargoyle_actual, #0
                base['gargoyleCheckID'], #1
                base['gargoyleComponent'], #2
                base['gargoyleHostname'], #3
                base['gargoyleOutput'], #4
                base['gargoyleResource'], #5
                base['gargoyleResult'], #6
                base['gargoyleSeverity'], #7
                base['gargoyleTask'], #8
                base['gargoyleTimestamp'], #9
                base['gargoyleValueLogic'], #10
                base['gargoyleExpected'], #11
                ]

        data_resp.append(new_resp)
    return data_resp


def main(reports):
    '''
    Main function

    :param dict reports: list of checkTasks from DB with report_enabled=1
    :return:
    '''
    report_types = []
    components = []

    if reports:
        for r in reports:
            report_types.append(r[0])
            components.append(r[1])

    report_types = set(report_types)
    components = set(components)

    parser = argparse.ArgumentParser(description='Generate Security Verification Reports')
    parser.add_argument('-ip', '--elastic_ip', required=True,
                        help='Specify IP address of Elastic Search API endpoint (gargoyle-es-data) - e.g., 172.18.0.x ',)
    parser.add_argument('-c', '--component', required=False, help='SVT component name', choices=components, )
    parser.add_argument('-m', '--match', required=False, help='Report fails or all', nargs='?', choices=['All','Fail'],)
    parser.add_argument('-gte', '--gte', required=True, help='Specify report date range: Start date - e.g., NOTE: Takes datemath or date value'
                                                             'value. For more information: https://www.elastic.co/guide/en/e'
                                                             'lasticsearch/reference/current/common-options.html#date-math', )
    parser.add_argument('-lte', '--lte', required=True, help='Specify report date range: End date - \n NOTE: Takes datemath or date value'
                                                             'value. For more information: https://www.elastic.co/guide/en/e'
                                                             'lasticsearch/reference/current/common-options.html#date-math', )
    args = parser.parse_args()

    if not args.elastic_ip:
        print 'Elastic Search API IP address required'
        sys.exit()
    else:
        elastic_ip = args.elastic_ip

    if args.index:
        index = args.index

    for r in reports:
        if args.report_type == r[0]:
            report = r

    report_type = ''
    if args.report_type:
        report_type = args.report_type

    if not args.match:
        print 'Report on field required- All, Fail or Pass'
        sys.exit()
    else:
        report_on = args.match
        match = args.match

    if not args.lte:
        print 'Report range start date required - lte'
    else:
        lte = args.lte

    if not args.gte:
        print 'Report range end date required - gte'
    else:
        gte = args.gte

    component = ''
    if args.component:
        component = args.component

    # start query to elastic search
    data = es_query(elastic_ip, report_type, gte, lte, component, index)

    # build pdf
    build_pdf(report_on, data, gte, lte, component, report_type, index)


if __name__ == "__main__":
    db = DbHandler()
    chk = CheckHandler(db.cursor)
    reports = chk.getReports(cloud)
    db.conn.close()
    main(reports)
