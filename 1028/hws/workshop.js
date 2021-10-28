const form = document.querySelector('form')
const ul = document.querySelector('ul')

function form_submit(e) {
  e.preventDefault()
  
  const todo = e.target.querySelector('input').value
  if (todo.trim()) {
    const li = document.createElement('li')
    const div = document.createElement('div')
    li.appendChild(div)
    
    const p = document.createElement('p')
    p.classList.add('todo-p')
    p.innerText = todo
    p.addEventListener('click', e => {
      const p = e.target
      if (p.classList.contains('done')) {
        p.classList.remove('done')
      }else {
        p.classList.add('done')
      }
    })
    div.appendChild(p)

    const btn = document.createElement('button')
    btn.innerText = 'X'
    btn.addEventListener('click', () => {
      ul.removeChild(li)
    })
    div.appendChild(btn)

    ul.appendChild(li)
  }else {
    alert('Todo를 입력해주세요!')
  }
  e.target.reset()
}

form.addEventListener('submit', form_submit)