// Carrega os projetos da API Flask
fetch("/api/projects")
  .then((response) => response.json())
  .then((projects) => {
    const list = document.getElementById("project-list");
    projects.forEach((p) => {
      const li = document.createElement("li");
      li.textContent = p.nome;
      li.onclick = () => mostrarDetalhes(p);
      list.appendChild(li);
    });
  });

function mostrarDetalhes(projeto) {
  const details = document.getElementById("project-details");
  details.innerHTML = `
    <h2>${projeto.nome}</h2>
    <p>Status: ${projeto.status}</p>
    <p>Descrição: ${projeto.descricao}</p>
    <img src="${projeto.bandeira}" alt="Bandeira" width="100">
  `;
}
