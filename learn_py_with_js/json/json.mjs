import fs from 'fs'

fs.readFile('data.json', 'utf8', (err, data) => {
    if (err) {
        console.log(err)
        return
    }
    try {
        const jsonData = JSON.parse(data)
        console.log('jsonData:', jsonData)
        jsonData.port = 5432

        const updatedData = JSON.stringify(jsonData, null, 2)

        fs.writeFile('data.json', updatedData, 'utf8', (err) => {
            if (err) {
                console.log(err)
                return
            }

            console.log('data.json updated')
        })

    } catch (err) {
        console.log(err)
    }
})