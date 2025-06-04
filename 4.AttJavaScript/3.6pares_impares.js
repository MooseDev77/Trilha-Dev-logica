
const listaDeNumeros = [1, 2, 3, 4, 5, 6,]

console.log('Listando todos os numeros na lista.')
console.log(listaDeNumeros)

console.log('\nFiltrando os numeros pares:')
const pares = listaDeNumeros.filter(n => n % 2 === 0)
console.log(pares)

console.log('\nFiltrando numero impares:')
const impares = listaDeNumeros.filter(n => n % 2 !== 0)
console.log(impares)
