
def main():
		# סוגי טיפוסים בסיסיים:
		x_int = 5
		x_float = 3.4
		x_str  = "hi"
		
		print("Basic types:", x_int, type(x_int), x_float, type(x_float), x_str, type(x_str))
		
		# בפייתון סוג הטיפוס יכול להשתנות
		x = 5
		x = "a"

		# מבני נתונים
		# רשימה - אברי הרשימה יכולים להיות מטיפוסים שונים, כולל מבני נתונים
		l = [1, 2, 3]
		l2 = ["Hello", "World"]
		l3 = [1, "a", "2.4", [1,2]]
		#גישה לאיבר ברשימה:
		print("first cell in l:", l[0], ", third:", l[2], ", last cell of l2:", l2[-1])
		# השמה לתא ברשימה
		l[2] = 4
		print("Updated list:", l)
		
		# Tuple - דומה לרשימה, אך לא ניתן לעריכה
		t = (1, 2, 3)
		
		# t[2] = 4 # This line will cause an error
		
		# set - רשימה של איברים ייחודיים. לא ניתן לכתוב ולקרוא לפי מיקום
		s = (1,2,3,3,4)
		print("The actual set:", s)
		# s[1] # An error
		
		# Dictionary - מיפוי של זוגות מפתח:ערך
		d = {"key1": "value1", "key2": "value2", "key3": 3}
		print("Value of key1:", d["key1"])
		
		x = 5 + 2
		x = x * 3
		
		print("Math operations:", x)
		
		# \n - new line
		print("Ranges of values:\n", list(range(10)), "\n" , list(range(10, 20)), "\n" , list(range(10, 20, 2)), "\n" , list(range(10, 1, -1))) 

		# פונקציה יכולה לקבל מספר משתנים, או כלום.
		# הקוד של הפונק' נמצא בהזחה קבועה
		def foo(x):
				print(x / 2)
				return x * 2 # default return value is None
				
		print("foo:", foo(3))

		"""
		this is the way to write
		multiline comment
		"""
		
		# מעבר בלולאה על איברי רשימה
		print("l values:")
		for n in l:
				print(n)
		
		# הדפסת המספרים עד 12
		l = [1, 3, 5, 12, 9]

		i = 0
		# הלולאה תרוץ כל עוד התנאי יחזיר ערך אמת
		while (l[i] == 12):
				print(l[i])
				i = i + 1

		
		# דרך יותר פייתונית	
		for n in l:
				if n == 12:
						break
				print(n)
				
		# any - return true if at least one value is true		
		# all - return true if all values are true
		# if expect to recieve True/False. 0, "", [] etc. are consider as False. anything else is true.
		# elif/else are optional.
		if any([n > 100 for n in l]):
				print(2)
		elif all([n > 20 for n in l]):
				print(100)
		else:
				print(3)
				
# __name__ will be __main__ only when running this file directly			
if __name__ == '__main__':				
		main()