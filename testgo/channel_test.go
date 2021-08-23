package testgo

import(
	"fmt"
    "testing"
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

func TestChannel(t *testing.T) {
	Do(t, testCloseNilChannel)
	Do(t, testCloseChannelTwice)
}

func Do(t *testing.T, f func()error) {
	defer func(){
		if err := recover(); err != nil {
			t.Error(fmt.Printf("fail: panic, %v\n", err))
		}
	}()
	err := f()
	if err != nil {
		t.Error(fmt.Printf("fail: error, %v\n", err))
	}
	fmt.Println("ok")
}
