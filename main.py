from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
from datetime import date


def BrowseFilesPath(window):
    global filesPath
    temp = filedialog.askdirectory()
    LabelBox = Label(window, text=temp, font=("Arial", 11),padx=5).grid(row=0,column=3)
    filesPath = temp

def BrowseResultPath(window):
    global resultPath
    temp = filedialog.askdirectory()
    LabelBox = Label(window, text=temp, font=("Arial", 11),padx=5).grid(row=2,column=3)
    resultPath = temp

def Start(window,startString,endString):
    global filesPath
    global resultPath
    today = date.today().strftime("%d/%m/%Y")
    try:
        newgenHeader = f'''
         /***********************************************************************************
         * NEWGEN SOFTWARE TECHNOLOGIES LIMITED Group : {startString.get()}
         * Author                                     : {endString.get()}
         * Date Written (DD/MM/YYYY)                  : {today}
         * Description                                :
         * Date Modified (DD/MM/YYYY)                 :
         ************************************************************************************/
         '''
    except:
        newgenHeader = f'''
         /***********************************************************************************
         * NEWGEN SOFTWARE TECHNOLOGIES LIMITED Group :
         * Author                                     :
         * Date Written (DD/MM/YYYY)                  : {today}
         * Description                                :
         * Date Modified (DD/MM/YYYY)                 :
         ************************************************************************************/
         '''

    files = os.listdir(filesPath)
    MainFile = open(os.path.join(resultPath,'consolidate.sql' ), 'w+')
    for f in files:
        try:
            tempFile = open(os.path.join(filesPath, f),"r")
            MainFile.write(newgenHeader + "\n")
            # ---------
            list_LINES = tempFile.read()
            for line in list_LINES:
                MainFile.write(line)
            # ----------

        except Exception as e:
            MainFile.write(newgenHeader + "\n")
            MainFile.write(f"   -- file {f} can't be write Error Code : {e}\n")
        tempFile.close()
    MainFile.close()
    messagebox.showinfo("Message", "Process Completed")
    window.destroy()

def mainUI():
    window = Tk()
    window.title("SQL Consolidator")
    window.geometry("700x300")
    # all the ui components here
    pathLabel = Label(window, text="Select Path for files",padx=5,pady=10,font=("Helvetica", 14),width=30).grid(row=0,column=0)
    browseBtn = Button(window, text="Browse", command= lambda:BrowseFilesPath(window), bg="#3d3d3d", fg="#ffffff").grid(row=0,column=1)

    resultPathLabel = Label(window, text="Select Path to store result file",padx=5,pady=10,font=("Helvetica", 14),width=30).grid(row=2,column=0)
    resultPathBtn = Button(window, text="Browse", command= lambda:BrowseResultPath(window), bg="#3d3d3d", fg="#ffffff").grid(row=2,column=1)

    startLabel = Label(window, text="Group Name(optional)",padx=5,pady=10,font=("Helvetica", 14),width=30).grid(row=5,column=0)
    startString = Entry(window, width=35, borderwidth=5)
    startString.grid(row=5,column=1,columnspan=3,padx=5,pady=10)
    endLabel = Label(window, text="Author Name(optional)",padx=5,pady=10,font=("Helvetica", 14),width=30).grid(row=6,column=0)
    endString = Entry(window, width=35, borderwidth=5)
    endString.grid(row=6,column=1,columnspan=3,padx=5,pady=10)
    startBtn = Button(window, text="Start", command= lambda:Start(window,startString,endString), bg="#000000", fg="#ffffff").grid(row=7,column=0)
    # --------------------------------
    window.mainloop()


if __name__ == "__main__":
    filesPath = ""
    resultPath = ""
    mainUI()
