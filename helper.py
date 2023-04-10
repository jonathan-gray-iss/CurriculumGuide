# csv_to_indiv_records
# proc_seniors_interim_q4
#
#
#
# tex file is   top, header, fill1, 
#                   quad1, fill2, 
#                   quad2, fill3, 
#                   quad3, fill4,
#                   quad4, fill5,
#                   bottom
#

from decimal import Decimal, ROUND_HALF_UP


def trim_sem(record):
    # Trim off -F, -S, - F, - S from old files
    # the record.dept != "MSON" is because an MSON class has a title with "- F" in it

    if record.dept != "MSON":
        s = record.course
        if "-F" in s:
    
            s = s[0:s.index("-F")]   
            record.course = s
        elif "- F" in s:
    
            s = s[0:s.index("- F")]   
            record.course = s
        elif "-S" in s:
    
            s = s[0:s.index("-S")]   
            record.course = s
        elif "- S" in s:
    
            s = s[0:s.index("- S")]   
            record.course = s  
    
    if "&" in record.course:
        if "\&" not in record.course:
            record.course = record.course.replace("&", "\&")
    if " and " in record.course:
        record.course = record.course.replace(" and ", " \& ")        
    if "Advanced" in record.course:
        record.course = record.course.replace("Advanced", "Adv")
    if "Pre-Calculus" in record.course:
        record.course = record.course.replace("Pre-Calculus", "Precalculus")        
    
    return record





class record():
    def __init__(self,line):
        self.first = line[0]
        self.last = line[1]           
        self.gradyr = int(line[2])
        self.ay = line[3]
        self.currgrade = line[4]    
        self.dept = line[5]
        self.course = line[6]
        self.grade = line[7]
        self.gradingpd = line[8]
        self.name = line[1]+", " + line[0]
        self.credit = line[10]
        self.gpacredit=line[10]
        #self.street = line[11]
        #self.city = line[12]
        #self.state = line[13]
        #self.zip = line[14]
        self.deptsort = None
        self.filename = line[1]+line[0]
    
    def __cmp__(self,other):
        return cmp(self.deptsort, other.deptsort)

class student():
    def __init__(self,name,their_records):
        self.name = name
        self.records=their_records
        
class address():        
    def __init__(self,name,street,city,state,zipcode,dob,enroll):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode
        self.dob = dob
        self.enroll = enroll
        
class full_record(object):        
    def __init__(self):
        self.name = ""
        self.g9 = []
        self.g10 = []
        self.g11 = []
        self.g12 = []
        self.g9gpa = 0.0
        self.g10gpa = 0.0
        self.g11gpa = 0.0
        self.cum10gpa =  0.0
        self.cum11gpa =  0.0
        
        self.street = ""
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""        
        
        self.spring = []




    