const readlineSync = requere('readline-sync')

let a = readlineSync.questionFloat("Digite o valor desejado: ")
let b = readlineSync.questionFloat("Digite o valor desejado: ")
let c = readlineSync.questionFloat("Digite um numero aleatorio: ")


const  soma = a + b

if (soma < c) {
    console.log('A soma de A + B é menor que C')
} else {
    console.log('A soma A + B é maior que C')
 }
