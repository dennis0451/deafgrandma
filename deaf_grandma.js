function deafGrandma() {
    let goodbyeCount = 0
    
    let continuedConvo = true
    while(continuedConvo){
    let input = window.prompt("Respond to grandma:")

    if(input === ''){
        response = "WHAT?!"
    }else if(input === input.toLowerCase()) {
        response = "SPEAK UP, KID!"
    }else if(input === input.toUpperCase()){
        response = "NO, NOT SINCE 1946!"
    }else if(input === "GOODBYE" && goodbyeCount === 0){
        goodbyeCount++
        response = "LEAVING SO SOON?"
    }else if(input ==="GOODBYE" && goodbyeCount === 1){
        response = "LATER, SKATER!"
        continuedConvo = false
    }
}
    alert(response)
}

deafGrandma();