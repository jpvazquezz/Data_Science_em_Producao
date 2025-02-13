import pickle
import inflection
import numpy as np
import pandas as pd
import math
import datetime 


class Rossmann(object):
    
    def __init__(self ):
        self.home_path =''
        self.competition_distance_scaler = pickle.load(open('C:/Users/Dell/Desktop/ciencia_de_dados/0.Comunidade DS/0.Data_Science_em_Producao/Modulo_10_Deploy/competition_distance_scaler.pkl','rb'))
        self.competition_time_month_scaler = pickle.load(open('C:/Users/Dell/Desktop/ciencia_de_dados/0.Comunidade DS/0.Data_Science_em_Producao/Modulo_10_Deploy/competition_time_month_scaler.pkl','rb'))
        self.promo_time_week_scaler = pickle.load(open('C:/Users/Dell/Desktop/ciencia_de_dados/0.Comunidade DS/0.Data_Science_em_Producao/Modulo_10_Deploy/promo_time_week_scaler.pkl','rb'))
        self.year_scaler = pickle.load(open('C:/Users/Dell/Desktop/ciencia_de_dados/0.Comunidade DS/0.Data_Science_em_Producao/Modulo_10_Deploy/year_scaler.pkl','rb'))
        self.store_type_scaler = pickle.load(open('C:/Users/Dell/Desktop/ciencia_de_dados/0.Comunidade DS/0.Data_Science_em_Producao/Modulo_10_Deploy/store_type_scaler.pkl','rb'))
    
    def data_cleaning(self, df1):
        
        cols_old = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment', 'CompetitionDistance', 'CompetitionOpenSinceMonth', 
                'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek','Promo2SinceYear', 'PromoInterval']

        snakecase = lambda x: inflection.underscore(x)

        cols_new = list(map(snakecase, cols_old))
        df1.columns = cols_new
        # date to datetime
        df1['date'] = pd.to_datetime(df1['date'])

        # 'competition_open_since_year',
        df1['competition_open_since_year'] = df1.apply(lambda x: x['date'].month if math.isnan(x['competition_open_since_year']) else x['competition_open_since_year'], axis=1)

        # 'competition_open_since_month',

        df1['competition_open_since_month'] = df1.apply(lambda x: x['date'].month if math.isnan(x['competition_open_since_month']) else x['competition_open_since_month'], axis=1)

        # 'competition_distance' --> Muito distante a ponto de não ser encarada como competição 
        df1['competition_distance'] = df1['competition_distance'].apply(lambda x:200000 if math.isnan(x)else x)

        # 'promo2_since_year',
        df1['promo2_since_year'] = df1.apply(lambda x: x['date'].year if math.isnan(x['promo2_since_year']) else x['promo2_since_year'], axis=1)

        # 'promo2_since_week',
        df1['promo2_since_week'] = df1.apply(lambda x: x['date'].week if math.isnan(x['promo2_since_week']) else x['promo2_since_week'], axis=1)

        # 'promo_interval',

        month_map = {1:'Jan', 2:'Fev', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun',7:'Jul', 8:'Aug', 9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
 
        df1['month_map'] = df1['date'].dt.month.map(month_map)
        
        df1['is_promo'] = df1[['promo_interval', 'month_map']].apply( lambda x: 0 if x['promo_interval'] == 0 else 1 if x['month_map'] in x['promo_interval'].split( ',' ) else 0, axis=1 )

        # De float para int
        df1.competition_open_since_month = df1.competition_open_since_month.astype(int)
        df1.competition_open_since_year = df1.competition_open_since_year.astype(int)
        df1.promo2_since_week = df1.promo2_since_week.astype(int)
        df1.promo2_since_year = df1.promo2_since_year.astype(int)
        
        return df1
    
    def feature_engineering(self, df2):
        
        # Year
        df2['year'] =df2['date'].dt.year

        # Month
        df2['month'] =df2['date'].dt.month

        # Day 
        df2['day'] =df2['date'].dt.day

        # Week of year
        df2['week_of_year'] =df2['date'].dt.weekofyear

        # Year week
        df2['year_week'] =df2['date'].dt.strftime('%Y-%W')


        # competition since
        years = df2.loc[df2['competition_open_since_year']<1677, 'competition_open_since_year'].unique().tolist()
        years_dic = {7:2007, 6:2006, 5:2005, 4:2004, 3:2003, 2:2002, 1:2001, 12:2012, 11:2011, 10:2010, 9:2009, 8:2008}
        df2['competition_open_since_year'].replace(years_dic, inplace=True)
        df2['competition_since'] = df2.apply( lambda x: datetime.datetime( year=x['competition_open_since_year'], month=x['competition_open_since_month'],day=1 ), axis=1 )
        df2['competition_time_month'] = ( ( df2['date'] - df2['competition_since'] )/30 ).apply( lambda x: x.days ).astype( int )

        # promo since
        df2['promo_since'] = df2['promo2_since_year'].astype( str ) + '-' + df2['promo2_since_week'].astype( str )
        df2['promo_since'] = df2['promo_since'].apply( lambda x: datetime.datetime.strptime( x + '-1', '%Y-%W-%w' ) - datetime.timedelta( days=7 ) )
        df2['promo_time_week'] = ( ( df2['date'] - df2['promo_since'] )/7 ).apply( lambda x: x.days ).astype( int )

        # assortment
        df2['assortment'] = df2['assortment'].replace({'a':'basic', "b": 'extra', 'c':'extended'})

        # state holiday
        df2['state_holiday'] = df2['state_holiday'].replace({'a':'public holiday', 'b': 'Easter holiday', 'c':'Christmas', '0':'regular_day'})

        # 3.0 Filtragem de variáveis

        ## 3.1 Filtragem das linhas

        # Filtrar open (apenas dias de loja aberta) e sales (apenas vendas acima de 0)
        df2 = df2[(df2['open']!=0)]

        ## 3.2 Seleção das colunas

        df2.drop(['open', 'promo_interval', 'month_map'],axis=1, inplace=True)
        
        return df2

    
    def data_preparation(self,df5):
        

        ## 5.2 Rescaling
        # Competition distance 
        df5['competition_distance'] = self.competition_distance_scaler.fit_transform(df5[['competition_distance']].values)
        # Competition time month 
        df5['competition_time_month'] = self.competition_time_month_scaler.fit_transform(df5[['competition_time_month']].values)

        # Promo time weak
        df5['promo_time_week'] = self.promo_time_week_scaler.fit_transform(df5[['promo_time_week']].values)
        # Year
        df5['year'] = self.year_scaler.fit_transform(df5[['year']].values)


        ## 5.3 Transformação dos dados
        ### 5.3.1 Encoding

        # state_holiday - One Hot Encoding
        df5 = pd.get_dummies( df5, prefix=['state_holiday'], columns=['state_holiday'] )

        # store_type - Label Encoding
        df5['store_type'] = self.store_type_scaler.fit_transform( df5['store_type'] )

        # assortment - Ordinal Encoding
        assortment_dict = {'basic': 1,  'extra': 2, 'extended': 3}
        df5['assortment'] = df5['assortment'].map( assortment_dict )

        ### 5.3.3 Transformação de Natureza dos dados
        # Day of week
        df5['day_of_week_sin'] = df5['day_of_week'].apply(lambda x: np.sin(x*(2* np.pi/7)))
        df5['day_of_week_cos'] = df5['day_of_week'].apply(lambda x: np.cos(x*(2* np.pi/7)))

        # Month
        df5['month_sin'] = df5['month'].apply(lambda x: np.sin(x*(2* np.pi/12)))
        df5['month_cos'] = df5['month'].apply(lambda x: np.cos(x*(2* np.pi/12)))

        # Day
        df5['day_sin'] = df5['day'].apply(lambda x: np.sin(x*(2* np.pi/30)))
        df5['day_cos'] = df5['day'].apply(lambda x: np.cos(x*(2* np.pi/30)))
        # Week of year
        df5['week_of_year_sin'] = df5['week_of_year'].apply(lambda x: np.sin(x*(2* np.pi/52)))
        df5['week_of_year_cos'] = df5['week_of_year'].apply(lambda x: np.cos(x*(2* np.pi/52)))
        
        cols_selected = ['store','promo','store_type',
        'assortment', 'competition_distance','competition_open_since_month', 'competition_open_since_year','promo2','promo2_since_week','promo2_since_year','competition_time_month','promo_time_week',
        'day_of_week_sin', 'day_of_week_cos',  'month_sin', 'month_cos', 'day_sin','day_cos','week_of_year_sin','week_of_year_cos']
        
        return df5[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        #  prediction
        pred = model.predict(test_data)
        
        # join pred into the original data
        
        original_data['prediction'] = np.expm1(pred)
        
        return original_data.to_json(orient='records', date_format='iso')
        