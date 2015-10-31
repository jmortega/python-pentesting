# -*- encoding: utf-8 -*-
#class for obtain metadata info from pdf

import os

#pdf lib
from PyPDF2 import PdfFileReader, PdfFileWriter

class PDFMetaData:
    
    def printMetaData(self):
        for dirpath, dirnames, files in os.walk("pdfs"):
            try:
                for name in files:
                    ext = name.lower().rsplit('.', 1)[-1]
                    if ext in ['pdf']:
                        print "[+] Metadata for file: %s " %(dirpath+os.path.sep+name)
                        pdfFile = PdfFileReader(file(dirpath+os.path.sep+name, 'rb'))
                        docInfo = pdfFile.getDocumentInfo()
                        for metaItem in docInfo:
                            print '[+] ' + metaItem + ':' + docInfo[metaItem]
                        print "\n"
            except Exception,e:
                print "Error to Obtain PDF METADATA"
                pass