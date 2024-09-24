Please run the following for requirements:
pip install -r requirements.txt 

When running by tags use the following:
behave -t @test --no-skipped

If you want to create a report of the run use the following:
behave -t @country -f html -o reports/behave_report_$(date +%Y%m%d_%H%M%S).html

If you want to open the report run the following:
xdg-open reports/behave_report_{timestamp#}.html

Easier method for running recently created report please do the following in terminal:
nano ~/.bashrc
alias latest_report='xdg-open $(ls -t reports/behave_report_*.html | head -1)'
behave_report() {
    behave -t "$1" -f html -o reports/behave_report_$(date +%Y%m%d_%H%M%S).html
}
behave_test() {
    behave -t "$1" --no-skipped
}
source ~/.bashrc

# To run a test run targeting @tags
behave_test @tag

#To run a report rest run targeting @tags
behave_report @tag

# to open recently created report 
latest_report

