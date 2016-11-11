class Employee(object):
	def __init__(self, fname, lname, pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
		self.email=fname.lower()+"_"+lname.lower()+"@company.com"
	def full_name(self):
		#return self.fname+" "+self.lname
		return '{} {}'.format(self.fname, self.lname)


emp1=Employee("Joyce", "Inyanji", 30000)
emp2=Employee("Abraham", "Wanjila", 150000)

print(emp2.full_name())
print(emp1.full_name())