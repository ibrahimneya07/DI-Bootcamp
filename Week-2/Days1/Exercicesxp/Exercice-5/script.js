typeof(15)
// Prediction:number
// Actual:integer

typeof(5.5)
// Prediction:number
// Actual:float

typeof(NaN)
// Prediction:NaN
// Actual:boolean

typeof("hello")
// Prediction:bonjour
// Actual:string

typeof(true)
// Prediction:true
// Actual:true

typeof(1 != 2)
// Prediction:1!=2
// Actual:boolean

"hamburger" + "s"
// Prediction:humburgers
// Actual:string

"hamburgers" - "s"
// Prediction:humberger
// Actual:string

"1" + "3"
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:-2
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:"johnny5"

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction:NaN
// Actual:NaN

1 != 1
// Prediction:false
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false
// Actual:false