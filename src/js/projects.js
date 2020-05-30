
const fetchProjects = () => {

    fetch('https://api.github.com/users/ltabis/repos').then((data) => {
        data.json().then((projects) => {
            prepareProjects(projects)
        }).catch((err) => {
            console.log(err)
        })
    }).catch((err) => {
        console.log(err)
    });
}

const prepareProjects = (projects) => {

    projects.forEach(async (pj) => {

        let card = document.createElement('div')
        card.innerHTML = await (await fetch('src/html/project_card_template.html')).text()

        const body = card.children[0].children[0].children

        body[0].innerHTML = pj['name']
        body[2].children[0].innerHTML = pj['description']
        body[2].children[1].setAttribute('href', pj['html_url'])

        document.getElementById('project-grid').append(card)
    })
}

window.addEventListener('DOMContentLoaded', () => {
    fetchProjects()
})