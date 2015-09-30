$(document).ready(function(){
	$('#id_pdf_button').on('click', function(eve){
		eve.preventDefault();
		$('#id_pdf_file').toggleClass('show');
	});
});