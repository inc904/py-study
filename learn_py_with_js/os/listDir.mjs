import fs from 'fs'
import path from 'path'
import {fileURLToPath} from 'node:url';
import {dirname} from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);


function listItems(directoryPath) {
    const items = fs.readdirSync(directoryPath)
    items.forEach(item => {
        const itemPath = path.join(directoryPath, item)
        const stats = fs.statSync(itemPath)
        console.log(`${item} is a ${stats.isDirectory() ? 'directory' : 'file'}`)
    })
}

// listItems(path.join(__dirname))

listItems('../')