function sendSession(key){
    var ajaxinfo = {
        url: '/pair/',
        data:{
            sessionKey: key
        },
        type: "POST",
        success:function(data){
            console.log(data);
        },
        error: function(xhr){
            console.log(xhr.responseText);
        }
    };
    $.ajax(ajaxinfo);
}

function init(language, theme) {
      //// Initialize Firebase.
      var firepadRef = getExampleRef();
    var sessionKey = firepadRef.key();
    sendSession(sessionKey);

      // TODO: Replace above line with:
      // var firepadRef = new Firebase('<YOUR FIREBASE URL>');
      //// Create ACE
    // var user = request.user.username;
    //console.log(user)
        var userId = $('#username').val();
        console.log(userId);
    var firepadUserList = FirepadUserList.fromDiv(firepadRef.child('users'),
          document.getElementById('userlist'), userId);
      var editor = ace.edit("firepad-container");
      editor.setTheme("ace/theme/"+ theme);
      var session = editor.getSession();
      session.setUseWrapMode(true);
      session.setUseWorker(false);
      session.setMode("ace/mode/"+ language);
      console.log(language)
      console.log(theme)
      //// Create Firepad.
      var firepad = Firepad.fromACE(firepadRef, editor, {
        defaultText: '// JavaScript Editing with Firepad!\nfunction go() {\n  var message = "Hello, world.";\n  console.log(message);\n}'
      });
    }
    // Helper to get hash from end of URL or generate a random one.
function getExampleRef() {
      var ref = new Firebase('https://firepad.firebaseio-demo.com');
      var hash = window.location.hash.replace(/#/g, '');
      if (hash) {
        ref = ref.child(hash);
      } else {
        ref = ref.push(); // generate unique location.
        window.location = window.location + '#' + ref.key(); // add it as a hash to the URL.
      }
      if (typeof console !== 'undefined')
        console.log('Firebase data: ', ref.toString());
      return ref;
    }

$(document).ready(function() {
    $('#language').change(function (e) {
        init($(this).val());
    });
    $('#theme').change(function (e) {
        init($(this).val());
    });
    window.onload = init('javascript', 'monokai');
});