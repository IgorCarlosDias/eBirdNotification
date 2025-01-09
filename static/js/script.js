// Função para carregar as aves automaticamente ao carregar a página
document.addEventListener("DOMContentLoaded", function() {
    fetchAves();
});

function fetchAves() {
    const avesList = document.getElementById("aves-list");
    avesList.innerHTML = ''; // Limpa a lista antes de adicionar novas aves

    fetch('/aves')  // Faz uma requisição GET à rota do Flask que traz as aves
        .then(response => response.json())
        .then(data => {
            if (data && data.length > 0) {
                data.forEach(ave => {
                    const aveDiv = document.createElement('div');
                    aveDiv.classList.add('ave');
                    
                    aveDiv.innerHTML = `
                        <h3>${ave.sciName}</h3>
                        <p>Data: ${ave.obsDt}</p>
                        <p>Local: ${ave.locName}</p>
                    `;

                    avesList.appendChild(aveDiv);
                });
            } else {
                avesList.innerHTML = '<p>Nenhuma ave encontrada.</p>';
            }
        })
        .catch(error => {
            console.error('Erro ao carregar as aves:', error);
        });
}

document.getElementById('salvar-token').addEventListener('click', function() {
    const token = document.getElementById('ebird-token').value;
    
    if (token) {
        // Enviar o token para o servidor
        fetch('/salvar-token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ token: token })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
                location.reload();  // Recarregar a página após salvar o token
            } else {
                alert('Erro ao salvar o token.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    } else {
        alert('Por favor, insira um token válido.');
    }
});


    // Função para atualizar a página a cada 3 minutos
    setInterval(() => {
        window.location.reload();
    }, 3 * 60 * 1000); // 3 minutos em milissegundos