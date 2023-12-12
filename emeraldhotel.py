#Name: Christopher Miller
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else:
                subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(total)
            guest[i].append(occupancy)
            guest[i].append(grandtotal)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #455f98;background-image: url(emeraldbeach.jpg); color: #000000;">\n')
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr style="padding: 15px; text-align: center"><td>'
    td = '</td><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'

 #STUDENTS: INSERT ALL THE MISSING f.write STATEMENTS HERE
    
    f.write('\n<table border="3"   style ="background-color: #ffed9c;  font-family: arial; margin: auto; width: 60%;">\n')            
    f.write('<h1 style="text-align: center">Emerald Beach Hotel & Resort </h1></td></tr>')
    f.write('<h2 style="text-align: center">Sales Report Date/Time: ' + day_time + ' </h2></td></tr>'+ endtr)
    f.write(tr + 'Last'  + endtd +  'First'  + endtd +  'Num Nights'  + endtd + 'Subtotal'  + endtd +  'Sales Tax'  + endtd +  'Occ Tax'  + endtd +  'Total' + endtr)

    for i in range(len(guest)):
        f.write(tr + guest[i][0] + endtd + guest[i][1] + endtd + guest[i][3] + endtd +
                format(guest[i][4], currency) + endtd +
                format(guest[i][5], currency) + endtd +
                format(guest[i][6], currency) + endtd +
                format(guest[i][7], currency) + endtr)
    f.write('</table><br />')
    f.write('\n<table border="3"   style ="background-color: #fc6d6d;  font-family: arial; margin: auto; width: 60%;">\n')
    f.write('\n<center>')
    f.write('<td style="text-align: center; font-size: large;">' + "Grand Total:" + endtr)
    f.write ('<td style="text-align: center;">' + format(grandtotal, currency) + endtr)
    f.write('\n</center>')
    
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
