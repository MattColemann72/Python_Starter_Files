#I got carried away.. again..

#tax calculator
#Add income amount
#take away 12k
#find out 20%
#print tax

##TAX BANDS##
##£12,571 to £50,270    20%
##£50,271 to £150,000   40%
##over £150,000         45%

##tax free allowance is 0 for income over £125,140

incomeAmount = int(input("Please enter your yearly income: "))
taxFreeAllowance = 12570.00
noTaxFree = 125140.00

#######TAX BANDS#######
taxBand1Low = 12571.00
taxBand1High = 50270.00
taxBand2Low = 50271.00
taxBand2High = 150000.00

#######TAX CODES#######
taxCode1 = 0.20
taxCode2 = 0.40
taxCode3 = 0.45
taxfree = 0.00


def TaxCalculation(income):
    payableTax = 0
    if income > noTaxFree:
        taxFreeAllowance = 0.00
    else:
        taxFreeAllowance = 12570.00
    #if income <= taxfree:
        #payableTax = 0.00
    #else:
        ##taxableIncome = income - taxFreeAllowance
    if income >= taxBand1Low and income <= taxBand1High:
            taxableIncome = income - taxFreeAllowance
            payableTax = taxableIncome*taxCode1
            if taxableIncome <= 0:
                payableTax = 0
    elif income >= taxBand2Low and income <= taxBand2High:
            tb2TI = income - taxBand1High
            tb1TI = (income - tb2TI) - taxFreeAllowance
            taxpaidcode1 = tb1TI * taxCode1
            taxpaidcode2 = tb2TI * taxCode2
            payableTax = taxpaidcode1+taxpaidcode2
    elif income > taxBand2High:
            tb3TI = income - taxBand2High
            tb2TI = tb3TI - taxBand1High
            tb1TI = (tb3TI - tb2TI) - taxFreeAllowance
            taxpaidcode1 = tb1TI * taxCode1
            taxpaidcode2 = tb2TI * taxCode2
            taxpaidcode3 = tb3TI * taxCode3
            payableTax = taxpaidcode1+taxpaidcode2+taxpaidcode3

    print(f"You will pay £{payableTax} in tax this year.")

TaxCalculation(incomeAmount)