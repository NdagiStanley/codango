$.ajaxSetup({
    headers: {
        "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
    },
});

function socialLogin(user) {
    var ajaxinfo = {
        url: "/login",
        type: "POST",
        data: user,
        success: function(data) {
            
            if (data == "success") {
                location.reload();
            }
            if (data == "register") {
                $("#tab_link").trigger("click");
                if (user.first_name !== undefined) {
                    $("#signup-form").append("<input type='hidden' name='first_name' value='" + user.first_name + "'>");
                    $("#signup-form").append("<input type='hidden' name='last_name' value='" + user.last_name + "'>");
                } else {
                    $("#signup-form").append("<input type='hidden' name='first_name' value='" + user.given_name + "'>");
                    $("#signup-form").append("<input type='hidden' name='last_name' value='" + user.family_name + "'>");
                }
                $("#signup-form").append("<input type='hidden' name='fb_id' value='" + user.id + "'>");
                $("#id_email").val(user.email).attr("disabled", true);
            }
        },
        error: function(error) {
            
        }
    };
    $.ajax(ajaxinfo);
}

var facebookLogin = {
    config: {

        login: "#facebook-login",
        fb_id: '1472709103038197'
    },
    init: function(config) {
        $(facebookLogin.config.login).attr("disabled", true);
        if (config && typeof(config) == 'object') {
            $.extend(facebookLogin.config, config);
        }
        $.getScript("//connect.facebook.net/en_US/sdk.js", function() {
            FB.init({
                appId: facebookLogin.config.fb_id,
                version: "v2.5"
            });
            $(facebookLogin.config.login).attr("disabled", false);
        });
        $(facebookLogin.config.login).click(function(e) {
            e.preventDefault();
            facebookLogin.login();
        });
    },
    login: function() {
        FB.login(function(response) {
            if (response.authResponse) {
                console.log("Welcome!  Fetching your information.... ");
                FB.api("/me?fields=email,first_name,last_name,picture", socialLogin);
            } else {
                console.log("Not logged in");
            }
        }, {
            scope: "email,user_likes"
        });
    },
};
var googleLogin = {
    config: {
        login: "#google-login",
        OAUTHURL: 'https://accounts.google.com/o/oauth2/auth?',
        VALIDURL: 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=',
        SCOPE: 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email',
        CLIENTID: '58714074667-55ulgv6a4mfe63t3u4qdil3dumo6cmvv.apps.googleusercontent.com',
        REDIRECT: 'http://localhost:8000',
        LOGOUT: 'http://accounts.google.com/Logout',
        TYPE: 'token',
    },
    init: function(config) {
        if (config && typeof(config) == "object") {
            $.extend(googleLogin.config, config);
        }
        $(googleLogin.config.login).click(function(e) {
            googleLogin.login();
        });
    },
    login: function() {
        var __url = googleLogin.config.OAUTHURL + "scope=" + googleLogin.config.SCOPE + "&client_id=" + googleLogin.config.CLIENTID + "&redirect_uri=" + googleLogin.config.REDIRECT + "&response_type=" + googleLogin.config.TYPE;
        var win = window.open(__url, "windowname1", "width=800, height=600");
        var pollTimer = window.setInterval(function() {
            try {
                console.log(win.document.URL);
                if (win.document.URL.indexOf(googleLogin.config.REDIRECT) != -1) {
                    window.clearInterval(pollTimer);
                    var url = win.document.URL;
                    googleLogin.config.acToken = googleLogin.gup(url, "access_token");
                    var tokenType = googleLogin.gup(url, "token_type");
                    var xpiresIn = googleLogin.gup(url, "expires_in");
                    win.close();
                    googleLogin.validateToken(googleLogin.config.acToken);
                }
            } catch (e) {}
        }, 500);
    },
    gup: function(url, name) {
        name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
        var regexS = "[\\#&]" + name + "=([^&#]*)";
        var regex = new RegExp(regexS);
        var results = regex.exec(url);
        if (results === null) return "";
        else return results[1];
    },
    validateToken: function(token) {
        $.ajax({
            url: googleLogin.config.VALIDURL + token,
            data: null,
            success: function(responseText) {
                googleLogin.getGoogleUserInfo();
            },
            dataType: "jsonp"
        });
    },
    getGoogleUserInfo: function() {
        $.ajax({
            url: "https://www.googleapis.com/oauth2/v1/userinfo?access_token=" + googleLogin.config.acToken,
            data: null,
            success: socialLogin,
            dataType: "jsonp"
        });
    }
};
var ajaxContent = {
    config: {
        filter: "#community a",
        contentDiv: "#community-content"
    },
    init: function(config) {
        if (config && typeof(config) == "object") {
            $.extend(ajaxContent.config, config);
        }
        $(ajaxContent.config.filter).click(function(e) {
            e.preventDefault();

            var url = ajaxContent.buildUrl($(this));
            ajaxContent.loadContent(url);
            window.history.pushState("object or string", "Title", url);
            console.log($(location).attr('href'));

        });
    },
    buildUrl: function(_this) {
        _this.closest("ul").closest("li").removeClass('open');
        if(_this.hasClass('filterby')) return location.protocol+'//'+location.host+location.pathname + _this.attr('href');
        return _this.attr('href');
    },
    loadContent: function(url) {
        console.log(url);
        $(ajaxContent.config.contentDiv).load(url,ajaxContent.afterAction);

    },
    afterAction: function(data,status,xhr) {
        $("#sidebar-mobile-link").show();
        $("#sidebar-mobile").animate({
            "left": "-=200px"
        });
        //console.log(xhr.responseText)


        //console.log(xhr.responseText)
        prettyPrint();
    }
};
var shareForm = {
    config: {
        share: "#id_share_form"
    },
    init: function(config) {
        if (config && typeof(config) == "object") {
            $.extend(shareForm.config, config);
        }
        $("body").on("submit",shareForm.config.share,function(e) {
            e.preventDefault();
            var fd = shareForm.formContents($(this));
            var url = $(this).attr("action");
            shareForm.shareForm(url, fd, $(this));
        });
    },
    formContents: function(_this) {
        var fd = new FormData();

        if(_this.hasClass('share'))
        {
        var file_data = _this.find('input[type="file"]')[0].files[0];
        fd.append("resource_file", file_data);
    }
        var other_data = _this.serializeArray();
        
        $.each(other_data, function(key, input) {
            fd.append(input.name, input.value);
        });
        return fd;
    },
    shareForm: function(url, fd, _this) {

        $("#preloader").show();

        //console.log(fd.get('resource_id'));

        var data = _this.serializeArray();
        $.ajax({
            url: url,
            type: "POST",
            contentType: false,
            processData: false,
            data: fd,
            success: function(data) {
                if (data == "success") {
                    _this.append("<div class='alert alert-success successmsg'>Successfully Created Your Resource!</div>");
                    setTimeout(function() {
                        $(".successmsg").hide();
                    }, 5000);
                }
            },
            error: function(status) {

                // Display errors
                if (status.responseText == "emptypost") {
                    _this.prepend("<div class='alert alert-danger errormsg'>Empty Post!!</div>");
                } else {
                    _this.prepend("<div class='alert alert-danger errormsg'>Invalid file type or greater than 10MB</div>");
                }
                setTimeout(function() {
                    $(".errormsg").hide();
                }, 5000);

            },
            complete: function() {

                $("#preloader").hide();
            if(_this.hasClass('share')){
                $("#community-content").load(document.URL, function() {
                    $("#id-snippet-body").hide();
                    $("#id-pdf-file").removeClass("show");
                    _this.trigger("reset");
                    prettyPrint();
                });
            }
            else{
                selector = "#rcomments-"+ data[1]['value'];
                $(selector).load(document.URL + " "+ selector);
            }

            _this.trigger('reset');
            }
        });
    }
};
var mobileNav = {
    config: {
        linkNav: "#sidebar-mobile-link i"
    },
    init: function(config) {
        if (config && typeof(config) == "object") {
            $.extend(mobileNav.config, config);
        }
        $(mobileNav.config.linkNav).click(function(e) {
            e.preventDefault();
            mobileNav.showNav($(this));
        });
    },
    showNav: function(_this) {
        if (_this.hasClass("glyphicon glyphicon-chevron-right")) {
            $("#sidebar-mobile-link").hide();
            $("#sidebar-mobile").animate({
                "left": "0px"
            });
        }
    }
};

