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

	$("#community a").click(function(e){
		e.preventDefault();
		var url = $(this).attr("href");
		console.log( '/ajax'+ url);

		$("#community-content").load('/ajax' + url, function(data){

		});
	})

	$("#id_share_form").submit(function(e){
		e.preventDefault();
	
		 var fd = new FormData();
         var file_data = $('#id_share_form input[type="file"]')[0].files[0];
         fd.append("resource_file", file_data);
		 var other_data = $(this).serializeArray();
		 console.log(other_data);
		$.each(other_data,function(key,input){
            fd.append(input.name,input.value);
            });
		var _this = $(this);
		var url = $(this).attr("action");
		$.ajax({
			url: url,
			type: 'POST',
			contentType: false,
        	processData: false,
			data:fd,
			success: function(data){
				console.log(data);
			},
			error:function(status){
				console.log(status.responseText)
			},
			complete: function(){
			$("#community-content").load('/ajax/community/all', function(data){
			$("#id-snippet-body").hide();
			_this.trigger('reset');
		});

 
			}
		})
	})
});
