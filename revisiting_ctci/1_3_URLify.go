package main


import(
	"fmt"
	"strings"
)

// take the string and replace all spaces with %20
func URL(s string) string {
	return strings.Replace(s," ", "%20", -1 )
}


func main(){

	t1 := "this is the string"

	fmt.Printf("words: %v\n",  t1)
	fmt.Printf("url: %v\n", URL(t1) )

}