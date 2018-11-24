from numpy import array, shape

def find_element(arr,l1,l2,h1,h2,x):
  if l1 < h1 and l2 < h2:
    print(arr[l1:h1,l2:h2]) 
  # top right element
    if arr[l1,h2-1] == x: return True 
    if arr[l1,h2-1] > x: # give up last column
      return find_element(arr, l1, l2, h1, h2-1, x)
    if arr[l1,h2-1] < x: # give up first row
      return find_element(arr, l1+1, l2, h1, h2, x)
  # bottom left
    if arr[h1-1,l2] == x: return True
    if arr[h1-1,l2] > x: # give up last row
      return find_element(arr,l1+1,l2,h1,h2)
    if arr[h1-1,l2] < x: # give up first column
      return find_element(arr, l1, l2+1, h1, h2, x)
  return False
  
arr = array([[15,20,70,85],[20,35,80,95],[30,55,95,105],[40,80,100,120],[50,100,110,130]])
