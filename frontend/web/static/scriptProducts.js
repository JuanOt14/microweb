function getProducts() {
  fetch('http://192.168.80.3:5003/api/products')
    .then(response => response.json())
    .then(data => {
      console.log(data);

      var tbody = document.querySelector('#product-list tbody');
      tbody.innerHTML = '';

      data.forEach(p => {
        var row = document.createElement('tr');

        var nameCell = document.createElement('td');
        nameCell.textContent = p.name;
        row.appendChild(nameCell);

        var descCell = document.createElement('td');
        descCell.textContent = p.description || '';
        row.appendChild(descCell);

        var priceCell = document.createElement('td');
        priceCell.textContent = p.price;
        row.appendChild(priceCell);

        var stockCell = document.createElement('td');
        stockCell.textContent = p.stock;
        row.appendChild(stockCell);

        var actionsCell = document.createElement('td');

        var editLink = document.createElement('a');
        editLink.href = `/editProduct/${p.id}`;
        editLink.textContent = 'Edit';
        editLink.className = 'btn btn-primary mr-2';
        actionsCell.appendChild(editLink);

        var deleteLink = document.createElement('a');
        deleteLink.href = '#';
        deleteLink.textContent = 'Delete';
        deleteLink.className = 'btn btn-danger';
        deleteLink.addEventListener('click', function() {
          deleteProduct(p.id);
        });
        actionsCell.appendChild(deleteLink);

        row.appendChild(actionsCell);
        tbody.appendChild(row);
      });
    })
    .catch(error => console.error('Error:', error));
}

function createProduct() {
  var data = {
    name: document.getElementById('pname').value,
    description: document.getElementById('pdesc').value,
    price: parseFloat(document.getElementById('pprice').value || 0),
    stock: parseInt(document.getElementById('pstock').value || 0)
  };

  fetch('http://192.168.80.3:5003/api/products', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    getProducts(); // refresca tabla
  })
  .catch(error => console.error('Error:', error));
}

function updateProduct() {
  var productId = document.getElementById('product-id').value;

  var data = {
    name: document.getElementById('pname').value,
    description: document.getElementById('pdesc').value,
    price: parseFloat(document.getElementById('pprice').value || 0),
    stock: parseInt(document.getElementById('pstock').value || 0)
  };

  fetch(`http://192.168.80.3:5003/api/products/${productId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    window.location.href = '/products';
  })
  .catch(error => console.error('Error:', error));
}

function deleteProduct(productId) {
  if (confirm('Are you sure you want to delete this product?')) {
    fetch(`http://192.168.80.3:5003/api/products/${productId}`, {
      method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      getProducts();
    })
    .catch(error => console.error('Error:', error));
  }
}
