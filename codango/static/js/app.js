$(document).ready(function(e){
	$('#id-snippet-body').hide();
	$('#flash-message').fadeOut(5000);

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
	$("#sidebar-mobile-link i").click(function(){
		// e.preventDefault();

		if($(this).hasClass("glyphicon glyphicon-chevron-right")){
			$("#sidebar-mobile-link").animate({'left':'+=200px'});
			$("#sidebar-mobile").animate({'left':'0px'});
			$(this).removeClass('glyphicon-chevron-right').addClass("glyphicon-chevron-left");
		}
		else if($("#sidebar-mobile-link i").hasClass("glyphicon glyphicon-chevron-left")){
			$("#sidebar-mobile-link").animate({'left':'-=200px'});
			$("#sidebar-mobile").animate({'left':'-=200px'});
			$(this).removeClass('glyphicon-chevron-left').addClass("glyphicon-chevron-right");
		}
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
