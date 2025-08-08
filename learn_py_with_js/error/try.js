const fs = require('fs')
try {
    const content = fs.readFileSync('file-not-exist.txt', 'utf8')
    console.log('content:', content)
    const lines = content.split('\n')
    console.log('lines:', lines)

    for (const line of lines) {
        if (line.trim() !== '') {
            console.log(line)
        }
    }

    const firstLine = lines[0].trim();
    console.log(`First line: ${firstLine}`);

    const numbers = lines.map(Number);
    console.log('numbers:', numbers)
    console.log(`Sum of numbers: ${numbers.reduce((a, b) => a + b, 0)}`);

} catch (error) {
    console.error(`An error occurred: ${error.message}`);
}