function ReverseString(text){
    let reverseText="";

    for (let char of text){
        reverseText=char+reverseText

    }

    return reverseText

}
console.log(ReverseString("python"))