// SFTPS: Simple Fast TCP Port Scanner
// SFTPS IP START_PORT END_PORT
package main

import (
    "fmt"
    "net"
    "os"
    "strconv"
    "sync"
)

var openPorts []int
var ipAddr string

func checkPort(port int, wg *sync.WaitGroup) {
    defer wg.Done()

    conn, err := net.Dial("tcp", ipAddr+":"+strconv.Itoa(port))
    if err == nil {
        conn.Close()
        openPorts = append(openPorts, port)
    }
}

func main() {
    if len(os.Args) < 2 {
        fmt.Printf("Usage: %s IP\n", os.Args[0])
        os.Exit(1)
    }

    // increase file descriptors
    var rLimit syscall.Rlimit
    syscall.Getrlimit(syscall.RLIMIT_NOFILE, &rLimit)
    rLimit.Cur = 65535
    syscall.Setrlimit(syscall.RLIMIT_NOFILE, &rLimit)

    ipAddr = os.Args[1]

    var wg sync.WaitGroup
    for port := 1; port <= 65535; port++ {
        wg.Add(1)
        go checkPort(port, &wg)
    }

    wg.Wait()

    fmt.Println(openPorts)
}
