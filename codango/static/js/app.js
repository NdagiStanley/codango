$(document).ready(function(e) {
    $('#id-snippet-body').hide();
    $('#flash-message').fadeOut(5000);
    var snippet = $('#snippet')
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/python");
    editor.getSession().on('change', function() {
        snippet.val(editor.getSession().getValue());
    });
    $('#id-snippet-button').click(function() {
        $('#id-snippet-body').toggle();
    });
    $('#id-pdf-button').on('click', function(hidden) {
        hidden.preventDefault();
        $('#id-pdf-file').toggleClass('show');
    });
    $("#community a").click(function(e) {
        e.preventDefault();
        var url = $(this).attr("href");
        console.log('/ajax' + url);
        $("#community-content").load('/ajax' + url, function(data) {});
           $("#sidebar-mobile-link").show()
            $("#sidebar-mobile").animate({
                'left': '-=200px'
            });
    })
    $("#id_share_form").submit(function(e) {
            e.preventDefault();
            var fd = new FormData();
            var file_data = $('#id_share_form input[type="file"]')[0].files[0];
            fd.append("resource_file", file_data);
            var other_data = $(this).serializeArray();
            console.log(other_data);
            $.each(other_data, function(key, input) {
                fd.append(input.name, input.value);
            });
            var _this = $(this);
            var url = $(this).attr("action");
            $.ajax({
                url: url,
                type: 'POST',
                contentType: false,
                processData: false,
                data: fd,
                success: function(data) {
                    console.log(data);
                    if (data == "success") {
                        _this.append("<p class='text-success successmsg'>Successfully Created Your Resource!</p>"); 

                        setTimeout(function(){
                            $(".successmsg").hide();
                        },5000)
                        
                    }
                },
                error: function(status) {
                    console.log(status.responseText)
                },
                complete: function() {
                    $("#community-content").load('/ajax/community/all', function(data) {
                        $("#id-snippet-body").hide();
                        _this.trigger('reset');
                    });
                }
            })
        })
        // sidebar
    $("#more a").click(function(e) {
        e.preventDefault();
        if ($("#sidebar-more").css('display') == 'block') {
            $("#sidebar-more").css('display', 'none');
            $(this).text("...more...");
        } else {
            $("#sidebar-more").css('display', 'block');
            $(this).text("...less...");
        }
    });
    $("#sidebar-mobile-link i").click(function() {
        // e.preventDefault();
        if ($(this).hasClass("glyphicon glyphicon-chevron-right")) {
            $("#sidebar-mobile-link").hide()
            $("#sidebar-mobile").animate({
                'left': '0px'
            });
        } 
    });
})