const slideContainer = document.querySelector('.slide-container');
const menuToggle = document.querySelector('#menu-toggle');
const ativarMenu = document.querySelector('.menu-active');
const user = document.querySelector('.user');
const userData = document.querySelector('.user-data');
let slideIndex = 0;


function moveSlide(direction) {
  slideIndex += direction;
  slideContainer.scrollBy({
    left: slideContainer.offsetWidth * direction,
    behavior: 'smooth'
  });
}

menuToggle.addEventListener("click", ()=> {
  if (ativarMenu.style.display === "none") {
    ativarMenu.style.display = "block";
  } else {
    ativarMenu.style.display = "none";
  }

});
  
user.addEventListener("click", ()=> {
  if(userData.style.display === "none") {
    userData.style.display = "block";
  } else {
    userData.style.display = "none";
  }
})

document.querySelector('#CC-BH').addEventListener('click', ()=> {
  window.location = 'https://polybalasdistribuidora136696.rm.cloudtotvs.com.br/FrameHTML/Web/App/RH/PortalMeuRH/#/login'
})