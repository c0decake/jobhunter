function updateAddedOrders() {
    const addedOrdersTable = document.getElementById('offers-table-body')

    fetch('/search/get_added_orders/?director_mode=True')
        .then(response => response.json())
        .then(orders => {
            orders.forEach(order => {
                const newRow = addedOrdersTable.insertRow();

                for (let key in order) {
                    if (key === 'id') {

                    } else if (key === 'district' || key === 'address') {
                        let lastCell = newRow.lastElementChild
                        lastCell.textContent += ' - ' + order[key];
                    } else {
                        const newCell = newRow.insertCell();
                        if (key === 'date') {
                            newCell.textContent = new Date(order[key]).toLocaleDateString('ru-RU');
                        } else {
                            newCell.textContent = order[key];
                        }
                    }
                }
                newRow.addEventListener('click', () => {
                    showOrderModal()
                })
                addedOrdersTable.appendChild(newRow)
            })
        })
}

window.onload = function () {
    updateAddedOrders()
}

function showOrderModal() {
    const orderModal = document.getElementById('added-order-modal')

    orderModal.classList.toggle('added-order-modal-activate')
}