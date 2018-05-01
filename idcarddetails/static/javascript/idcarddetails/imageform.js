function toggleImageAdditionForm() {
	var imageForm = document.getElementById('id_imageForm');
	var imageAddToggleButton = document.getElementById('imageFormToggleButton')
	if (imageForm.style.display === 'none') {
		imageForm.style.display = 'block';
		imageFormToggleButton.innerText = 'Hide Image form';
	}
	else{
		imageForm.style.display = 'none';
		imageFormToggleButton.innerText = 'Add another image';
	}

}