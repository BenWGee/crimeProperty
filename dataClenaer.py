"""
@description: Clean the crime, and property data so it can be used in
further analysis.

@author: Bengee
"""

import operator
import pandas as pd
import sys, os, logging, datetime, time
from logging.handlers import RotatingFileHandler

# Path to project
path = ""
#Create name
name = "dataCleaner" #Project Name
#Create version
version = "0.0.0"
#Set Log dir location
log_dir = path + "logs/" #Path to logs file
#Create PID
pid = "pid="+str(os.getpid())+";"
#LOGGING
## Create Logger
logger = logging.getLogger(name)
##Set Default Logging Level
logger.setLevel(logging.DEBUG)
## Create Console Handler
ch = logging.StreamHandler()
## Set ch log level
ch.setLevel(logging.DEBUG)
## Create a rotating local log file handler
#fh = logging.handlers.RotatingFileHandler(name+".log", mode='a', maxBytes=4096, backupCount=0, encoding=None, delay=False, errors=None)
fh = logging.handlers.RotatingFileHandler(log_dir+name+".log", mode='a', maxBytes=4096, backupCount=0, encoding=None, delay=False)
## Set fh log level
fh.setLevel(logging.DEBUG)
## Logging format options
stdFormat = logging.Formatter('[%(asctime)s] '+pid+' level="%(levelname)s"; name="%(name)s"; message="%(message)s";', datefmt='%Y-%m-%dT%H:%M:%S')
debugFormat = logging.Formatter('[%(asctime)s] '+pid+' level="%(levelname)s"; name="%(name)s"; function="%(funcName)s"; line="%(lineno)d"; message="%(message)s";', datefmt='%Y-%m-%dT%H:%M:%S')
## Add formatting to handlers
ch.setFormatter(debugFormat)
fh.setFormatter(debugFormat)
##Add log handlers
logger.addHandler(ch)
logger.addHandler(fh)

# End of Logging boilerplate

logger.info(os.path.basename(__file__) + " stated")

#===============================================================================
def readFile(filename,extension):
    """
    @overview: Read in some file based on file extension.
    Return pandas dataframe.
    """
    if extension == "csv":
        logger.info("Succesfully read " + file)
        df =  pd.read_csv(filename)
    elif extension == "xlsx":
        df =  pd.read_excel(filename)
    else:
        logger.critical(filename + " cannot be read as it is of type " + extension)
        return
    return df
#===============================================================================

#===============================================================================
def dropColumns(df,cols,removeCols):
    """
    @overview: Drop unwanted columns from dataframe.
    Return pandas dataframe
    """
    if removeCols == True:
        dfDrop =  df.drop(cols, axis = 1)
    elif removeCols == False:
        dfDrop = df.filter(cols, axis=1)
    else:
        logger.error("Could not remove columns")
        return
    return dfDrop
#===============================================================================

#===============================================================================
def dropRows(df,col,value,opChar,removeRows):
    """
    @overview: Drop unwanted rows based on some condition.
    Return pandas dataframe
    """
    if removeRows == True:
        if opChar == ">":
            dfDrop =  df.drop(df[col] > value)
            logger.info("Succesfully dropped rows")
        elif opChar == "<":
            dfDrop =  df.drop(df[col] < value)
            logger.info("Succesfully dropped rows")
        elif opChar == "<":
            dfDrop =  df.drop(df[col] == value)
            logger.info("Succesfully dropped rows")
        else:
            logger.error("Could not drop rows")
    else:
        logger.error("Could not remove rows")
        return
    return dfDrop
#===============================================================================

#===============================================================================
def saveFile(df,saveTo,type):
    """
    @overview: Save modified dataframe to some location
    Return nothing
    """
    if type == "csv":
        df.to_csv(saveTo)
        logger.info("File saved")
    elif type == "excel":
        df.to_excel(saveTo)
        logger.info("File saved")
    else:
        logger.error("Could not save file")
#===============================================================================

file = "propertyData.xlsx"
badColumns = ["price","longitude","latitude"]
removeCols = False
removeRows = True
#compareCol = "Currency"
#value = "2019"
#operator = ">"
path = ""
filename = "propertyDataCondensed.csv"
type = "csv"

df = readFile(file,str(file.split(".")[1]))
#df = dropRows(df,compareCol,value,operator,removeRows)
df = dropColumns(df,badColumns,removeCols)
saveFile(df,filename,type)
