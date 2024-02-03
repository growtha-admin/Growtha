const menuBtn = document.getElementById("menu_btn")
const mobileNav = document.querySelector(".mobile_navbar")
const main = document.getElementById("main")


menuBtn.addEventListener('click', () => {
    mobileNav.classList.toggle('remove_mobile_navbar');   
})


document.addEventListener('click', (e) => {
    if(e.target.id !== 'mobile_navbar' && e.target.id !== 'menu_btn') {    
        mobileNav.classList.remove('remove_mobile_navbar');
    }
})