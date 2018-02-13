import pandas as pd
import numpy as np
import math


def LoadFile():
    df = pd.read_table('../input/itcont.txt' , sep ='|' , index_col = False ,  names =('CMTE_ID' , 'AMNDT_IND' ,' RPT_TP' , ' TRANSACTION_PGI' , ' IMAGE_NUM' , 'TRANSACTION_TP' , 'ENTITY_TP' ,'NAME' , 'CITY', 'STATE' , 'ZIP_CODE','EMPLOYER','OCCUPATION','TRANSACTION_DT','TRANSACTION_AMT','OTHER_ID','TRAN_ID','FILE_NUM','MEMO_CD','MEMO_TEXT','SUB_ID'   )  , lineterminator='\n')
    df1 = df[['CMTE_ID' , 'NAME' ,'ZIP_CODE' ,'OTHER_ID' ,'TRANSACTION_DT','TRANSACTION_AMT']]
    return (df1)

    
def CleanFile(dataframe):
     df = dataframe
     df1 = df.drop(df[df['ZIP_CODE'] < 10000].index)
     otherid_value = df1['OTHER_ID'].isna()
     df3 = df1[otherid_value ]
     df3 = df3.dropna(subset=["CMTE_ID","NAME" , "ZIP_CODE" ,"TRANSACTION_DT" , "TRANSACTION_AMT"])
     df3['TRANSACTION_DT'] = pd.to_datetime(df3['TRANSACTION_DT'] , format = '%m%d%Y')
     df3['YEAR'] = df3['TRANSACTION_DT'].dt.year
     df3['ZIP_CODE'] = df3[['ZIP_CODE']].astype(str)
     #print (df3.dtypes)
     df3['ZIP_CODE'] = df3.ZIP_CODE.str.slice(0, 5)
     #print (df3)
     return df3

     
def PercentileContribution(a):
    AmountList = a
    #print (AmountList)
    N = len(AmountList)
    file = open("../input/percentile.txt", "r")
    Percentile = file.read()
    Percentile = int(Percentile)
    #print (Percentile)
    OrdinalRank = (Percentile/100)*N
    #print(OrdinalRank)
    RankPercentile = math.floor(OrdinalRank)
    #print (RankPercentile)
    file.close()
    return (RankPercentile)

    
def RepeatDonor(dataframe):
    DictDonors = dict()
    
    Recipients= []
    df = dataframe
    count =0
    AmountList =[]
    df1 = pd.DataFrame(columns=[ 'CMTE_ID','ZIP_CODE' ,'YEAR' , 'percentile_contribution' , 'Total_contribution' , 'number_of_contributions'])
    for row in df.itertuples():
        count = count +1
        #print (count)
        name_donor = (getattr(row, "NAME"))
        zip_donor = (getattr(row, "ZIP_CODE"))
        cmte = (getattr(row, "CMTE_ID"))
        amt = (getattr(row, "TRANSACTION_AMT"))
        yr = (getattr(row, "YEAR"))
        #print (DictDonors)
        #print (zip_donor, name_donor)
        if ( name_donor , zip_donor) in DictDonors.items():

            Recipients.append(cmte)
            #print ("nsnjxfne is " , Recipients)
            AmountList.append(amt)
            #print(AmountList)
            nO_of_contri = Recipients.count(cmte)

            PositionsCmte = [i for i,val in enumerate(Recipients) if val== cmte ]
            #print("t is " , PositionsCmte)

            total =0
            rank_amount=[]
            for i in range(0,len(PositionsCmte)):


                P = PositionsCmte[i]
                #print(P)
                q = (AmountList[P])
                rank_amount.append(q)
                #print (rank_amount)
                total =  total +AmountList[P]

            rank_amount = sorted(rank_amount)
            contri = PercentileContribution(rank_amount)
            #print (contri)
            contri = (rank_amount[contri])
            #print (contri)
            df1 = df1.append({  'CMTE_ID' : cmte , 'ZIP_CODE' : zip_donor , 'number_of_contributions' : nO_of_contri,'YEAR' : yr , 'Total_contribution' : total , 'percentile_contribution': contri }, ignore_index=True)
        else :
            DictDonors[name_donor] = zip_donor

    return (df1)


def main():
     df = LoadFile()
     df1 = CleanFile(df)
     #print (df1 )
     df_final = RepeatDonor(df1)
     df_final.to_csv(path_or_buf = "../output/repeat_donors.txt" , sep = "|", header= False , index = False)



if __name__== "__main__":
  main()

