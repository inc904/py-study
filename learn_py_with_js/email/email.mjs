const emailAddresses = [
    "john.doe@example1.com",
    "jane.smith@example2.com",
    "foo@bar.com",
];

const regex = /([^@]+)@(.+)/

emailAddresses.forEach(email => {
    const [_,username, domian] = email.match(regex)
    console.log(`username: ${username}, domian: ${domian}`)
})
