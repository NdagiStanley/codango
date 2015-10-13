$(document).ready(function(e){
	$('#id-snippet-body').hide();
	$('#flash-message').fadeOut(3000);

	// sidebar
	$("#more a").click(function(e){
		e.preventDefault();
		if($("#sidebar-more").css('display') == 'block'){
			$("#sidebar-more").css('display','none');
			$(this).text("...more...");
		}
		else{
			$("#sidebar-more").css('display','block');
			$(this).text("...less...");
		}
	});
	$("#sidebar-mobile-link").click(function(e){
		e.preventDefault();

		$("#sidebar-mobile").animate({left:'0px'});
		$(this).css('visibility','hidden');
	});

	// snippet
	var snippet = $('#snippet')

	var editor = ace.edit("editor");
	editor.setTheme("ace/theme/twilight");
	editor.session.setMode("ace/mode/python");

	editor.getSession().on('change', function () {
		snippet.val(editor.getSession().getValue());
	});


	$('#id-snippet-button').click(function() {
		$('#id-snippet-body').toggle();
	});

	// pdf
	$('#id-pdf-button').on('click', function(hidden){
		hidden.preventDefault();
		$('#id-pdf-file').toggleClass('show');
	});
})
