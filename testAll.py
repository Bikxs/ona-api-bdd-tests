import os
import shutil
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    # clean up previous tests
    reportsPath = "reports"
    if os.path.exists(reportsPath):
        shutil.rmtree(reportsPath)
    # run the behave tests
    os.system("behave --junit --format pretty")

    # convert the junit reports to HTML for easier human viewing
    os.mkdir(f"{reportsPath}/xml")
    os.mkdir(f"{reportsPath}/html")

    xmlsReports = [f for f in listdir(reportsPath) if isfile(join(reportsPath, f))]
    if (xmlsReports):
        print("\n*******************************************************")
        print("Produced Reports")
        print("*******************************************************")

        for index, xmlReport in enumerate(xmlsReports):
            shutil.move(f"{reportsPath}/{xmlReport}",f"{reportsPath}/xml/{xmlReport}")
            xmlPath = f"{reportsPath}/xml/{xmlReport}"
            htmlPath = f"{reportsPath}/html/{xmlReport.replace('.xml', '.html')}"
            os.system(f"junit2html {xmlPath} {htmlPath}")
            print(f"\t{index + 1}) {htmlPath}")
        print("*******************************************************\n")
