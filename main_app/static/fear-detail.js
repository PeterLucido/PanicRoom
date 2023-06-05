const fileInput = document.getElementById('file-input')
const fileName = document.getElementById('file-name')
const imagePreview = document.getElementById('image-preview')

fileInput.addEventListener('change', evt => {
  const fileToUpload = evt.target.files[0]
  if (fileToUpload) {
    fileName.innerText = fileToUpload.name

    const reader = new FileReader()
    reader.onload = function(e) {
      imagePreview.src = e.target.result
      imagePreview.style.display = 'block'
    }
    reader.readAsDataURL(fileToUpload)
  } else {
    fileName.innerText = ""
    imagePreview.style.display = 'none'
  }
})
