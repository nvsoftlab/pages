const menu=document.querySelector('.menu'),nav=document.querySelector('.nav'),header=document.querySelector('.header');
menu?.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));document.body.classList.toggle('menu-open',open)});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu?.setAttribute('aria-expanded','false');document.body.classList.remove('menu-open')}));
addEventListener('scroll',()=>header?.classList.toggle('scrolled',scrollY>8),{passive:true});
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
document.getElementById('year').textContent=new Date().getFullYear();
document.getElementById('lead-form')?.addEventListener('submit',event=>{event.preventDefault();const form=event.currentTarget;if(!form.reportValidity())return;const data=new FormData(form),body=`Imię: ${data.get('name')}\nTelefon: ${data.get('phone')}\nUsługa: ${data.get('service')}\n\n${data.get('message')||''}`;form.querySelector('.form__success').hidden=false;location.href=`mailto:biuro@frigeris.pl?subject=${encodeURIComponent('Zapytanie ze strony — '+data.get('service'))}&body=${encodeURIComponent(body)}`});
