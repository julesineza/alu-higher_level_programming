
const args = process.argv.slice(2)

const fs = require("fs");

const filename= args[0]

fs.readFile(filename,"utf-8",(err,data) => {
    if (err){
        console.log(err)
        return
    }
    console.log(data)
})

