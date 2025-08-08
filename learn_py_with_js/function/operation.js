let url = new URL('http://127.0.0.1:8000/books')

let params = {
    'title': '人间旅馆',
    'author': '陈年喜'
}


function addBook(title, author) {
    fetch(url.href, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title,
            author
        })
    })
        .then((response) => response.json())
        .then((response) => {
            console.log(response)
        })
}

addBook('人间旅馆', '陈年喜')