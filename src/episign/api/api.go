package main

import (
	"github.com/kataras/iris"
	"github.com/kataras/iris/mvc"
	"github.com/kataras/iris/middleware/logger"
	"github.com/kataras/iris/middleware/recover"

	//"encoding/json"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"io/ioutil"
	"time"

	"github.com/Jeffail/gabs"
)

func newApp() *iris.Application {
	app := iris.New()
	app.Use(recover.New())
	app.Use(logger.New())
	mvc.New(app).Handle(new(CoreController))
	return app
}

func main() {
	app := newApp()

	app.Run(iris.Addr(":9090"))
}

type CoreController struct{}



func (c *CoreController) GetDisplay() interface{} {
	planning := getPlanning()
	fmt.Println(planning)

	jsonParsed, err := gabs.ParseJSON([]byte(planning))

	children, _ := jsonParsed.S("").Children()
	for _, child := range children {
		fmt.Println(child.Data().(string))
	}

	jsonString, err := json.Marshal(map[string]map[int]string{"message": {1: "Kick-Off ObjDump", 2: "  14h - SM2", 3: "Projet Hub", 4: " 17h - U"}})
	if err != nil {
		fmt.Println(err)
	}
	return jsonString
}

func getPlanning() string {
	current := time.Now()
	response, err := http.Get("https://intra.epitech.eu/auth-7d3c35a078f73117aa5e6606fa25c727065e674a/planning/load?format=json&location=FR/MPL&semester=0,1,2,3,4,5,6&start=" + current.Format("2006-01-02") + "&end=" + current.Format("2006-01-02"))
	if err != nil {
		fmt.Printf("%s", err)
		os.Exit(1)
	}
	defer response.Body.Close()
	contents, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Printf("%s", err)
		os.Exit(1)
	}
	return string(contents)
}
