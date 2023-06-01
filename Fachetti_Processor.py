import multiprocessing
import os, sys
import arcpy
import re 

arcpy.env.overwriteOutput = True

def get_install_path():
    ''' Return 64bit python install path from registry (if installed and registered),
        otherwise fall back to current 32bit process install path. Function borrowed from 
        Lesson 1 Assignment to ensure 64bit is being used. 
    '''
    if sys.maxsize > 2**32: return sys.exec_prefix #We're running in a 64bit process
  
    #We're 32 bit so see if there's a 64bit install
    path = r'SOFTWARE\Python\PythonCore\2.7'
  
    from _winreg import OpenKey, QueryValue
    from _winreg import HKEY_LOCAL_MACHINE, KEY_READ, KEY_WOW64_64KEY
  
    try:
        with OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_READ | KEY_WOW64_64KEY) as key:
            return QueryValue(key, "InstallPath").strip(os.sep) #We have a 64bit install, so return that.
    except: return sys.exec_prefix #No 64bit, so return 32bit path 


def worker(demFile, output):
    ''' Accept a single DEM file and and output folder as input and return a hillshade
        and slope raster file created from that DEM file. Save files to output folder
    '''
    # Set up a try/except block to handle errors. 
    try:
        demBase = os.path.basename(demFile)                             # Obtain the basename from the DEM file to name output files. 
        hillshade = arcpy.sa.Hillshade(demFile)                         # Create a hillshade layer from the DEM file. 
        hillshade.save(os.path.join(output, 'hillshade_' + demBase))    # Save hillshade layer to output folder. 
        slope = arcpy.sa.Slope(demFile)                                 # Create a slope layer form the DEM file. 
        slope.save(os.path.join(output, 'slope_'+ demBase))             # Save slope layer to output folder. 
        
    except:
        
        print('Processing failed.')


def main(DEMs, state, year, output):
    ''' Set up the regular expression match to only pull DEM files that match the criteria 
        supplied by the user. Set up multiprocessing and send jobs to the worker function 
        for execution.
    '''
    
    pattern = f'USGS.*{state}.*{year}.*(.tif)' # Use regular expressions combined with user input to only select 
                                               # files from the selected state and year.
                                               
    compiledRE = re.compile(pattern)           # Compile the pattern for matching. 
    
    multiprocessing.set_executable(os.path.join(get_install_path(), 'pythonw.exe')) # Make sure Python environment is used for running processes, even when this is run as a script tool

    cpuNum = multiprocessing.cpu_count()  # Determine number of cores to use. 
       
    jobs = []                               # Create empty jobs list to add selected DEM files. 
    for dem in os.listdir(DEMs): 
        
        demFile = os.path.join(DEMs, dem)   
        if compiledRE.match(dem):           # Check to see if the file name matches the pattern. 
            jobs.append((demFile, output))  # If matched, add a tuple containing the DEM filepath 
                                            # and the output folder to the jobs list. 
    
    with multiprocessing.Pool(processes=cpuNum) as pool: # Create the pool object. 
        pool.starmap(worker, jobs)  # Run jobs in job list. 



