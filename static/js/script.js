 fetch('/download', { method: 'POST' })
  .then(response => {
    if (response.ok) {
      return response.json(); // Tente interpretar a resposta como JSON
    } else {
      return response.text().then(text => { // Pegue a resposta como texto
        throw new Error(`HTTP error! status: ${response.status}, response: ${text}`);
      });
    }
  })
  .then(data => {
    alert(data.message);
  })
  .catch(error => {
    alert('Erro ao fazer o download: ' + error.message);
  });
