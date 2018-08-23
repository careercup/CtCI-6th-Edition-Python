package main

import (
	"fmt"
)

func IsRotation(a string, b string) bool {

	for i := 0; i < len(a); i++ {

		if a == b {
			return true
		}

		a = fmt.Sprintf("%v%v", string(a[len(a)-1]), a[:(len(a)-1)])

	}

	return false
}

func main() {

	fmt.Println("test and ttes are rotations:")
	fmt.Println(IsRotation("test", "ttes"))

	fmt.Println("test and sett are rotations:")
	fmt.Println(IsRotation("test", "sett"))

	fmt.Println("test and estt are rotations:")
	fmt.Println(IsRotation("test", "estt"))

	fmt.Println("test and golang are rotations:")
	fmt.Println(IsRotation("test", "golang"))

}
