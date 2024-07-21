// Função para calcular a posição final do herói
function calcularPosicaoFinal(posicaoInicial, passos) {
    // Calcula a posição final somando a posição inicial com o número de passos
    let posicaoFinal = posicaoInicial + passos;
    return posicaoFinal;
}

// Exemplo de uso da função
let posicaoInicial = 2; // Altere este valor para testar diferentes cenários
let passos = 3; // Altere este valor para testar diferentes cenários

// Chama a função e exibe o resultado
let posicaoFinal = calcularPosicaoFinal(posicaoInicial, passos);
console.log(`Posição final do herói: ${posicaoFinal}`);
