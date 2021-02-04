#In[]
import win32con
import win32print
import win32ui


def print2Printer():
        INCH = 1440

        hDC = win32ui.CreateDC ()
        hDC.CreatePrinterDC (win32print.GetDefaultPrinter ())
        hDC.StartDoc ("Test doc")
        hDC.StartPage ()
        hDC.SetMapMode (win32con.MM_TWIPS)
        hDC.DrawText ("",
                       (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
        hDC.EndPage ()
        hDC.EndDoc ()
 
print2Printer()
print("----------------")



# %%
