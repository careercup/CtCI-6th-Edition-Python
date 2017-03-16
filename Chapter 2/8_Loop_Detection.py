from LinkedList import LinkedList

class Solution(object):
	def detect_loop(self, ll) -> bool:
		"""
		get node at intersection of cycle
		"""
		
		slow, fast = ll.head, ll.head
		if fast and fast.next:
			fast = fast.next.next
		
		while fast and fast.next and slow is not fast:
			slow, fast = slow.next, fast.next.next

		if fast is None or fast.next is None:
			return None

		slow = ll.head
		fast = fast.next.next
		while fast is not slow:
			fast = fast.next
			slow = slow.next

		return fast


def main(): 
	print()
	s = Solution()
	tests = [
			(LinkedList(), None),
			((LinkedList((3,1,5,9,7,2,1))), None),
			 ]
	ll_a = LinkedList([3,1,5,9,7,2,1])
	ll_a.tail.next = ll_a.head.next.next
	
	tests.append( ((ll_a), 5) )
	for t in tests:
		input_, output = t
		
		# print(input_)
		ret = s.detect_loop(input_)
		# print(ret)
		if ret == output:
			# print(ret)
			print('PASS')
		else:
			print('FAIL')
			# print(input_)
			print('expected:')
			print(output)
			print('got:')
			print(ret)


if __name__ == '__main__':
	main()
