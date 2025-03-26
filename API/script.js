document.getElementById('simulation-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Empêche le rechargement de la page

  console.log('Simulation lancée. En attente des résultats...');

  const request = {
    busType: document.getElementById('bus-type').value,
    routeName: document.getElementById('route-name').value,
    temperature: parseFloat(document.getElementById('temperature').value),
    humidity: parseFloat(document.getElementById('humidity').value),
    coolingType: document.getElementById('cooling-type').value,
    optimization: document.getElementById('optimization').value
  };

  fetch('http://127.0.0.1:8000/simulate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Erreur réseau ou serveur.');
    }
    return response.json();
  })
  .then(result => {
    document.getElementById('pac-consumption').textContent = result.pacConsumption.toFixed(2);
    document.getElementById('acs-consumption').textContent = result.acsConsumption.toFixed(2);
    document.getElementById('btms-consumption').textContent = result.btmsConsumption.toFixed(2);
    document.getElementById('total-consumption').textContent = result.totalConsumption.toFixed(2);
  })
  .catch(error => {
    console.error('Erreur :', error);
    alert('Une erreur est survenue lors de la simulation.');
  });
});
