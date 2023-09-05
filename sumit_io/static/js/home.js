'use strict'

const elements =[...document.getElementsByClassName('slide-out'),...document.getElementsByClassName('pop-translate')];
const main_container=document.getElementsByClassName('main-container')[0];
const form=document.getElementById('LeaveMessage');
const form_submit =form.querySelector('#form-submit');

const Leave_Message=form.getElementsByTagName('button')[0];

form_submit.addEventListener('click',(e)=>{
form.submit((e)=>{
e.preventDefault();
return false;

});
})

const eventfunction=(a,b)=>{
                            let item=undefined;
                            a.forEach((x)=>{    
                            item=x.target.classList;
                            console.log(x.target,x.intersectionRatio>0);
                            if(x.intersectionRatio>0.10&&item.contains('slide-out')){ 
                                          item.add('slide');
                                          observer.unobserve(x.target);               
                            }
                            else if(x.intersectionRatio>0.10&&item.contains('pop-translate')){
                                       item.remove('pop-translate');
                                       observer.unobserve(x.target);                            }  
                            });}                        
const observer=new IntersectionObserver(eventfunction,{root:null,threshold:[0,0.15]}) ;

elements.forEach((x) =>observer.observe(x));


Leave_Message.addEventListener('click',()=>{
    const form_div=form.getElementsByTagName('form')[0]; 
    form_div.classList.toggle('hidden'); 
})

/*
main_container.addEventListener('scroll',()=>{        
     elements.forEach((x) =>animate(x,'slide'));
    }
    );
function animate(element,animation){
    let Win_size=window.innerHeight;
    let Element_pos=element.getBoundingClientRect().top;
    if(Win_size>Element_pos&&Element_pos>0){
        element.classList.add(animation);
    }
}
*/








