import os
from os import listdir
from os.path import isfile, join
from pprint import pprint

if __name__ == '__main__':
    # clean up previous tests
    os.system("rm reports -r")

    #run the behave tests
    os.system("behave --junit --format pretty")

    # convert the junit repotrs to HTML for easier viewing
    myPath = "reports"
    os.mkdir("reports/xml")
    os.mkdir("reports/html")

    xmlsReports = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    if(xmlsReports):
        print("\n*******************************************************")
        print("Produced Reports")
        print("*******************************************************")

        for index, xmlReport in enumerate(xmlsReports):
            os.system(f"mv reports/{xmlReport} reports/xml/{xmlReport}")
            xmlPath = f"reports/xml/{xmlReport}"
            htmlPath = f"reports/html/{xmlReport.replace('.xml','.html')}"
            os.system(f"junit2html {xmlPath} {htmlPath}")
            print(f"\t{index+1}) {htmlPath}")
        print("*******************************************************\n")


