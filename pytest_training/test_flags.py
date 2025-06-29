def test_sample1():

    print("sample1")

def test_sample2():
    print("sample2")

    # i am using flags like   pytest -h      for help
                            # pytest -rA     to print both passed and failed tests
                            # pytest -v      to print details test results
                            # pytest -k      for keywords like below
                            # pytest -k "1"                   it will run methods having 1
                            # pytest -k "not 2"               it will run all methods other than methods having 2
                            # pytest -k " one or 2" -rA       it will run methods either one or 2 and print test results for passed and failed tests
                            # pytest test_flags.py            to run specific file from project

                            # Reports
                            # pytest -rA --junit-xml="first_file.xml"   to generate xml reports
                            # pytest -rA --html="report_html.html"      to generate html reports

                            # Markers
                            # pytest -rA -m smoke           to run markers having smoke only
                            # pytest -rA -m, regression     to run markers having regression only
                            # pytest -rA -m "smoke or regression"     to run either smoke or regression

                            # custom markers
                            # refer pytest.ini file for defining custom markers and usage is same as user defined markers
                            # pytest -vs  to print tests in detail and print all the print statements in those tests
                            # pytest -rA pytest_training/test_fixture_with_conftest_1.py  pytest_training/test_fixture_with_conftest_2.py   to run only two files at a time from package
                            # pytest - rA - -html = "conftest_autouse/report.html" conftest_autouse
                            # pytest -n 3   it executes the tests parallely depending on the given number ( here it executes 3 functions at a time)
                            # pytest -vs -n 3 conftest_autouse  we can use other flags also with pytest-xdist