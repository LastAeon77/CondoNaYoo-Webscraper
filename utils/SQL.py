def insertIntoSQL(Vinvestor,originalName,g):
    g = g.fillna("Not Available")
    ins = Vinvestor.insert().values(name_th = originalName,
                                    realName_th = g.iloc[0][1],
                                    Owner =g.iloc[1][1],
                                    Area = g.iloc[2][1],
                                    Number_of_Buildings = g.iloc[3][1],
                                    Floors = g.iloc[4][1],
                                    Room = g.iloc[5][1],
                                    Room_size_and_feature = g.iloc[6][1],
                                    Total_Parking = g.iloc[7][1],
                                    Total_Lifts = g.iloc[8][1],
                                    Zone = g.iloc[9][1],
                                    Public_Transports = g.iloc[10][1],
                                    Passing_Transport_Vehicles = g.iloc[11][1],
                                    Address = g.iloc[12][1],
                                    Schedule = g.iloc[13][1],
                                    Year_Construction_Completed = g.iloc[14][1],
                                    Price = g.iloc[15][1],
                                    Price_per_Square_Meter = g.iloc[16][1],
                                    Common_fee_and_funds = g.iloc[17][1],
                                    Nearby_Important_Locations = g.iloc[18][1],
                                    Conveniences = g.iloc[19][1],
                                    Highlights = g.iloc[20][1]
                                   )
    return ins