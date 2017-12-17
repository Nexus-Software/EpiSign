package main

import "github.com/kataras/iris"

func main() {
	app := iris.Default()

	app.RegisterView(iris.HTML("./views", ".html").Layout("layout.html"))

	// Method:   GET
	// Resource: http://localhost:8080/
	app.Handle("GET", "/", func(ctx iris.Context) {
		ctx.View("home.html")
	})

	// Set port
	app.Run(iris.Addr(":8080"))
}
