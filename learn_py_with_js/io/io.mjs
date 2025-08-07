import fs from 'fs'

const data = fs.readFileSync('./books.txt', 'utf8')
console.log(data)
const books = data.split('\r\n')
console.log(books)

const classics = ['红楼梦', '西游记', '水浒传', '三国演义']
const missingClassics = classics.filter(classic => !books.includes(classic))
console.log('missingClassics: ', missingClassics)

if (missingClassics.length === 0) {
    console.log('文件中已经包含全部四大名著')
} else {
    const missing = missingClassics.join('\r\n')
    // fs.writeFileSync('./books.txt', missing, 'utf8') // 没生效
    fs.appendFileSync('books.txt', `\n${missing}`, 'utf8');
    console.log('已补充缺失的名著到文件中：\r\n', `${missing
    }`)
}