// TODO: Implementar a lógica do chat em si ao invés de apenas uma coletânea de formulários
// TODO: Comentar igual um ser humano normal

// Evento de escuta para quando o documento estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    const resultDiv = document.getElementById('result');

    // Pega o formulário de INSERT e adiciona um evento de escuta
    document.getElementById('insertForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const table = document.getElementById('insertTable').value; // Pega a tabela
        const values = document.getElementById('insertValues').value.split(','); // Pega os valores mas separa com virgula pra passar em JSON

        fetch('/insert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ table, values }) // Converte o objeto em uma string JSON
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => console.error('Error:', error));
    });

    // Cria um evento para o formulário de SELECT
    document.getElementById('selectForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const table = document.getElementById('selectTable').value; // Análogo ao INSERT
        const columns = document.getElementById('selectColumns').value.split(',');
        const condition = document.getElementById('selectCondition').value || '1=1'; //Considera caso onde não tem condição como TRUE ou no caso 1=1

        const queryParams = new URLSearchParams({ table });
        columns.forEach(col => queryParams.append('columns', col));
        queryParams.append('condition', condition);

        fetch(`/select?${queryParams.toString()}`)
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => console.error('Error:', error));
    });

    // Abaixo vai ser feito análogamente aos anteriores com suas devidas peculiaridades
    document.getElementById('updateForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const table = document.getElementById('updateTable').value; // Análogo aos anteriores
        const columns = document.getElementById('updateColumns').value.split(',');
        const values = document.getElementById('updateValues').value.split(',');
        const condition = document.getElementById('updateCondition').value;

        fetch('/update', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ table, columns, values, condition })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => console.error('Error:', error));
    });

    document.getElementById('deleteForm').addEventListener('submit', (event) => {
        event.preventDefault();
        const table = document.getElementById('deleteTable').value; // Análogo aos anteriores
        const condition = document.getElementById('deleteCondition').value;

        fetch('/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ table, condition })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => console.error('Error:', error));
    });
});