const readline = require ('readlines-sync')

const listaDeNumeros = []

for (let i = 1; i <= 5; i++ ) {
    let numero = readline.questionFloat(`Digite o ${i}º número: `)
    listaDeNumeros.push(numero)
}

const negativos = listaDeNumeros.filter(n => n < 0)
const positivos = listaDeNumeros.filter(n => n > 0).reduce((soma, total) => soma + total, 0)

console.log(`\nQuantidade de negativos: ${negativos.length}`)
console.log(`soma de positivos: ${positivos}`)
