const menuIcon = document.querySelector('.menu-logo')
const Links = document.querySelector('.links')

menuIcon.addEventListener('click', () => {  
    Links.classList.toggle('active');
    }
)