#a palindromic num is symmetric e.g. 343 or 3553
def check_palindromic_num(num):
	
	num = str(num)
	reverse_num = num[len(num)::-1]
	
	if num == reverse_num:
		return True 
	else:
		return False
