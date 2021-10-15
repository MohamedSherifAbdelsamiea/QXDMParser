import datetime
import os
import geohash2 as geo

BRSRP_Filtered=''
RSRQ_Filtered=''
Serving_SNR=''
LTE_PCC_RSRP=''
geohash=''
Serving_Cell_Quality_RSRP=''
Serving_Cell_Quality_RSRQ=''
Avg_SNR=''
WB_CQI=''
best_thp_timestamp_1sec=''
Serving_SSB=''
count=1
os.mkdir('./Output')
f = open('./Output/5G_Post_Processing_Full.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tgeohash\tSystem Time  Slot\tSystem Time  Numerology\tSystem Time Frame\tNum PDSCH Status\
            \tCarrier ID\tTech ID\tConn Id\tRNTI Type\tHarq Id\tBand Type\tMod Type\tTB Size (Bytes)\tTotal Bits\tPhysical cell ID\
            \tNum ReTx\tRV\tDiscard_Mode\tMCS\tSCS_MU\
            \tNum Layers\tCRC State\tCRC status\tNDI\tBandwdith\tNew Tx Flag\
            \tNum_Rbs\tEARFCN\tTB_Index\tNum_RX\tBRSRP Filtered\tRSRQ Filtered\tServing_SNR\tWB CQI\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/5G_Signaling.txt',"w")
