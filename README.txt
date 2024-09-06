Please run the following for requirements:
pip install -r requirements.txt 

When running by tags use the following:
behave -t @test
If you want to create a report of the run use the following:
behave -t @your_tag -f html -o path/to/your/behave_report.html

If you want to open the report run the following:
xdg-open reports/behave_report.html



