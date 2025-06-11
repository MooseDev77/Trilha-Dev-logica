function gerarTabuada() {
    // Pega o valor do input do HTML
    const numeroInput = document.gentElementById('numeroInput')
    let numero = parseInt(numeroInput.value)

    // Mostra o resultado onde a tabela deve ser exixbida
    const resultadoDiv = document.gentElementById('resultadoTabuada')
    resultadoDiv.innerHTML = ''

    // Adiciona um título para tabuada.
    resultadoDiv.innerHTML += `<h2>Tabuada do número ${numero} </h2>`

    // laço de repetição para gerar a tabuada.
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`
    
    }
}
// a função gerartabuada sera executada quando clicar no botão
const gerarBotao = document.getElementById('gerarBotao')
gerarBotao.addEventListener('click', gerarTabuada)