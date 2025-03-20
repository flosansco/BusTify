document.getElementById('simulation-form').addEventListener('submit', function(event) {
  // Empêcher la soumission classique du formulaire
  event.preventDefault();

  // Récupérer les données du formulaire
  const temperature = document.getElementById('temperature').value;
  const humidity = document.getElementById('humidity').value;
  const passengers = document.getElementById('passengers').value;

  const data = {
    temperature: parseFloat(temperature),
    humidity: parseFloat(humidity),
    passengers: parseInt(passengers)
  };

  // Envoyer les données en POST vers le backend
  fetch('http://127.0.0.1:8000/simulate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erreur serveur: ${response.status}`);
    }
    return response.json();
  })
  .then(result => {
    document.getElementById('result').textContent =
    `Résultat : ${result.message
    || 'Pas de message reçu'}`;
  })
  .catch(error => {
    document.getElementById('result').textContent = `Erreur : ${error.message}`;
  });
});
