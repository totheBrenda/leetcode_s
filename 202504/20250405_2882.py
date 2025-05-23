## https://leetcode.com/problems/drop-duplicate-rows/

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=['email'], keep='first')
    return customers