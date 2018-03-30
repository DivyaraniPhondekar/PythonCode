class Error(Exception):
	pass

class ValueTooSmallError(Error):
	pass

class ValueTooLargeError(Error):
	pass

def main():
	number=10
	try:
		inputnum=int(input("Please enter integer\n"))

		if inputnum < number:
			raise ValueTooSmallError
		if inputnum > number:
			raise ValueTooLargeError
		else:
			print ("Perfect")

	except ValueTooLargeError:
		print("The value is large")

	except ValueTooSmallError:
		print("The value is small")

	except Exception:
		print("Unexpected Error")


if __name__=="__main__":
	main()

