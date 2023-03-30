netto = 1230
brutto = 1000

def ProcessInvoice(netto, brutto):
    if netto >= brutto:
        raise ValueError("Netto should be lower or equal to brutto")
    else:
        print("Processing invoice: netto={} brutto={}".format(netto,brutto))

try:
    ProcessInvoice(netto, brutto)
except ValueError as e:
    print("The vaules on invoice are incorrect: {}".format(e))
except Exception as e:
    print("Error processing invoice: {}".format(e))

