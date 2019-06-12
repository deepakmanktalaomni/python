from ddt import ddt,data,unpack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import xlrd

def getData(filename):
    myrows = []
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    for i in range(1,sheet.nrows):
