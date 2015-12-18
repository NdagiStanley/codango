var FIRBASE_URL = "https://intense-fire-2301.firebaseio.com/";

var editor = ace.edit("firepad-container");
var session = editor.getSession();

/* Initialize the ACE Editor */
function init(language, theme) {
    editor.setTheme("ace/theme/" + theme);
    session.setMode("ace/mode/" + language);
}

// Helper to get hash from end of URL or generate a random one.
function getPageRef() {
    


}

$(document).ready(function () {
    var app = {
        init: function(language, theme) {
            // Initialize the events
            app.bindEvents();
            // Get the username
            var userId = $("#username").val();

            // Set defaults for the theme and language
            theme = theme || 'monokai';
            language = language || 'javascript';

            // Get current session firebase ref
            var thisSessionRef = app.getPageRef();

            // Initialize ACE Editor
            //var editor = ace.edit("firepad-container");
            editor.setTheme("ace/theme/" + theme);
            //var session = editor.getSession();
            session.setUseWrapMode(true);
            session.setUseWorker(false);
            session.setMode("ace/mode/" + language);
            
            // Create Firepad
            var firepad = Firepad.fromACE(thisSessionRef, editor, {
                defaultText: '// JavaScript Editing with Firepad!\nfunction go() {\n  var message = "Hello, world.";\n  console.log(message);\n}'
            });

            var firepadUserList = FirepadUserList.fromDiv(thisSessionRef.child('users'),
                document.getElementById('userlist'), userId);
            console.log(firepadUserList);
        },
        bindEvents: function() {
            // Language change event handler
            $('#language').change(function (e) {
                init($(this).val(), $("#theme").val());

            });

            // Theme change event handler
            $('#theme').change(function (e) {
                init($('#language').val(), $(this).val());
            });
        },
        getPageRef: function() {
            var firepadRef = new Firebase(FIRBASE_URL);
            var sessionId = $("#session-id").val();
            return firepadRef.child('session/' + sessionId);
        }
    };
    
    app.init();
});