f.write("Summary of OTA Messages\n")
f.close()
f = open('./Output/5G_Events.txt',"w")
f.write("Summary of Event Messages\n")
f.close()
f = open('./Output/0xB97F_NR5G_ML1_Searcher_Measurement_Database_Update_Ext.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tRaster_ARFCN\tPCI\tPBCH_SFN\tNUM_Beams\tCell_Quality_RSRP\
            \tCell_Quality_RSRQ\tDetected_Beams_Num\tDetected_Beams_SSB_Index\tDetected_Beams_RX_Beam_Info_RX_Beam_Id\
            \tDetected_Beams_RX_Beam_Info_RX_Beam_RSRP\tDetected_Beams_NR2NR_Filtered_Tx_Beam_RSRP_L3\
            \tDetected_Beams_NR2NR_Filtered_Tx_Beam_RSRQ_L3\tDetected_Beams_L2NR_Filtered_Tx_Beam_RSRP_L3\
            \tDetected_Beams_L2NR_Filtered_Tx_Beam_RSRQ_L3\tbest_1sec\n")

f.close()
f = open('./Output/0xB975_NR5G_ML1_Serving_Cell_Beam_Management.txt',"w")
f.write("Time_Stamp\tLongitude\tLatitude\tPCI\tSSB Periodicity Serv Cell\tServing Beam SSB Index\
            \tBRSRP Filtered\tRSRQ Filtered\tFrequency Offset PPM\tTime Offset\tNum Detected Beams\
            \tTx Beam Index 0\tRSRP Value 0\tRSRQ Value 0\
            \tTx Beam Index 1\tRSRP Value 1\tRSRQ Value 1\
            \tTx Beam Index 2\tRSRP Value 2\tRSRQ Value 2\
            \tTx Beam Index 3\tRSRP Value 3\tRSRQ Value 3\
            \tTx Beam Index 4\tRSRP Value 4\tRSRQ Value 4\
            \tTx Beam Index 5\tRSRP Value 5\tRSRQ Value 5\
            \tTx Beam Index 6\tRSRP Value 6\tRSRQ Value 6\
            \tTx Beam Index 7\tRSRP Value 7\tRSRQ Value 7\
            \tTx Beam Index 8\tRSRP Value 8\tRSRQ Value 8\tbest_1sec\n")


f.close()
f = open('./Output/0xB173  LTE PDSCH Stat Indication.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tgeohash\tSubframe Num\tFrame Num\tNum Layers\
            \tNum Transport Blocks Present\tServing Cell Index\tHARQ ID\tRV\tNDI\
            \tCRC Result\tRNTI Type\tTB Index\
            \tDiscarded reTx Present\tDiscarded ReTx\tDid Recombining\
            \tTB Size (bytes)\tMCS\tNum RBs\
            \tModulation Type\tACK/NACK Decision\tAlt_TBS_Index\tAlt_MCS_Enabled\tLTE_PCC_RSRP\tbest_1sec\tFile Name\n")
f.close()

f = open('./Output/0xB18F  LTE ML1 AdvRx IC Cell List.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tCarrier Index\tEarfcn\tSubFn\
            \tServing Cell ID\tServing DL Bandwidth\tServing Num Antennas\
            \tServing Filt RSRP (dB)\tServing RSRP SS Buffer\tServing Cell Type\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0xB8DD  NR5G LL1 FW Serving FTL.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tCell Id\tSSB Or TRS\tCarrier Index\tFTL SNR[0]\
            \tFTL SNR[1]\tFTL SNR[2]\tFTL SNR[3]\tbest_1sec\tFile name\n")
f.close()
f = open('./Output/0xB8A7  NR5G MAC CSF Report.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tSlot\tNumerology\tFrame\
            \tCarrier ID\tReport Type\tReport Quantity Bitmask\tCRI\tRI\tWB CQI\tbest_1sec\n")
f.close()
f = open('./Output/0xB959  NR5G ML1 RLM Stats.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tSystem_Frame_Number\tRLM_Sync_State\tIS_RLM_Filtered_BLER\
            \tOOS_RLM_Filtered_BLER\tbest_1sec\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages ENL2DL NR.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\t5gPHY\t5gMAC\t5gRLC\
            \t5gPDCP\tIPA\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages ENL2DL LT.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\t4gPHY\t4gMAC\t4gRLC\
            \t4gPDCP\tIPA\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages ENL2DL ENDC.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\t5gPHY\t5gMAC\t5gRLC\
            \t5gPDCP\t4gPHY\t4gMAC\t4gRLC\t4gPDCP\tIPA\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages ENL2UL NR.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tPHY\tMACpad\tL2UL\
            \tIPA\tL2buffDelay\tavgRLCrtt\tWM\ttxWin\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages ENL2UL LT.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tPHY\tMACpad\tL2UL\
            \tIPA\tL2buffDelay\tavgRLCrtt\tWM\ttxWin\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages ENL2UL ENDC.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\t5gPHY\t5gMAC\t5gL2UL\t5gIPA\
            \t4gPHY\t4gMAC\t4gL2UL\t4gIPA\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages NR5GMAC DL.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tAvgPHY\tBLER\tCRCpass/fail\
            \tAvgTB\tAvgMCS\tAvgRB\tHARQ fail/recovery/redundant\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0x1FE8  QTrace Messages NR5GMAC UL.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tAvgPHY\tBLER\tCRCfail\
            \tTXcnt\tAvgTB\tAvgMCS\tAvgRB\tAvgLayers*10\tAvgRank*10\tAvgPHRidx\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0xB888  NR5G MAC PDSCH Stats.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
            \tTime_Stamp\tLongitude\tLatitude\tNum CA\tCarrier ID\tNum Slots\tNum PDSCH Decode\
            \tNum CRC Pass TB\tNum CRC Fail TB\tNum ReTx\tACK As NACK\tHARQ Failure\tCRC Pass TB Bytes\
            \tCRC Fail TB Bytes\tTB Bytes\tPadding Bytes\tReTx Bytes\tBLER\tbest_1sec\tFile Name\n")
f.close()
f = open('./Output/0xB16B  LTE PDCCH-PHICH Indication Report.txt',"w")
f.write("unixtimestamp_1sec\tunixtimestamp_100msec\tunixtimestamp_10msec\tunixtimestamp\
                \tTime_Stamp\tLongitude\tLatitude\tNum PDCCH Results\tNum PHICH Results\tPDCCH Timing SFN\tPDCCH Timing Sub-fn\
                \tForce Send PDCCH Ind\tPHICH Cell Index\tPHICH Present\tPHICH Value\tPHICH 1 Value\tPDCCH Serv Cell Index\
                \tRNTI Type\tPDCCH Payload Size\tAggregation Level\tSearch Space\tSPS Grant Type\tNew DL Tx\tNum DL Trblks\
                \tFake Pdcch Sf\tIs Ul Dropped\tMsleep\tUsleep\tuSleep Duration\tInterf Active\tS0 Index\tS1 Index\tS2 Index\
                \tS3 Index\tFull Mode Events Mask\tDl Subframe Count\tbest_1sec\tbest_1sec\tFile Name\n")
f.close()

for name in os.listdir('./'):
    if name.endswith(".txt"):
        txt = open(name,encoding="cp437", errors='ignore')
        print("pre-processing File : ",name, " Count : ", count)
        best_thp=0
        temp=txt.readline()
        while len(temp) > 0 :
            if temp.find("0x1FE8  QTrace Messages") > 0 :
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                var=txt.readline()
                if var.find("ENL2DL   | NR | DL since last") > 0 :
                    dic=var.split("|")
                    t_5gPHY=dic[4]
                    dic=t_5gPHY.split(" ")
                    if (int(dic[1]) > best_thp):
                        best_thp=int(dic[1])
                        best_thp_timestamp_1sec=unixtimestamp_1sec
            temp=txt.readline()
        txt.close()
        txt = open(name,encoding="cp437", errors='ignore')
        print("processing File : ",name, " Count : ", count)
        count=count+1
        Longitude=''
        Latitude=''
        eventtime=''
        eventtime_ul=''
        Num_SlotsL={}
        Num_SlotsL['0']='0'
        Num_PDSCHL={}
        Num_PDSCHL['0']='0'
        Num_CRC_Pass_TBL={}
        Num_CRC_Pass_TBL['0']='0'
        Num_CRC_Fail_TBL={}
        Num_CRC_Fail_TBL['0']='0'
        Num_ReTxL={}
        Num_ReTxL['0']='0'
        ACK_As_NACKL={}
        ACK_As_NACKL['0']='0'
        HARQ_FailureL={}
        HARQ_FailureL['0']='0'
        CRC_Pass_TB_BytesL={}
        CRC_Pass_TB_BytesL['0']='0'
        CRC_Fail_TB_BytesL={}
        CRC_Fail_TB_BytesL['0']='0'
        TB_BytesL={}
        TB_BytesL['0']='0'
        Padding_BytesL={}
        Padding_BytesL['0']='0'
        ReTx_BytesL={}
        ReTx_BytesL['0']='0'
        temp=txt.readline()
        while len(temp) > 0 :
            if temp.find("0xB16B  LTE PDCCH-PHICH Indication Report") > 0:
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(11):
                    txt.readline()
                var=txt.readline()
                while var != '\n' :
                    if len(var) > 0 :
                        if(var[4:7].strip()!=""):
                            Num_PDCCH_Results=var[8:15].strip()
                            Num_PHICH_Results=var[16:23].strip()
                            PDCCH_Timing_SFN=var[24:30].strip()
                            PDCCH_Timing_Sub_fn=var[31:37].strip()
                            Force_Send_PDCCH_Ind=var[38:43].strip()
                            Full_Mode_Events_Mask=var[210:222].strip()
                            Dl_Subframe_Count=var[223:231].strip()
                        PHICH_Cell_Index=var[44:49].strip()
                        PHICH_Present=var[50:57].strip()
                        PHICH_Value=var[58:63].strip()
                        PHICH_1_Value=var[64:69].strip()
                        PDCCH_Serv_Cell_Index=var[70:75].strip()
                        RNTI_Type=var[76:90].strip()
                        PDCCH_Payload_Size=var[91:98].strip()
                        Aggregation_Level=var[99:110].strip()
                        Search_Space=var[111:117].strip()
                        SPS_Grant_Type=var[118:128].strip()
                        New_DL_Tx=var[129:134].strip()
                        Num_DL_Trblks=var[135:141].strip()
                        Fake_Pdcch_Sf=var[142:147].strip()
                        Is_Ul_Dropped=var[148:155].strip()
                        Msleep=var[156:162].strip()
                        Usleep=var[163:169].strip()
                        uSleep_Duration=var[170:178].strip()
                        Interf_Active=var[179:185].strip()
                        S0_Index=var[186:191].strip()
                        S1_Index=var[192:197].strip()
                        S2_Index=var[198:203].strip()
                        S3_Index=var[204:209].strip()
                        f = open('./Output/0xB16B  LTE PDCCH-PHICH Indication Report.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                        +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+Num_PDCCH_Results+"\t"+Num_PHICH_Results+"\t"+PDCCH_Timing_SFN\
                        +"\t"+PDCCH_Timing_Sub_fn+"\t"+Force_Send_PDCCH_Ind+"\t"+PHICH_Cell_Index+"\t"+PHICH_Present+"\t"+PHICH_Value+"\t"+PHICH_1_Value\
                        +"\t"+PDCCH_Serv_Cell_Index+"\t"+RNTI_Type+"\t"+PDCCH_Payload_Size+"\t"+Aggregation_Level+"\t"+Search_Space+"\t"+SPS_Grant_Type\
                        +"\t"+New_DL_Tx+"\t"+Num_DL_Trblks+"\t"+Fake_Pdcch_Sf+"\t"+Is_Ul_Dropped+"\t"+Msleep+"\t"+Usleep\
                        +"\t"+uSleep_Duration+"\t"+Interf_Active+"\t"+S0_Index+"\t"+S1_Index+"\t"+S2_Index+"\t"+S3_Index\
                        +"\t"+Full_Mode_Events_Mask+"\t"+Dl_Subframe_Count+"\t"+best_1sec+"\t"+name+"\n")        
                        f.close()
                    var=txt.readline()
            if temp.find("0xB888  NR5G MAC PDSCH Stats") > 0:
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(6):
                    txt.readline()
                var=txt.readline()
                if (var[0:6] == "Num CA"):
                    Num_CA=var[28:31].strip()
                else:
                    for n in range(2):
                        var=txt.readline()
                    if(var[0:6] == "Num CA"):
                        Num_CA=var[28:31].strip()
                    else:
                        for n in range(2):
                            var=txt.readline()
                        if(var[0:6] == "Num CA"):
                            Num_CA=var[28:31].strip()
                for n in range(5):
                    txt.readline()
                var=txt.readline()
                if len(var)>0:
                    Carrier_ID=var[5:15].strip()
                    Num_SlotsL['1']=var[16:26].strip()
                    if (Num_SlotsL['0'] != '0'):
                        Num_Slots=str(int(Num_SlotsL['1'])-int(Num_SlotsL['0']))
                        Num_SlotsL['0']=Num_SlotsL['1']
                    else:
                        Num_Slots=str(int(Num_SlotsL['1']))
                    Num_PDSCHL['1']=var[27:37].strip()
                    if (Num_PDSCHL['0'] != '0'):
                        Num_PDSCH=str(int(Num_PDSCHL['1'])-int(Num_PDSCHL['0']))
                        Num_PDSCHL['0']=Num_PDSCHL['1']
                    else:
                        Num_PDSCH=str(int(Num_PDSCHL['1']))
                    Num_CRC_Pass_TBL['1']=var[38:48].strip()
                    if (Num_CRC_Pass_TBL['0'] != '0'):
                        Num_CRC_Pass_TB=str(int(Num_CRC_Pass_TBL['1'])-int(Num_CRC_Pass_TBL['0']))
                        Num_CRC_Pass_TBL['0']=Num_CRC_Pass_TBL['1']
                    else:
                        Num_CRC_Pass_TB=str(int(Num_CRC_Pass_TBL['1']))
                    Num_CRC_Fail_TBL['1']=var[49:59].strip()
                    if (Num_CRC_Fail_TBL['0'] != '0'):
                        Num_CRC_Fail_TB=str(int(Num_CRC_Fail_TBL['1'])-int(Num_CRC_Fail_TBL['0']))
                        Num_CRC_Fail_TBL['0']=Num_CRC_Fail_TBL['1']
                    else:
                        Num_CRC_Fail_TB=str(int(Num_CRC_Fail_TBL['1']))
                    Num_ReTxL['1']=var[60:70].strip()
                    if (Num_ReTxL['0'] != '0'):
                        Num_ReTx=str(int(Num_ReTxL['1'])-int(Num_ReTxL['0']))
                        Num_ReTxL['0']=Num_ReTxL['1']
                    else:
                        Num_ReTx=str(int(Num_ReTxL['1']))
                    ACK_As_NACKL['1']=var[71:81].strip()
                    if (ACK_As_NACKL['0'] != '0'):
                        ACK_As_NACK=str(int(ACK_As_NACKL['1'])-int(ACK_As_NACKL['0']))
                        ACK_As_NACKL['0']=ACK_As_NACKL['1']
                    else:
                        ACK_As_NACK=str(int(ACK_As_NACKL['1']))
                    HARQ_FailureL['1']=var[82:92].strip()
                    if (HARQ_FailureL['0'] != '0'):
                        HARQ_Failure=str(int(HARQ_FailureL['1'])-int(HARQ_FailureL['0']))
                        HARQ_FailureL['0']=HARQ_FailureL['1']
                    else:
                        HARQ_Failure=str(int(HARQ_FailureL['1']))
                    CRC_Pass_TB_BytesL['1']=var[93:113].strip()
                    if (CRC_Pass_TB_BytesL['0'] != '0'):
                        CRC_Pass_TB_Bytes=str(int(CRC_Pass_TB_BytesL['1'])-int(CRC_Pass_TB_BytesL['0']))
                        CRC_Pass_TB_BytesL['0']=CRC_Pass_TB_BytesL['1']
                    else:
                        CRC_Pass_TB_Bytes=str(int(CRC_Pass_TB_BytesL['1']))
                    CRC_Fail_TB_BytesL['1']=var[114:134].strip()
                    if (CRC_Fail_TB_BytesL['0'] != '0'):
                        CRC_Fail_TB_Bytes=str(int(CRC_Fail_TB_BytesL['1'])-int(CRC_Fail_TB_BytesL['0']))
                        CRC_Fail_TB_BytesL['0']=CRC_Fail_TB_BytesL['1']
                    else:
                        CRC_Fail_TB_Bytes=str(int(CRC_Fail_TB_BytesL['1']))
                    TB_BytesL['1']=var[135:155].strip()
                    if (TB_BytesL['0'] != '0'):
                        TB_Bytes=str(int(TB_BytesL['1'])-int(TB_BytesL['0']))
                        TB_BytesL['0']=TB_BytesL['1']
                    else:
                        TB_Bytes=str(int(TB_BytesL['1']))
                    Padding_BytesL['1']=var[156:176].strip()
                    if (Padding_BytesL['0'] != '0'):
                        Padding_Bytes=str(int(Padding_BytesL['1'])-int(Padding_BytesL['0']))
                        Padding_BytesL['0']=Padding_BytesL['1']
                    else:
                        Padding_Bytes=str(int(Padding_BytesL['1']))
                    ReTx_BytesL['1']=var[177:197].strip()
                    if (ReTx_BytesL['0'] != '0'):
                        ReTx_Bytes=str(int(ReTx_BytesL['1'])-int(ReTx_BytesL['0']))
                        ReTx_BytesL['0']=ReTx_BytesL['1']
                    else:
                        ReTx_Bytes=str(int(ReTx_BytesL['1']))
                    BLER=var[198:208].strip()
                    if (Num_SlotsL['0'] != '0'):
                        f = open('./Output/0xB888  NR5G MAC PDSCH Stats.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                            +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+Num_CA+"\t"+Carrier_ID+"\t"+Num_Slots+"\t"+Num_PDSCH+"\t"+Num_CRC_Pass_TB\
                            +"\t"+Num_CRC_Fail_TB+"\t"+Num_ReTx+"\t"+ACK_As_NACK+"\t"+HARQ_Failure+"\t"+CRC_Pass_TB_Bytes+"\t"+CRC_Fail_TB_Bytes\
                            +"\t"+TB_Bytes+"\t"+Padding_Bytes+"\t"+ReTx_Bytes+"\t"+BLER+"\t"+best_1sec+"\t"+name+"\n")     
                        f.close()
                    else:
                        Num_SlotsL['0']=Num_SlotsL['1']
                        Num_PDSCHL['0']=Num_PDSCHL['1']
                        Num_CRC_Pass_TBL['0']=Num_CRC_Pass_TBL['1']
                        Num_CRC_Fail_TBL['0']=Num_CRC_Fail_TBL['1']
                        Num_ReTxL['0']=Num_ReTxL['1']
                        ACK_As_NACKL['0']=ACK_As_NACKL['1']
                        HARQ_FailureL['0']=HARQ_FailureL['1']
                        CRC_Pass_TB_BytesL['0']=CRC_Pass_TB_BytesL['1']
                        CRC_Fail_TB_BytesL['0']=CRC_Fail_TB_BytesL['1']
                        TB_BytesL['0']=TB_BytesL['1']
                        Padding_BytesL['0']=Padding_BytesL['1']
                        ReTx_BytesL['0']=ReTx_BytesL['1']
            if temp.find("0x1FE8  QTrace Messages") > 0 :
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                var=txt.readline()
                if var.find("ENL2DL   | NR | DL since last") > 0 :
                    dic=var.split("|")
                    t_5gPHY=dic[4]
                    t_5gMAC=dic[6]
                    t_5gRLC=dic[8]
                    t_5gPDCP=dic[10]
                    IPA=dic[12]
                    f = open('./Output/0x1FE8  QTrace Messages ENL2DL NR.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_5gPHY+"\t"+t_5gMAC\
                    +"\t"+t_5gRLC+"\t"+t_5gPDCP\
                    +"\t"+IPA+"\t"+best_1sec+"\t"+name+"\n")        
                    f.close()
                    if unixtimestamp == eventtime :
                        f = open('./Output/0x1FE8  QTrace Messages ENL2DL ENDC.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                        +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_5gPHY+"\t"+t_5gMAC\
                        +"\t"+t_5gRLC+"\t"+t_5gPDCP+"\t"+t_4gPHY+"\t"+t_4gMAC+"\t"+t_4gRLC+"\t"+t_4gPDCP\
                        +"\t"+IPA+"\t"+best_1sec+"\t"+name+"\n")        
                        f.close()
                    eventtime = unixtimestamp
                if var.find("ENL2DL   | LT | DL since last") > 0 :
                    dic=var.split("|")
                    t_4gPHY=dic[4]
                    t_4gMAC=dic[6]
                    t_4gRLC=dic[8]
                    t_4gPDCP=dic[10]
                    IPA=dic[12]
                    f = open('./Output/0x1FE8  QTrace Messages ENL2DL LT.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_4gPHY+"\t"+t_4gMAC\
                    +"\t"+t_4gRLC+"\t"+t_4gPDCP\
                    +"\t"+IPA+"\t"+best_1sec+"\t"+name+"\n")        
                    f.close()
                    if unixtimestamp == eventtime :
                        f = open('./Output/0x1FE8  QTrace Messages ENL2DL ENDC.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                        +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_5gPHY+"\t"+t_5gMAC\
                        +"\t"+t_5gRLC+"\t"+t_5gPDCP+"\t"+t_4gPHY+"\t"+t_4gMAC+"\t"+t_4gRLC+"\t"+t_4gPDCP\
                        +"\t"+IPA+"\t"+best_1sec+"\t"+name+"\n")        
                        f.close()
                    eventtime = unixtimestamp
                if var.find("ENL2UL   | NR | UL since last") > 0 :
                    dic=var.split("|")
                    t_5gPHY=dic[10]
                    t_5gMACpad=dic[8]
                    t_5gL2UL=dic[6]
                    t_5gIPA=dic[4]
                    L2buffDelay=dic[11]
                    avgRLCrtt=dic[12]
                    WM=dic[13]
                    txWin=dic[14]
                    f = open('./Output/0x1FE8  QTrace Messages ENL2UL NR.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_5gPHY+"\t"+t_5gMACpad\
                    +"\t"+t_5gL2UL+"\t"+t_5gIPA+"\t"+L2buffDelay+"\t"+avgRLCrtt+"\t"+WM+"\t"+txWin+"\t"+best_1sec+"\t"+name+"\n")     
                    f.close()
                    if unixtimestamp == eventtime_ul :
                        f = open('./Output/0x1FE8  QTrace Messages ENL2UL ENDC.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                        +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_5gPHY+"\t"+t_5gMACpad\
                        +"\t"+t_5gL2UL+"\t"+t_5gIPA+"\t"+t_4gPHY+"\t"+t_4gMACpad+"\t"+t_4gL2UL+"\t"+t_4gIPA+"\t"+best_1sec+"\t"+name+"\n")        
                        f.close()
                    eventtime_ul = unixtimestamp
                if var.find("ENL2UL   | LT | UL since last |IPA") > 0 :
                    dic=var.split("|")
                    t_4gPHY=dic[10]
                    t_4gMACpad=dic[8]
                    t_4gL2UL=dic[6]
                    t_4gIPA=dic[4]
                    L2buffDelay=dic[11]
                    avgRLCrtt=dic[12]
                    WM=dic[13]
                    txWin=dic[14]
                    f = open('./Output/0x1FE8  QTrace Messages ENL2UL LT.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_4gPHY+"\t"+t_4gMACpad\
                    +"\t"+t_4gL2UL+"\t"+t_4gIPA+"\t"+L2buffDelay+"\t"+avgRLCrtt+"\t"+WM+"\t"+txWin+"\t"+best_1sec+"\t"+name+"\n")     
                    f.close()
                    if unixtimestamp == eventtime_ul :
                        f = open('./Output/0x1FE8  QTrace Messages ENL2UL ENDC.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                        +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+t_5gPHY+"\t"+t_5gMACpad\
                        +"\t"+t_5gL2UL+"\t"+t_5gIPA+"\t"+t_4gPHY+"\t"+t_4gMACpad+"\t"+t_4gL2UL+"\t"+t_4gIPA+"\t"+best_1sec+"\t"+name+"\n")        
                        f.close()
                    eventtime_ul = unixtimestamp
                if var.find("NR5GMAC  | DL since last | CA_ID:  0 | AvgPHY") > 0 :
                    dic=var.split("|")
                    AvgPHY=dic[3]
                    BLER=dic[4]
                    CRCpassfail=dic[5]
                    AvgTB=dic[6]
                    AvgMCS=dic[7]
                    AvgRB=dic[8]
                    HARQfailrecoveryredundant=dic[9]
                    f = open('./Output/0x1FE8  QTrace Messages NR5GMAC DL.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+AvgPHY+"\t"+BLER\
                    +"\t"+CRCpassfail+"\t"+AvgTB+"\t"+AvgMCS+"\t"+AvgRB+"\t"+HARQfailrecoveryredundant+"\t"+best_1sec+"\t"+name+"\n")
                    f.close()
                if var.find("NR5GMAC  | UL since last | CA_ID:  0 | AvgPHY") > 0 :
                    dic=var.split("|")
                    AvgPHY=dic[3]
                    BLER=dic[4]
                    CRCfail=dic[5]
                    TXcnt=dic[6]
                    AvgTB=dic[7]
                    AvgMCS=dic[8]
                    AvgRB=dic[9]
                    AvgLayers=dic[10]
                    AvgRank=dic[11]
                    AvgPHRidx=dic[12]
                    f = open('./Output/0x1FE8  QTrace Messages NR5GMAC UL.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+AvgPHY+"\t"+BLER\
                    +"\t"+CRCfail+"\t"+TXcnt+"\t"+AvgTB+"\t"+AvgMCS+"\t"+AvgRB+"\t"+AvgLayers+"\t"+AvgRank+"\t"+AvgPHRidx+"\t"+best_1sec+"\t"+name+"\n")
                    f.close()
            if temp.find("0xB8DD  NR5G LL1 FW Serving FTL") > 0:
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(3):
                    txt.readline()
                var=txt.readline()
                Cell_Id=var[32:37].strip()
                var=txt.readline()
                SSB_Or_TRS=var[32:37].strip()
                var=txt.readline()
                Carrier_Index=var[32:35].strip()
                txt.readline()
                var=txt.readline()
                FTL_SNR_0=var[35:42].strip()
                txt.readline()
                var=txt.readline()
                FTL_SNR_1=var[35:42].strip()
                txt.readline()
                var=txt.readline()
                FTL_SNR_2=var[35:42].strip()
                txt.readline()
                var=txt.readline()
                FTL_SNR_3=var[35:42].strip()
                if SSB_Or_TRS=='SSB' and Serving_SSB == '0':
                    Avg_SNR = FTL_SNR_0
                elif SSB_Or_TRS=='SSB' and Serving_SSB == '1':
                    Avg_SNR = FTL_SNR_1
                elif SSB_Or_TRS=='SSB' and Serving_SSB == '2':
                    Avg_SNR = FTL_SNR_2
                elif SSB_Or_TRS=='SSB' and Serving_SSB == '3':
                    Avg_SNR = FTL_SNR_3
                elif SSB_Or_TRS=='SSB':
                    Avg_SNR=FTL_SNR_0
                f = open('./Output/0xB8DD  NR5G LL1 FW Serving FTL.txt',"a")
                f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+Cell_Id+"\t"+SSB_Or_TRS\
                +"\t"+Carrier_Index+"\t"+FTL_SNR_0\
                +"\t"+FTL_SNR_1+"\t"+FTL_SNR_2\
                +"\t"+FTL_SNR_3+"\t"+best_1sec+"\t"+name+"\n")        
                f.close()
            if temp.find("0xB959  NR5G ML1 RLM Stats") > 0:
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(9):
                    txt.readline()
                var=txt.readline()
                while var != '\n' :
                    System_Frame_Number=var[19:25].strip()
                    RLM_Sync_State=var[8:18].strip()
                    IS_RLM_Filtered_BLER=var[26:38].strip()
                    OOS_RLM_Filtered_BLER=var[39:51].strip()
                    f = open('./Output/0xB959  NR5G ML1 RLM Stats.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                    +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+System_Frame_Number+"\t"+RLM_Sync_State\
                    +"\t"+IS_RLM_Filtered_BLER+"\t"+OOS_RLM_Filtered_BLER+"\t"+best_1sec+"\n")     
                    f.close()
                    var=txt.readline()
            if temp.find("0xB8A7  NR5G MAC CSF Report") > 0:
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(15):
                    txt.readline()
                var=txt.readline()
                Slot=var[8:12].strip()
                Numerology=var[13:23].strip()
                Frame=var[24:29].strip()
                Carrier_ID=var[42:49].strip()
                Report_Type=var[66:76].strip()
                Report_Quantity_Bitmask=var[77:97].strip()
                CRI=var[169:172].strip()
                RI=var[173:175].strip()
                WB_CQI=var[176:179].strip()
                f = open('./Output/0xB8A7  NR5G MAC CSF Report.txt',"a")
                f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+Slot+"\t"+Numerology\
                +"\t"+Frame+"\t"+Carrier_ID\
                +"\t"+Report_Type+"\t"+Report_Quantity_Bitmask\
                +"\t"+CRI+"\t"+RI+"\t"+WB_CQI+"\t"+best_1sec+"\n")        
                f.close()
            if temp.find("0xB18F  LTE ML1 AdvRx IC Cell List") > 0:
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(2):
                    txt.readline()
                var=txt.readline()
                Carrier_Index=var[32:37].strip()
                var=txt.readline()
                Earfcn=var[32:38].strip()
                for n in range(9):
                    txt.readline()
                var=txt.readline()
                SubFn=var[32:38].strip()
                for n in range(7):
                    txt.readline()
                var=txt.readline()
                Serving_Cell_ID=var[8:14].strip()
                Serving_DL_Bandwidth=var[15:24].strip()
                Serving_Num_Antennas=var[25:33].strip()
                Serving_Filt_RSRP=var[34:44].strip()
                Serving_RSRP_SS_Buffer=var[45:51].strip()
                Serving_Cell_Type=var[59:81].strip()
                if(Carrier_Index)=='PCC' :
                    LTE_PCC_RSRP=Serving_Filt_RSRP
                f = open('./Output/0xB18F  LTE ML1 AdvRx IC Cell List.txt',"a")
                f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+Carrier_Index+"\t"+Earfcn\
                +"\t"+SubFn+"\t"+Serving_Cell_ID\
                +"\t"+Serving_DL_Bandwidth+"\t"+Serving_Num_Antennas\
                +"\t"+Serving_Filt_RSRP+"\t"+Serving_RSRP_SS_Buffer+"\t"+Serving_Cell_Type+"\t"+best_1sec+"\t"+name+"\n")        
                f.close()
            if temp.find("0xB173  LTE PDSCH Stat Indication") > 0 :
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                j=1
                for n in range(10):
                    txt.readline()
                var=txt.readline()
                while var != '\n' :
                    if len(var) > 0 :
                        Num_Transport_Blocks_Present=var[34:43].strip()
                        if Num_Transport_Blocks_Present=='2':
                            Subframe_Num=var[8:16].strip()
                            Frame_Num=var[17:22].strip()
                            if j==1:
                                master_System_Frame_num=int(Frame_Num)
                            j=0    
                            time_difference=  (int(Frame_Num) - int(master_System_Frame_num))*10
                            var_timestamp = timestamp + datetime.timedelta(0,0,0,time_difference)
                            tti_timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
                            Num_Layers=var[27:33].strip()
                            Serving_Cell_Index=var[44:51].strip()
                            HARQ_ID=var[52:56].strip()
                            RV=var[57:59].strip()
                            NDI=var[60:63].strip()
                            CRC_Result=var[64:70].strip()
                            RNTI_Type=var[71:80].strip()
                            TB_Index=var[81:86].strip()
                            Discarded_reTx_Present=var[87:96].strip()
                            Discarded_ReTx=var[97:132].strip()
                            Did_Recombining=var[133:144].strip()
                            TB_Size=var[145:152].strip()
                            MCS=var[153:156].strip()
                            Num_RBs=var[157:160].strip()
                            Modulation_Type=var[161:171].strip()
                            ACK_NACK_Decision=var[172:180].strip()
                            Alt_TBS_Index=var[191:196].strip()
                            Alt_MCS_Enabled=var[197:204].strip()
                            f = open('./Output/0xB173  LTE PDSCH Stat Indication.txt',"a")
                            f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                            +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+geohash+"\t"+Subframe_Num+"\t"+Frame_Num\
                            +"\t"+Num_Layers+"\t"+Num_Transport_Blocks_Present\
                            +"\t"+Serving_Cell_Index+"\t"+HARQ_ID\
                            +"\t"+RV+"\t"+NDI+"\t"+CRC_Result\
                            +"\t"+RNTI_Type+"\t"+TB_Index\
                            +"\t"+Discarded_reTx_Present+"\t"+Discarded_ReTx+"\t"+Did_Recombining\
                            +"\t"+TB_Size+"\t"+MCS+"\t"+Num_RBs\
                            +"\t"+Modulation_Type+"\t"+ACK_NACK_Decision\
                            +"\t"+Alt_TBS_Index+"\t"+Alt_MCS_Enabled+"\t"+LTE_PCC_RSRP+"\t"+best_1sec+"\t"+name+"\n")   
                            f.close()
                            var=txt.readline()
                            HARQ_ID=var[52:56].strip()
                            RV=var[57:59].strip()
                            NDI=var[60:63].strip()
                            CRC_Result=var[64:70].strip()
                            RNTI_Type=var[71:80].strip()
                            TB_Index=var[81:86].strip()
                            Discarded_reTx_Present=var[87:96].strip()
                            Discarded_ReTx=var[97:132].strip()
                            Did_Recombining=var[133:144].strip()
                            TB_Size=var[145:152].strip()
                            MCS=var[153:156].strip()
                            Num_RBs=var[157:160].strip()
                            Modulation_Type=var[161:171].strip()
                            ACK_NACK_Decision=var[172:180].strip()
                            f = open('./Output/0xB173  LTE PDSCH Stat Indication.txt',"a")
                            f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                            +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+geohash+"\t"+Subframe_Num+"\t"+Frame_Num\
                            +"\t"+Num_Layers+"\t"+Num_Transport_Blocks_Present\
                            +"\t"+Serving_Cell_Index+"\t"+HARQ_ID\
                            +"\t"+RV+"\t"+NDI+"\t"+CRC_Result\
                            +"\t"+RNTI_Type+"\t"+TB_Index\
                            +"\t"+Discarded_reTx_Present+"\t"+Discarded_ReTx+"\t"+Did_Recombining\
                            +"\t"+TB_Size+"\t"+MCS+"\t"+Num_RBs\
                            +"\t"+Modulation_Type+"\t"+ACK_NACK_Decision\
                            +"\t"+Alt_TBS_Index+"\t"+Alt_MCS_Enabled+"\t"+LTE_PCC_RSRP+"\t"+best_1sec+"\t"+name+"\n")        
                            f.close()
                        elif Num_Transport_Blocks_Present=='1':
                            Subframe_Num=var[8:16].strip()
                            Frame_Num=var[17:22].strip()
                            if j==1:
                                master_System_Frame_num=int(Frame_Num)
                            j=0    
                            time_difference=  (int(Frame_Num) - int(master_System_Frame_num))*10
                            var_timestamp = timestamp + datetime.timedelta(0,0,0,time_difference)
                            tti_timestamp=var_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]   
                            Num_Layers=var[27:33].strip()
                            Serving_Cell_Index=var[44:51].strip()
                            HARQ_ID=var[52:56].strip()
                            RV=var[57:59].strip()
                            NDI=var[60:63].strip()
                            CRC_Result=var[64:70].strip()
                            RNTI_Type=var[71:80].strip()
                            TB_Index=var[81:86].strip()
                            Discarded_reTx_Present=var[87:96].strip()
                            Discarded_ReTx=var[97:132].strip()
                            Did_Recombining=var[133:144].strip()
                            TB_Size=var[145:152].strip()
                            MCS=var[153:156].strip()
                            Num_RBs=var[157:160].strip()
                            Modulation_Type=var[161:171].strip()
                            ACK_NACK_Decision=var[172:180].strip()
                            Alt_TBS_Index=var[191:196].strip()
                            Alt_MCS_Enabled=var[197:204].strip()
                            f = open('./Output/0xB173  LTE PDSCH Stat Indication.txt',"a")
                            f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                            +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+geohash+"\t"+Subframe_Num+"\t"+Frame_Num\
                            +"\t"+Num_Layers+"\t"+Num_Transport_Blocks_Present\
                            +"\t"+Serving_Cell_Index+"\t"+HARQ_ID\
                            +"\t"+RV+"\t"+NDI+"\t"+CRC_Result\
                            +"\t"+RNTI_Type+"\t"+TB_Index\
                            +"\t"+Discarded_reTx_Present+"\t"+Discarded_ReTx+"\t"+Did_Recombining\
                            +"\t"+TB_Size+"\t"+MCS+"\t"+Num_RBs\
                            +"\t"+Modulation_Type+"\t"+ACK_NACK_Decision\
                            +"\t"+Alt_TBS_Index+"\t"+Alt_MCS_Enabled+"\t"+LTE_PCC_RSRP+"\t"+best_1sec+"\t"+name+"\n")        
                            f.close()
                        var=txt.readline()
            if temp.find("0xB975  NR5G ML1 Serving Cell Beam Management") > 0 :
                Tx_Beam_Number_Index_0=''
                RSRP_Value_0=''
                RSRQ_Value_0=''
                Tx_Beam_Number_Index_1=''
                RSRP_Value_1=''
                RSRQ_Value_1=''
                Tx_Beam_Number_Index_2=''
                RSRP_Value_2=''
                RSRQ_Value_2=''
                Tx_Beam_Number_Index_3=''
                RSRP_Value_3=''
                RSRQ_Value_3=''
                Tx_Beam_Number_Index_4=''
                RSRP_Value_4=''
                RSRQ_Value_4=''
                Tx_Beam_Number_Index_5=''
                RSRP_Value_5=''
                RSRQ_Value_5=''
                Tx_Beam_Number_Index_6=''
                RSRP_Value_6=''
                RSRQ_Value_6=''
                Tx_Beam_Number_Index_7=''
                RSRP_Value_7=''
                RSRQ_Value_7=''
                Tx_Beam_Number_Index_8=''
                RSRP_Value_8=''
                RSRQ_Value_8=''
                Tx_Beam_Number_Index=['0','1','2','3','4','5','6','7','8']
                RSRP_Value=['','','','','','','','','']
                RSRQ_Value=['','','','','','','','','']
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                timestamp= timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(2):
                    txt.readline()
                var=txt.readline()
                if len(var) > 41:
                    PCI=var[37:41]
                else:
                    PCI=var[37:40]
                txt.readline()
                var=txt.readline()
                SSB_Periodicity_Serv_Cell=var[38:42]
                var=txt.readline()
                Serving_Beam_SSB_Index=var[38]
                var=txt.readline()
                BRSRP_Filtered=var[38:44]
                var=txt.readline()
                RSRQ_Filtered=var[41:44]
                var=txt.readline()
                Frequency_Offset=var[38:42]
                var=txt.readline()
                Time_Offset=var[38:39]
                var=txt.readline()
                Num_Detected_Beams=var[38]
                if int(Num_Detected_Beams) > 0:
                    for n in range(5):
                        txt.readline()
                    var=txt.readline()
                    while len(var) > 1:
                        Tx_Beam_Number_Index_temp=var[15]
                        RSRP_Value_temp=var[22:29]
                        RSRQ_Value_temp=var[36:42]
                        #new_SSB=1
                        for i in range(9):
                            if Tx_Beam_Number_Index_temp == Tx_Beam_Number_Index[i]:
                                RSRP_Value[i]=RSRP_Value_temp
                                RSRQ_Value[i]=RSRQ_Value_temp
                                #new_SSB = 0
                        #if new_SSB==1:
                        #        for i in range(9):
                         #       if Tx_Beam_Number_Index[i]==i:
                          #          Tx_Beam_Number_Index[i]=Tx_Beam_Number_Index_temp
                          #          RSRP_Value[i]=RSRP_Value_temp
                           #         RSRQ_Value[i]=RSRQ_Value_temp
                            #        break
                        var=txt.readline()
                    Tx_Beam_Number_Index_0=Tx_Beam_Number_Index[0]
                    RSRP_Value_0=RSRP_Value[0]
                    RSRQ_Value_0=RSRQ_Value[0]
                    Tx_Beam_Number_Index_1=Tx_Beam_Number_Index[1]
                    RSRP_Value_1=RSRP_Value[1]
                    RSRQ_Value_1=RSRQ_Value[1]
                    Tx_Beam_Number_Index_2=Tx_Beam_Number_Index[2]
                    RSRP_Value_2=RSRP_Value[2]
                    RSRQ_Value_2=RSRQ_Value[2]
                    Tx_Beam_Number_Index_3=Tx_Beam_Number_Index[3]
                    RSRP_Value_3=RSRP_Value[3]
                    RSRQ_Value_3=RSRQ_Value[3]
                    Tx_Beam_Number_Index_4=Tx_Beam_Number_Index[4]
                    RSRP_Value_4=RSRP_Value[4]
                    RSRQ_Value_4=RSRQ_Value[4]
                    Tx_Beam_Number_Index_5=Tx_Beam_Number_Index[5]
                    RSRP_Value_5=RSRP_Value[5]
                    RSRQ_Value_5=RSRQ_Value[5]
                    Tx_Beam_Number_Index_6=Tx_Beam_Number_Index[6]
                    RSRP_Value_6=RSRP_Value[6]
                    RSRQ_Value_6=RSRQ_Value[6]
                    Tx_Beam_Number_Index_7=Tx_Beam_Number_Index[7]
                    RSRP_Value_7=RSRP_Value[7]
                    RSRQ_Value_7=RSRQ_Value[7]
                    Tx_Beam_Number_Index_8=Tx_Beam_Number_Index[8]
                    RSRP_Value_8=RSRP_Value[8]
                    RSRQ_Value_8=RSRQ_Value[8]
                f = open('./Output/0xB975_NR5G_ML1_Serving_Cell_Beam_Management.txt',"a")
                f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                +"\t"+timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+PCI+"\t"+SSB_Periodicity_Serv_Cell\
                +"\t"+Serving_Beam_SSB_Index+"\t"+BRSRP_Filtered\
                +"\t"+RSRQ_Filtered+"\t"+Frequency_Offset\
                +"\t"+Time_Offset+"\t"+Num_Detected_Beams+"\t"+Tx_Beam_Number_Index_0\
                +"\t"+RSRP_Value_0+"\t"+RSRQ_Value_0\
                +"\t"+Tx_Beam_Number_Index_1+"\t"+RSRP_Value_1+"\t"+RSRQ_Value_1\
                +"\t"+Tx_Beam_Number_Index_2+"\t"+RSRP_Value_2+"\t"+RSRQ_Value_2\
                +"\t"+Tx_Beam_Number_Index_3+"\t"+RSRP_Value_3+"\t"+RSRQ_Value_3\
                +"\t"+Tx_Beam_Number_Index_4+"\t"+RSRP_Value_4+"\t"+RSRQ_Value_4\
                +"\t"+Tx_Beam_Number_Index_5+"\t"+RSRP_Value_5+"\t"+RSRQ_Value_5\
                +"\t"+Tx_Beam_Number_Index_6+"\t"+RSRP_Value_6+"\t"+RSRQ_Value_6
                +"\t"+Tx_Beam_Number_Index_7+"\t"+RSRP_Value_7+"\t"+RSRQ_Value_7
                +"\t"+Tx_Beam_Number_Index_8+"\t"+RSRP_Value_8+"\t"+RSRQ_Value_8+"\t"+best_1sec+"\n")           
                f.close()
            if temp.find("0xB97F  NR5G ML1 Searcher Measurement Database Update Ext") > 0 :
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                timestamp= timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(8):
                    txt.readline()
                var=txt.readline()
                Raster_ARFCN=var[40:48].strip()
                for n in range(2):
                    txt.readline()
                var=txt.readline()
                Serving_Cell_PCI=var[40:45].strip()
                var=txt.readline()
                Serving_SSB=var[40:43].strip()
                for n in range(17):
                    txt.readline()    
                var=txt.readline()
                while var != '\n' :
                    Detected_Beams_Num=var[57:60].strip()
                    if int(Detected_Beams_Num)> 0:
                        Detected_Beams_SSB_Index=var[61:66].strip()
                        Detected_Beams_RX_Beam_Info_RX_Beam_Id=var[67:74].strip()
                        Detected_Beams_RX_Beam_Info_RX_Beam_RSRP=var[75:90].strip()
                        Detected_Beams_NR2NR_Filtered_Tx_Beam_RSRP_L3=var[91:103].strip()
                        Detected_Beams_NR2NR_Filtered_Tx_Beam_RSRQ_L3=var[104:116].strip()
                        Detected_Beams_L2NR_Filtered_Tx_Beam_RSRP_L3=var[117:129].strip()
                        Detected_Beams_L2NR_Filtered_Tx_Beam_RSRQ_L3=var[130:142].strip()
                    else :
                        PCI=var[11:17].strip()
                        PBCH_SFN=var[18:24].strip()
                        NUM_Beams=var[25:30].strip()
                        Cell_Quality_RSRP=var[31:43].strip()
                        Cell_Quality_RSRQ=var[44:56].strip()
                        Detected_Beams_SSB_Index=var[61:66].strip()
                        Detected_Beams_RX_Beam_Info_RX_Beam_Id=var[67:74].strip()
                        Detected_Beams_RX_Beam_Info_RX_Beam_RSRP=var[75:90].strip()
                        Detected_Beams_NR2NR_Filtered_Tx_Beam_RSRP_L3=var[91:103].strip()
                        Detected_Beams_NR2NR_Filtered_Tx_Beam_RSRQ_L3=var[104:116].strip()
                        Detected_Beams_L2NR_Filtered_Tx_Beam_RSRP_L3=var[117:129].strip()
                        Detected_Beams_L2NR_Filtered_Tx_Beam_RSRQ_L3=var[130:142].strip()
                        if PCI == Serving_Cell_PCI:
                            Serving_Cell_Quality_RSRP=var[31:43].strip()
                            Serving_Cell_Quality_RSRQ=var[44:56].strip()
                    f = open('./Output/0xB97F_NR5G_ML1_Searcher_Measurement_Database_Update_Ext.txt',"a")
                    f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                        +"\t"+timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+Raster_ARFCN+"\t"+PCI+"\t"+PBCH_SFN+"\t"+NUM_Beams\
                        +"\t"+Cell_Quality_RSRP+"\t"+Cell_Quality_RSRQ+"\t"+Detected_Beams_Num\
                        +"\t"+Detected_Beams_SSB_Index+"\t"+Detected_Beams_RX_Beam_Info_RX_Beam_Id+"\t"+Detected_Beams_RX_Beam_Info_RX_Beam_RSRP\
                        +"\t"+Detected_Beams_NR2NR_Filtered_Tx_Beam_RSRP_L3+"\t"+Detected_Beams_NR2NR_Filtered_Tx_Beam_RSRQ_L3\
                        +"\t"+Detected_Beams_L2NR_Filtered_Tx_Beam_RSRP_L3+"\t"+Detected_Beams_L2NR_Filtered_Tx_Beam_RSRQ_L3+"\t"+best_1sec+"\n")
                    f.close()
                    txt.readline()
                    var=txt.readline()
            if temp.find("0x1FFB") > 0 :
                if temp.find("Reserved")== 0:
                    f = open('./Output/5G_Events.txt',"a")
                    text = "Latitude: " + Latitude + " Longitude : " + Longitude + " OTA: "+temp
                    f.write(text)
                    f.close()
            if temp.find("0xB821") > 0 :
                f = open('./Output/5G_Signaling.txt',"a")
                text = "Latitude: " + Latitude + " Longitude : " + Longitude + " OTA: "+temp
                f.write(text)
                f.close()
            if temp.find("0x1FEE  3D GPS Info")> 0 :
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                timestamp= timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(3):
                    txt.readline()
                var=txt.readline()
                Longitude = var[14:23]
                txt.readline()
                var=txt.readline()
                Latitude=var[13:21]
                geohash=geo.encode(float(Latitude),float(Longitude), precision=9)
            if temp.find("0xB887  NR5G MAC PDSCH Status")> 0 :
                year=int(temp[0:4])
                month_str=temp[5:8]
                month=int(datetime.datetime.strptime(month_str, '%b').month)
                day=int(temp[9:11])
                hour=int(temp[13:15])
                minute=int(temp[16:18])
                second=int(temp[19:21])
                milisecond=int(temp[22:25])
                microsecond=int(milisecond*1000)
                timestamp=datetime.datetime(year,month,day,hour,minute,second,microsecond)
                unixtimestamp_1sec=str(int(timestamp.timestamp()))
                unixtimestamp_100msec=str(int(timestamp.timestamp()*10))
                unixtimestamp_10msec=str(int(timestamp.timestamp()*100))
                unixtimestamp=str(int(timestamp.timestamp()*1000))
                best_1sec="No"
                if (unixtimestamp_1sec==best_thp_timestamp_1sec):
                    best_1sec="Yes"
                for n in range(3):
                    txt.readline()
                var=txt.readline()
                if var[0:2]=='ML' :
                    txt.readline()
                elif var[0:2]=='DL':
                    txt.readline()
                    txt.readline()
                    txt.readline()
                for n in range(10):
                    txt.readline()
                var=txt.readline()
                if var[1:10] == '  -------':
                    var=txt.readline()
                    j=1
                while var != '\n':
                    if len(var) > 0 :
                        System_Time_Slot=var[10:12]
                        System_Time_Numerology=var[18:23]
                        System_Time_Frame=var[26:29]
                        #frame_subframe=int(frame_num) *10 + int(subframe_num)
                        if j==1:
                            master_System_Time_Frame=System_Time_Frame
                            #    master_frame_num=frame_num
                            #    master_frame_subframe=int(master_frame_num) *10 + int(master_subframe_num)
                        j=0
                        #time_difference=  int(System_Time_Frame) - int(master_System_Time_Frame)
                        #var_timestamp = timestamp + datetime.timedelta(0,0,0,time_difference)
                        tti_timestamp= timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                        Num_PDSCH_Status= var[35]
                        Carrier_ID = var[32]
                        Tech_ID=var[48]
                        Conn_Id=var[60]
                        Bandwdith=var[69:71].strip()
                        Band_Type=var[75]
                        Physical_cell_ID=var[90:93].strip()
                        EARFCN=var[96:102]
                        TB_Index=var[107]
                        Num_Layers=var[159].strip()
                        TB_Size_Bytes=var[113:117].strip()
                        Total_bits=str(int(TB_Size_Bytes)*8*int(Num_Layers))
                        SCS_MU=var[120]
                        MCS=var[123:125].strip()
                        Num_Rbs=var[127:130].strip()
                        RV=var[132]
                        Harq_Id=var[138]
                        RNTI_Type=var[143]
                        CRC_State=var[175:179]
                        CRC_status=var[182:186]
                        New_Tx_Flag=var[190]
                        NDI=var[194]
                        Discard_Mode=var[202]
                        Num_ReTx=var[221]
                        Mod_Type=var[269:276].strip()
                        Num_RX=var[283:291].strip()
                        f = open('./Output/5G_Post_Processing_Full.txt',"a")
                        f.write(unixtimestamp_1sec+"\t"+unixtimestamp_100msec+"\t"+unixtimestamp_10msec+"\t"+unixtimestamp\
                                +"\t"+tti_timestamp+"\t"+Longitude+"\t"+Latitude+"\t"+geohash+"\t"+System_Time_Slot+"\t"+System_Time_Numerology+"\t"+System_Time_Frame\
                                +"\t"+Num_PDSCH_Status+"\t"+Carrier_ID+"\t"+Tech_ID\
                                +"\t"+Conn_Id+"\t"+RNTI_Type+"\t"+Harq_Id\
                                +"\t"+Band_Type+"\t"+Mod_Type+"\t"+TB_Size_Bytes+"\t"+Total_bits+"\t"+Physical_cell_ID\
                                +"\t"+Num_ReTx\
                                +"\t"+RV\
                                +"\t"+Discard_Mode\
                                +"\t"+MCS+"\t"+SCS_MU\
                                +"\t"+Num_Layers+"\t"+CRC_State\
                                +"\t"+CRC_status+"\t"+NDI+"\t"+Bandwdith\
                                +"\t"+New_Tx_Flag\
                                +"\t"+Num_Rbs+"\t"+EARFCN+"\t"+TB_Index+"\t"+Num_RX\
                                +"\t"+Serving_Cell_Quality_RSRP+"\t"+Serving_Cell_Quality_RSRQ+"\t"+Avg_SNR\
                                +"\t"+WB_CQI+"\t"+best_1sec+"\t"+name+"\n")
                        f.close()
                        var=txt.readline()
                    else:
                        breakpoint
            temp=txt.readline()
        txt.close()
        





    
        

    
