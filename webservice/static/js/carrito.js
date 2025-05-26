<button onclick="pagar()">Pagar</button>

<script>
function pagar() {
  const productos = [
    {title: "Producto 1", quantity: 2, unit_price: 5000},
    {title: "Producto 2", quantity: 1, unit_price: 3000},
  ];

  fetch('/pagar/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({productos: productos}),
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
}
</script>
