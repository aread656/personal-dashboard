# finance-tracker
An application for personal organisation. Currently is limited to the realms of finance tracking, with sample data currently being used and statistics calculated for the user to view and make deductions on their own financial habits. Uses a command line interface
At present, the program is made to fit a specific format of bank statement of the bank I use personally, the specifics of which are not shared on the public repository, but example statements of identical format will be available and generated for testing purposes.
# RUNNING INFO
- To run the tracker, use "python -m src.menu" command from repo root
- Generate sample transactions for analysis through selecting:
        - (Main menu) 3: Modify Transactions
        - 7: Generate Sample Transactions
    - Upon returning to the main menu, the transactions will be saved to "financeRecords.csv" by default. Analysis is then possible on these sample transactions through the rest of the menu