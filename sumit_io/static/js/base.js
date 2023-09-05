let nav_bar=document.getElementsByClassName('nav-bar')[0];
let [menu_button,menu_close]=document.getElementsByClassName('menu-toggle ');
let cursor=document.getElementsByClassName('cursor');
menu_button.addEventListener('click',function() {

    menu_button.classList.add('hidden');
    menu_close.classList.remove('hidden');
    nav_bar.classList.toggle('hidden');
 
})
menu_close.addEventListener('click',function() {
    
    menu_button.classList.toggle('hidden');
    menu_close.classList.toggle('hidden');
    nav_bar.classList.toggle('hidden');
 
})

