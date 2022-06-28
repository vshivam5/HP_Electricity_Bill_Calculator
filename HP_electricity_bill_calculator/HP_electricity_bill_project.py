from datetime import date
from fpdf import FPDF

Fixed_charges = 70
pay_amount = 1
subsidy = 1
first_unit =1
num = 1
tax = 1
final =1
consumer_id = input("Enter the 13 Digit Valid Consumer Id Number:- ")
try:
    if len(consumer_id) == 13:
        unit = float(input("Enter the Unit Consumed:- "))
        if unit<=60:
            pay_amount = unit*3.50
            subsidy = unit*3.50
            final = float(Fixed_charges+(pay_amount-subsidy))
            tax  = (pay_amount*3)/100
            num = tax+final
        elif unit <=300:
            if unit>100:
                first_unit = 100
                second_unit = unit-100
                subsidy = (first_unit*2.30) + (second_unit*1.10)
                second_unit = second_unit*5.05
                first_unit = first_unit*4.15
                pay_amount = first_unit+second_unit
                tax = (pay_amount*3)/100
                final = (pay_amount-subsidy)+tax+Fixed_charges
            else:
                first_unit = unit
                subsidy = (first_unit*2.30)
                first_unit = first_unit*4.15
                pay_amount = first_unit
                tax = (pay_amount*3)/100
                final = (pay_amount-subsidy)+tax+Fixed_charges
        elif unit > 300:
            first_unit = 100
            second_unit = 200
            third_unit = 300 - unit
            subsidy = (first_unit*2.30) + (second_unit*1.10) + (third_unit*0.65)
            second_unit = second_unit*5.05
            first_unit = first_unit*4.15
            third_unit = third_unit*5.65
            pay_amount = first_unit+second_unit+third_unit
            tax = (pay_amount*3)/100
            final = (pay_amount-subsidy)+tax+Fixed_charges

    today = date.today()
    date = today.strftime("%d/%m/%Y")
    pdf = FPDF()
    pdf.add_page()
    pdf.image('logo.jpg',7,8,33)


    pdf.set_font("Courier", size = 16,style = 'B')
    pdf.cell(200, 15, txt = "Himachal Pradesh State Electricity Board",ln = 1, align = 'C')

    pdf.set_font("Courier", size = 13,style = 'B')
    pdf.cell(200, 10, txt = "DOMESTIC SUPPLY (DS)",ln = 1, align = 'C')


    pdf.set_font("Courier", size = 11,style = 'B')
    pdf.cell(200, 10, txt = "DATE:- "+str(date),ln = 1, align = 'C')

    pdf.set_font("Courier", size = 10,style="B")
    pdf.cell(190, 10, txt = "CONSUMER ID: "+str(consumer_id),ln = 1, align = 'L',border=1)

    pdf.set_font("Courier", size = 10,style="B")
    pdf.cell(190, 10, txt = "UNIT CONSUMED: "+str(unit),ln = 1, align = 'L',border=1)

    pdf.set_font("Courier", size = 10,style="B")
    pdf.cell(190, 10, txt = "AMOUNT "+str('%.2F'%pay_amount),ln = 1, align = 'L',border=1)

    pdf.set_font("Courier", size = 10,style="B")
    pdf.cell(190, 10, txt = "TAX DUTY: "+str(tax),ln = 1, align = 'L',border=1)

    pdf.set_font("Courier", size = 10,style="B")
    pdf.cell(190, 10, txt = "SUBSIDY: "+str('%.2f'%subsidy),ln = 1, align = 'L',border=1)

    pdf.set_font("Courier", size = 10,style="B")
    pdf.cell(190, 10, txt = "CURRENT BILL: "+str('%.2f'%final),ln = 1, align = 'L',border=1)

    pdf.output('Electricity Bill.pdf')
except:
    print("Invalid Consumer Id")
