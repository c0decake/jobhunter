function updateDistricts(citySelectorId, districtSelectorId) {
    const selectedCity = document.getElementById(citySelectorId).value;
    const districtSelect = document.getElementById(districtSelectorId);
    districtSelect.innerHTML = '<option value="">Выберите район</option>'; // Очистка списка

    fetch('/menu/get_districts?city=' + selectedCity)
        .then(response => response.json())
        .then(districts => {
            districts.forEach(district => {
                const option = document.createElement('option');
                option.value = district.id;
                option.text = district.name;
                districtSelect.add(option);
            });
            if (districtSelect.options.length === 1) {
                districtSelect.disabled = true;
                districtSelect.options[0].text = "Нет районов";
            }
            else {
                districtSelect.disabled = false
            }
        });

}


function updateShops() {
    const selectedDistrict = document.getElementById("district").value;
    const shopField = document.getElementById("shop");
    shopField.innerHTML = '<option value="">Выберите магазин</option>';


    fetch('/menu/get_shops/?district=' + selectedDistrict)
        .then(response => response.json())
        .then(shops => {
            shops.forEach(shop => {
                const option = document.createElement('option');
                option.value = shop.id; // ID района
                option.text = shop.name; // Название района
                shopField.add(option);
            });
        });
}