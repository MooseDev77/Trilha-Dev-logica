// Para ligar: npm install readline-sync 
const readline = require('readline-sync') 

listaDenotas = []

for (let i = 1; i <= 3; i++) {
    nota = readline.questionFloat(`Digite a ${i}ª nota: `)
    listaDeNumeros.push(nota)
}

console.log('\nSomadas notas: ')
soma = listaDeNumeros.reduce((soma,total) => soma + total, 0)
console.log(soma)

console.log('\nQuantidade de notas:')
quantidadedenotas = listaDeNumeros.length
console.log(quantidadedenotas)

console.log('\nMédia: ')
media = soma / quantidadedenotas
console.log(media)

console.log('\nExibindo todas as notas: ')
listaDenotas,forEach((notas, index) => console.log(`${++index}ª notas: ${notas} `))