var votes = {
    config:{
        voteButton: ".like, .unlike"

    },
    init: function(config){
        if(config && typeof(config) == 'object') $.extend(votes.config, conifg);
        $("body").on('click',votes.config.voteButton,function(e){
            e.preventDefault();
            var url = $(this).attr("href");
            var resource_id = $(this).data("id");
            votes.doVote(url,resource_id,$(this));

        });
    },
    doVote: function(url,resource_id,_this){
        $.ajax({
            url:url,
            type:"POST",
            data:{
                resource_id: resource_id
            },
            success: function(data){
                console.log(data);
                if(data['status'] == "NoVote") _this.find('span').removeClass('active');
                else _this.find('span').addClass('active')
            if(_this.hasClass('like')){
                _this.siblings('.unlike').find('span').removeClass('active').text(data['downvotes'])
                _this.find('span').text(data['upvotes'])
            }
            else
            {
                _this.siblings('.like').find('span').removeClass('active').text(data['upvotes'])
                _this.find('span').text(data['downvotes'])
                

            }

            },
            error: function(x){
                console.log(x.responseText)
                
            }
        });

    }

}
$(document).ready(function() {
    facebookLogin.init({
        //fb_id: "1472691016373339"
    });
    googleLogin.init({
        //REDIRECT: "http://codango-staging.herokuapp.com/"
    });
    shareForm.init({share: "#id_share_form, .commentform"});
    ajaxContent.init({filter: "#community a,.filter-menu a"});
    mobileNav.init();
    votes.init();
    $('#id-snippet-body').hide();
    $('#flash-message').fadeOut(5000);
    $('#id-snippet-button').click(function() {
        $('#id-snippet-body').toggle();
    });
    $("#id-pdf-button").on("click", function(hidden) {
        hidden.preventDefault();
        $("#id-pdf-file").toggleClass("show");
    });
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
    // endless pagination plugin
    $.endlessPaginate({
        paginateOnScroll: true,
        paginateOnScrollMargin: 20
    });
    // syntax highlighter plugin
    prettyPrint();
    // Handling follow
    $('#follow-btn').click(function(e){
        e.preventDefault();
        var _this = $(this)
        var id = $(this).data('id');
        console.log(id);
        var url = $(this).attr('href');
        console.log(url);

        $.ajax({
            url: url,
            type: 'POST',
            success: function(data,textStatus,xhr){
                console.log(xhr.status);
                console.log("i still got here")
                console.log(_this)
                _this.attr('disabled', true);
                _this.text('following')
            },
            error: function(x){
                console.log(x.responseText)
            }

        })


    $(document).on("click",".mdi-comment",function(e){
        e.preventDefault();

        $(this).closest('.feed-content').find('.comments-div').toggle();
        
        //$(".feed-content .comments-div").toggle();
    });
});