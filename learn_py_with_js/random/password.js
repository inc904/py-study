// function generatePassword() {
//     const password = Math.random().toString(36).slice(2, 10);
//     console.log('Generated password: ', password)
//     return password;
// }


function generatePassword() {
    let length = 32;
    // 包含大小写字母和数字
    let charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    let password = '';

    for (let i = 0, n = charset.length; i < length; ++i) {
        password += charset.charAt(Math.floor(Math.random() * n));
    }
    console.log('Generated password: ', password)
}

generatePassword()