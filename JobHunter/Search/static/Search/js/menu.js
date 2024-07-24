function Sidebar() {
    const sidebar = document.getElementById('sidebar')
    // const sel= sidebar.querySelectorAll('ul li')
    // const mainMenu = document.getElementById('main-menu-list')
    //
    // fetch('is_director/')
    //     .then(response => response.json())
    //     .then(answer => {
    //         if (answer['is_director'] === 'True' && sel.length === 4) {
    //             const aItem = document.createElement('a')
    //             aItem.text = 'Добавленные'
    //             aItem.style.cursor = 'pointer'
    //             const liItem = document.createElement('li')
    //             liItem.appendChild(aItem)
    //             sel[1].insertAdjacentElement('afterend', liItem)
    //         } else if (answer['is_director'] === 'False' && sel.length === 5) {
    //             mainMenu.removeChild(sel[2])
    //         }
    //     })

    sidebar.classList.toggle('active')
}