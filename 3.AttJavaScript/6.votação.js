let idade = 19

const votacao = (a) => {
    if (a < 16){
    console.log("Não pode votar.")
    } else if (a <= 17){
    console.log("voto opcional")
    } else if (a < 65){
    console.log("Voto obrigatório")
    } else{
    console.log("Não são obrigados a votar")
    }
}

votacao(idade)

