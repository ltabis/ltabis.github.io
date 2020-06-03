import path from 'path';

export const fetchProjects = () => {
 
  fetch('https://api.github.com/users/ltabis/repos').then((data) => {
      data.json().then((projects) => {
          prepareProjects(projects);
      }).catch((err) => {
          console.log(err);
      })
  }).catch((err) => {
      console.log(err);
  });
}

const prepareProjects = (projects: any) => {

  projects.forEach(async (pj: any) => {

      let card = document.createElement('div');
      card.innerHTML = await (await fetch(path.join(__dirname,'src/html/project_card_template.html'))).text();

      const body = card.children[0].children[0].children;

      body[0].innerHTML = pj['name'];
      body[2].children[0].innerHTML = pj['description'];
      body[2].children[1].setAttribute('href', pj['html_url']);

      const grid = document.getElementById('project-grid');
      if (grid)
        grid.append(card);
  })
}