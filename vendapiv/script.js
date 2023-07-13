const ctx = document.getElementById('graficoIdeal');
fetch('resultados.json')
    .then(response => response.json())
    .then(data => {
    const nomes = data.map(row => row.nome);
    const quantidades = data.map(row => row.quantidade);

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: nomes,
        datasets: [{
            label: "Vendas",
            data: quantidades,
            backgroundColor: [
                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)',
                'rgba(75, 192, 192, 0.7)',
                'rgba(153, 102, 255, 0.7)',
                'rgba(255, 159, 64, 0.7)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 3)',
                'rgba(54, 162, 235, 3)',
                'rgba(255, 206, 86, 3)',
                'rgba(75, 192, 192, 3)',
                'rgba(153, 102, 255, 3)',
                'rgba(255, 159, 64, 3)'
            ],
            borderWidth:0 
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    crossAlign: 'Far'
                }
            }
        }
    }
});
}).catch(error => {
    console.error('Erro ao obter os dados:', error);
});

// Função para atualizar a página
function atualizarPagina() {
    location.reload();
}

// Agendar a atualização após um determinado período (em milissegundos)
setTimeout(atualizarPagina, 50000)
// setTimeout(atualizarPagina, 1800000);