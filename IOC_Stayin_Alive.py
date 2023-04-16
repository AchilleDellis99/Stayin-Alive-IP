import ping3
import openpyxl
from IOC_list import get_IOC

lista_IOC=get_IOC()

# apertura del file txt
with open('IOCs.txt') as file:
    ip_list = [line.strip() for line in file]

# creazione del file Excel
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'IP offline'

# verifica degli IP
print("")
print("         ^J5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5Y^")                                           
print("        !PPPP55PPPPPPPPPP55YYY5PPPPPPPP5YYY5PPPPPPPPPPPP!")                                           
print("       7PPP5^  ^5PPPPPY7^.     .~JPPJ~. .   .^YPPPPPPPP!")                                            
print("      ?PPPY:    7PPPY^  ^7JYYJ7^  J?  ^J55Y?~!5PPPPPPP!")                                 
print("     ?PPPY. :Y:  YPY. .JPPPPPPPPY5P7  :7?Y5PPPPPPPPP5~")                      
print("   .JPPPJ. ^5PJ..?P~  7PPPPPPPPPPPPPJ!^..  .~YPPPPP5^     Future at your")               
print("  .YPPP?  ^J!!!~~!Y!  ~PPPPPPPP5Y5PPPPPP5Y7  :5PPP5:      Side")            
print(" .YPPP7  ~P?^^^:  .Y~  :7JYYJ7^  ??^~?YYYJ~  ~PPPY:       @Achille Dellis") 
print(":YPPPY. ~PPPPPPP!..?PJ!:     .:!YP?^.  ....~JPPPJ.        ")
print("5PPPPP55PPPPPPPPP55PPPPP5YYY55PPPPPP55YYY5PPPPPJ.         ") 
print("!Y5555PP555555555PP5555PPPPPPP555555PPPPPPP555?.")   
for ip in ip_list:
    response_time = ping3.ping(ip)
    if response_time is not None:
        print(f'{ip} is online')
    else:
        print(f'{ip} is offline')
        worksheet.append([ip])

# salvataggio del file Excel
workbook.save('ip_offline.xlsx')
