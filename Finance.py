# ...P&L subfunctions...
def GrossProfit(Revenue, COGS):
    return Revenue - COGS

def OperProfit(GrossProfit, SnM, GnA, RnD):
    return GrossProfit - SnM - GnA - RnD

def EBITDA(OperProfit, OtherCosts, OtherProfits):
    return OperProfit - OtherCosts + OtherProfits

def NetIncome(EBITDA, DnA, Interests, Taxes):
    return EBITDA - DnA - Interests - Taxes
# ...end P&L subfunctions...

# ...CFS subfunctions...
# Operating activities (direct method)
def CashReceived(Revenue):
    return Revenue

def CashToMerchandise(COGS, ChangeAccReceivable, ChangeAccPayable, ChangeInventory):
    return COGS + ChangeAccReceivable + ChangeAccPayable + ChangeInventory

def OPEX(SnM, GnA, RnD, OtherCosts, OtherProfits):
    return SnM + GnA + RnD + OtherCosts - OtherProfits

def CashToInterest(Interests):
    return Interests

def CashToTaxes(Taxes):
    return Taxes

def TotalOperCashDir(CashReceived, CashToMerchandise, OPEX, CashToInterest, CashToTaxes):
    return CashReceived - CashToMerchandise - OPEX - CashToInterest - CashToTaxes

# Operating activities (indirect method)
def ChangeAccReceivable(AccReceivable_curr, AccReceivable_last):
    return AccReceivable_curr - AccReceivable_last

def ChangeAccPayable(AccPayable_curr, AccPayable_last):
    return AccPayable_curr - AccPayable_last

def ChangeInventory(Inventory_curr, Inventory_last):
    return Inventory_curr - Inventory_last

def TotalOperCashIndir(NetIncome, DnA, ChangeAccReceivable, ChangeAccPayable, ChangeInventory):
    return NetIncome + DnA - ChangeAccReceivable + ChangeAccPayable - ChangeInventory

# Investing activities
def CapEx(CapitalAssets_curr, CapitalAssets_last):
    return CapitalAssets_curr - CapitalAssets_last

def TotalInvCash(CapEx, Acquisitions):
    return - CapEx - Acquisitions

# Financing activities
def ChangeDebt(ShortDebts_curr, ShortDebts_last, TaxPayable_curr, TaxPayable_last, InterestPayable_curr, InterestPayable_last):
    return (ShortDebts_curr - ShortDebts_last) + (TaxPayable_curr - TaxPayable_last) + (InterestPayable_curr - InterestPayable_last)

def ChangeEquity(CapitalStock_curr, CapitalStock_last):
    return CapitalStock_curr - CapitalStock_last

def TotalFinCash(ChangeDebt, ChangeEquity, Dividends):
    return ChangeDebt + ChangeEquity - Dividends

# Result subfunctions
def TotalCash(TotalOperCash, TotalInvCash, TotalFinCash):
    return TotalOperCash + TotalInvCash + TotalFinCash

def OpenCash(CloseCash_last):
    return CloseCash_last

def CloseCash(TotalCash, OpenCash):
    return TotalCash + OpenCash

def CheckOperCash(TotalOperCashDir, TotalOperCashIndir):
    return TotalOperCashDir == TotalOperCashIndir
# ...end CFS subfunctions...

# ...Balance subfunctions...
# Assets
def Cash(CloseCash):
    return CloseCash

def TotalCurrAssets(Cash, AccReceivable, Inventory):
    return Cash + AccReceivable + Inventory

def TotalFixAssets(CapitalAssets, AccumDeprecioation):
    return CapitalAssets - AccumDeprecioation

def TotalAssets(TotalCurrAssets, TotalFixAssets):
    return TotalCurrAssets + TotalFixAssets

# Liabilities
def TotalCurrLiabilities(AccPayable, ShortDebts, TaxPayable, InterestPayable):
    return AccPayable + ShortDebts + TaxPayable + InterestPayable

def TotalLiabilities(TotalCurrLiabilities, LongLiabilities):
    return TotalCurrLiabilities + LongLiabilities

# Equities
def RetainedErnings(NetIncome, Dividends, RetainedErnings_last):
    return NetIncome - Dividends + RetainedErnings_last

def TotalEquities(CapitalStock, RetainedErnings):
    return CapitalStock + RetainedErnings

# Checking
def ChickBalance(TotalAssets, TotalLiabilities, TotalEquities):
    return TotalAssets == (TotalLiabilities + TotalEquities)
# ...end Balance subfunctioins...