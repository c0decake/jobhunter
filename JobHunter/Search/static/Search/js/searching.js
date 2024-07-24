function showCityOptions() {
    const citySelector = document.getElementById('searching-city')

    citySelector.innerText = ""

    fetch('/search/get_cities/')
        .then(response => response.json())
        .then(cities => {
            cities.forEach(city => {
                let option = document.createElement('option')
                option.text = city.name
                option.value = city.id
                citySelector.appendChild(option)
            })
        })

    showDistrictOptions()
}

function showDistrictOptions() {
    const districtSelector = document.getElementById('searching-district')
    let selectedCity = document.getElementById('searching-city').value
    districtSelector.innerText = ""
    console.log(selectedCity)
    fetch('/search/get_districts/?city=' + selectedCity.toString())
        .then(response => response.json())
        .then(districts => {
            districts.forEach(district => {
                let option = document.createElement('option')
                option.text = district.name
                option.value = district.id
                districtSelector.appendChild(option)
            })
        })
}

function showPostOptions() {
    const postSelector = document.getElementById('searching-post')

    postSelector.innerText = ""

    fetch('/search/get_posts/')
        .then(response => response.json())
        .then(posts => {
            posts.forEach(post => {
                let option = document.createElement('option')
                option.text = post.name
                option.value = post.id
                postSelector.appendChild(option)
            })
        })
}

function updateOffers() {
    const offersTable = document.getElementById('offers-table-body')

    fetch('/search/get_orders/')
        .then(response => response.json())
        .then(orders => {
            orders.forEach(order => {
                const newRow = offersTable.insertRow();


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
                let orderBtn = document.createElement('button')
                orderBtn.textContent = "Беру"
                orderBtn.className = "order-button"
                orderBtn.id = order.id
                orderBtn.addEventListener('click', () => {
                    updateModalOrderData(event.target.id)
                    const orderModal = document.getElementById('order-window')

                    orderModal.classList.toggle('order-modal-active')
                })
                const newCell = newRow.insertCell();
                newCell.appendChild(orderBtn);
                offersTable.appendChild(newRow)
            })
        })
}

window.onload = function () {
    showCityOptions()
    showPostOptions()
    updateOffers()
}

function updateModalOrderData(order_id) {
    const orderDataList = document.querySelectorAll('#modal-order-data-list li');

    orderDataList.forEach(li => {
        const spans = li.querySelectorAll('span');
        if (spans.length > 1) {
            for (let i = 1; i < spans.length; i++) {
                li.removeChild(spans[i]);
            }
        }
    });

    fetch('/search/get_orders/?order=' + order_id.toString())
        .then(response => response.json())
        .then(orders => {
            orders.forEach(order => {
                for (let param in order) {
                    if (param === 'date') {
                        order[param] = new Date(order[param]).toLocaleDateString('ru-RU')
                    }
                    let paramElement = document.getElementById('order_' + param.toString())
                    let orderParamSpan = document.createElement('span')
                    orderParamSpan.textContent = order[param]
                    paramElement.appendChild(orderParamSpan)
                }
            })
        })
}

function showTaxiToPopup() {
    const taxiToPopup = document.getElementById('taxi-to-popup')

    taxiToPopup.classList.toggle('taxi-to-popup-activate')
}

function showTaxiFromPopup() {
    const taxiFromPopup = document.getElementById('taxi-from-popup')

    taxiFromPopup.classList.toggle('taxi-from-popup-activate')
}

function showDrinksPopup() {
    const drinksPopup = document.getElementById('drinks-popup')

    drinksPopup.classList.toggle('drinks-popup-activate')
}

function showFoodPopup() {
    const foodPopup = document.getElementById('food-popup')

    foodPopup.classList.toggle('food-popup-activate')
}

function showToiletPopup() {
    const toiletPopup = document.getElementById('toilet-popup')

    toiletPopup.classList.toggle('toilet-popup-activate')
}

function closeOrderModal() {
    const orderModal = document.getElementById('order-window')

    orderModal.classList.toggle('order-modal-active')
}

// function updateOrders() {
//     const keys = ['city', 'district', 'post', 'date'];
//     const checkboxKeys = ['taxi', 'toilet', 'food', 'drinks'];
//     const tableBody = document.querySelector('tbody');
//
//
//     const data = new URLSearchParams();
//
//     for (const key of keys) {
//         data.append(key, document.getElementById(${key}-selector).value);
//     }
//     for (const key of checkboxKeys) {
//         data.append(key, document.getElementById(${key}-checkbox).checked);
//     }
//
//     fetch('/menu/get_orders/?' + data.toString())
//         .then(response => response.json())
//         .then(orders => {
//             orders.forEach(order => {
//                 const newOrder = tableBody.insertRow();
//                 const orderCell = newOrder.insertCell();
//                 newOrder.classList.add('order');
//                 newOrder.setAttribute('id', order.id);
//                 if (!document.getElementById(order.id)) {
//                     ordersBlock.appendChild(renderOrders(newOrder, order));
//                 }
//             });
//         });
// }
