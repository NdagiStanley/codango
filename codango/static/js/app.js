$.getScript('//connect.facebook.net/en_US/sdk.js', function() {
    FB.init({
        appId: '1472709103038197',
        version: 'v2.5' // or v2.0, v2.1, v2.0
    });
    //FB.getLoginStatus(updateStatusCallback);
});
$.ajaxSetup({
    headers: {
        'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
    },
});
$(document).ready(function() {
    $('#id-snippet-body').hide();
    $('#flash-message').fadeOut(5000);
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
                if (data == "success") {
                    _this.append("<div class='alert-success successmsg'>Successfully Created Your Resource!</div>");
                    setTimeout(function() {
                        $(".successmsg").hide();
                    }, 5000)
                }
            },
            error: function(status) {
                console.log(status.responseText);
            },
            complete: function() {
                $("#community-content").load("/ajax/community/all", function() {
                    $("#id-snippet-body").hide();
                    _this.trigger("reset");
                });
            }
        });
    });
    // sidebar
    $("#more a").click(function(e) {
        e.preventDefault();
        if ($("#sidebar-more").css("display") == "block") {
            $("#sidebar-more").css("display", "none");
            $(this).text("...more...");
        } else {
            $("#sidebar-more").css("display", "block");
            $(this).text("...less...");
        }
    });
    $("#sidebar-mobile-link i").click(function() {
        if ($(this).hasClass("glyphicon glyphicon-chevron-right")) {
            $("#sidebar-mobile-link").hide()
            $("#sidebar-mobile").animate({
                "left": "0px"
            });
        }
    });
    $("#facebook-login").click(function(e) {
        e.preventDefault();
        FB.login(function(response) {
            if (response.authResponse) {
                console.log('Welcome!  Fetching your information.... ');
                FB.api('/me?fields=email,first_name,last_name,picture', function(user) {
                    console.log(user);
                    var ajaxinfo = {
                        url: "/login",
                        type: "POST",
                        data: user,
                        success: function(data) {
                            console.log(data);
                            if (data == "success") {
                                location.reload()
                            }
                            if (data == "register") {
                                $("#tab_link").trigger("click");
                                $("#signup-form").append("<input type='hidden' name='fb_id' value='" + user.id + "'>");
                                $("#id_email").val(user.email);
                            }
                        },
                        error: function(error) {
                            console.log(error.responseText);
                        }
                    }
                    $.ajax(ajaxinfo);
                });
            } else {
                console.log("Not logged in");
            }
        }, {
            scope: 'email,user_likes'
        })
    });

});