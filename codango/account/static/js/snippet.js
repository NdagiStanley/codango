$(document).ready(function(){

	var snippet = $('#snippet')

	var editor = ace.edit("editor");
	editor.setTheme("ace/theme/twilight");
	editor.session.setMode("ace/mode/python");

	editor.getSession().on('change', function () {
		snippet.val(editor.getSession().getValue());
	});

		
	$('#id-snippet-body').load('home.html', function() {
		$(this).hide();
	});


	$('#id-snippet-button').click(function() {
		$('#id-snippet-body').toggle();
	});
});
