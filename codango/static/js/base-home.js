$(document).ready(function(e){
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
})
