document.querySelector('.descrição').addEventListener('click', ()=> {
    const divDesc = document.createElement("input");
    divDesc.type = 'text';
    divDesc.className = 'input-descrição';
    divDesc.name = 'texto'
    document.querySelector('.right-side').appendChild(divDesc);
});