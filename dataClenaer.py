"""
@description: Clean the crime, and property data so it can be used in
further analysis.

@author: Bengee
"""

import operator
import pandas as import pd
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
        df =  pd.read_xlsx(filename)
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
        dfDrop = df.drop(df.columns.differnce(cols), axis = 1,inplace = True)
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
    ops = {
        ">": operator.gt,
        ">=": operator.ge,
        "<": operator.lt,
        "<=": operator.le,
        "=": operator.eq,
        "!=": operator.ne
    }

    if removeRows == True:
        dfDrop =  df.drop(ops[opChar](df[col],value))
        logger.info("Succesfully dropped rows")
    else
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
        pd.to_csv(saveTo)
        logger.info("File saved")
    elif type == "excel":
        pd.to_excel(saveTo)
        logger.info("File saved")
    else:
        logger.error("Could not save file")
#===============================================================================

files = ["priceOfCrime.csv"]
badColumns = ["",""]
df = readFile(f)
df = dropColumns(df,columns,removeCols)
df = dropRows(df,column,value,operator,removeRows)
saveFile(df,path,filename,type)
