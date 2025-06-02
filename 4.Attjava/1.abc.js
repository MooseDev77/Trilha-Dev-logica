const readlineSync = requere('readline-sync')

function igual (var1, var2){
 if (var1 === var2) {
    return var1+var2
} else {
    return var1*var2
    }
}

function mensagen (var1, var2){
    if (var1 == var2) {
        console.log("Os valores são iguais. Somando: ")
    } else {
        console.log("Valores são diferentes. Vai ser multiplicado: ")
    }
}

let A = readlineSync.questionFloat("Digite o valor desejado: ")
let B = readlineSync.questionFloat("Digite o valor desejado: ")
let C = igualar(A,B)

mensagen (A,B)
console.log(C)
