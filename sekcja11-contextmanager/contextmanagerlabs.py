

class HtmlCM:

    def __init__(self):
        pass
    def __enter__(self):
        print('<TABLE>\n <TR> \n <TH>number</TH><TH>Description</TH> \n <\TR>')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>')

with HtmlCM() as my_HtmlCM:
    print("<TR> \n<TD>1</TD><TD>Say hello!</TD></TR>")
    print("<TR> \n<TD>2</TD><TD>Say good bye!</TD></TR>")

'''

    def __init__(self):
        pass
    def __enter__(self):
        print('<TABLE>')
        print(' <TR> ')
        print("     <TH>number</TH><TH>Description</TH>")
        print(' <\TR> ')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>')

with HtmlCM() as my:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD>")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD>")
    print(" </TR>")

'''