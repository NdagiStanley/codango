$(document).ready(function(){
	$('#id-pdf-button').on('click', function(hidden){
		hidden.preventDefault();
		$('#id-pdf-file').toggleClass('show');
	});
});