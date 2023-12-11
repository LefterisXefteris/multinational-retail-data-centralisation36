from data_cleaning import retrieve_pdf_data
import tabula


class DataCleaning:
    
    def data_cleaning(self):
        df = tabula.read_pdf(retrieve_pdf_data())
        df = df.dropna(axis=0, how='any')
        df = df.dropna(axis=1, how='all')
    


df_displays = DataCleaning()
df_clean_test = df_displays.data_cleaning()
print(df_clean_test.head(10))