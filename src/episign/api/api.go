package main

import (
	"github.com/kataras/iris"
	"github.com/kataras/iris/mvc"
	"github.com/kataras/iris/middleware/logger"
	"github.com/kataras/iris/middleware/recover"

	//"encoding/json"
	"encoding/json"
	"fmt"
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
	jsonString, err := json.Marshal(map[string]map[int]string{"message": {1: "Kick-Off Malloc", 2: "  14h - SM2", 3: "Projet Hub", 4: " 17h - U"}})
	if err != nil {
		fmt.Println(err)
	}
	return jsonString
}