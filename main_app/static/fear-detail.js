const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')

fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0]
  if (fileToUpload) {
    fileName.innerText = fileToUpload.name
  } else {
    fileName.innerText = ""
  }
})
