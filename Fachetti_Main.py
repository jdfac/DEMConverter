import multiprocessing
import os, sys
import re 
import DEM_converter 
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from Fachetti_Processor import main 

if __name__ == '__main__':
    
    # Initiate GUI
    app = QApplication(sys.argv)
    
    window = QWidget()
    ui = DEM_converter.Ui_Form()
    ui.setupUi(window)

    # Set up list of New England states to compare DEM states to. This can be edited to include more states, if necessary. 
    neStates = ['CT', 'MA', 'ME', 'NH', 'RI', 'VT']

    # Set up empty list to extract DEM years from folder
    years = []

    # Set up empty list to extract DEM states from folder
    states = []
   
    def selectDEMfolder():
        ''' Allow user to select folder containing DEMs. Loop through files in the folder to extract
            all possible years and states contained in the folder, add them to the GUI's combo boxes.
        ''' 
        folderName = QFileDialog.getExistingDirectory(window, "Select directory.") 
        if folderName:
            ui.DEMfolderLE.setText(folderName)
            for dem in os.listdir(folderName):
                year = re.search('.*(\d{4}).*(.tif)', dem).group(1)         # Search filenames for years and save them to the variable year.
                state = re.search('.*_([A-Z]{2,2})_.*(.tif)', dem).group(1) # Search filenames for states and save them to the variable state.
                if year not in years:                                       # Check to see if year is in years list, if not, add it. 
                    years.append(year)
                if state not in states and state in neStates:               # Check to see if state is in states list, if not, add it. 
                    states.append(state)
        years.sort() 
        states.sort()           
        ui.YearCB.addItems(years)                                           # Add years list to the GUI's year combo box. 
        ui.StateCB.addItems(states)                                         # Add states list to the GUI's state combo box. 
  
        
    def selectOutputFolder():
        ''' Allow user to select folder to store processed DEM layers.
        '''
        folderName = QFileDialog.getExistingDirectory(window, "Select directory.")
        if folderName:
            ui.OutputFolderLE.setText(folderName)


    def run():
        ''' Run the main function to perform file selection and file processing through multiprocessing. 
        '''
        # Set up try/except block to handle errors. 
        try:
            main(ui.DEMfolderLE.text(), ui.StateCB.currentText(), ui.YearCB.currentText(), ui.OutputFolderLE.text())
            success_message = QMessageBox()
            success_message.setText('Files created!')
            success_message.show()
            success_message.exec()
        except():
            error_message = QMessageBox()
            error_message.setText('No files created. Ensure that State has DEMs from year.')
            error_message.show()
            error_message.exec()


    # Connect GUI buttons to their accompanying functions. 
    ui.DEMFolderTB.clicked.connect(selectDEMfolder)
    ui.OutputFolderTB.clicked.connect(selectOutputFolder)
    ui.RunPB.clicked.connect(run)

    window.show()
    app.exec_()