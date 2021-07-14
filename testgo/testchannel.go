package main

import(
	"fmt"
)

func testCloseNilChannel() error {
	//close nil chan
	var c chan int
	close(c)

	return nil
}

func testCloseChannelTwice() error {
	c := make(chan int)
	close(c)
	close(c)

	return nil
}

func main() {
	Do(testCloseNilChannel)
	Do(testCloseChannelTwice)
}

func Do(f func()error) {
	defer func(){
		if err := recover(); err != nil {
			fmt.Printf("fail: panic, %v\n", err)
		}
	}()
	err := f()
	if err != nil {
		fmt.Printf("fail: error, %v\n", err)
		return
	}
	fmt.Println("ok")
}
