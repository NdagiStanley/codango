var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.getSession().setMode("ace/mode/javascript");
// JQuery element pointing to the ACE Editor
var $editor = $('#editor');
var FIREBASE_URL = 'https://intense-fire-2301.firebaseio.com/';
var root = new Firebase(FIREBASE_URL);
// Get reference to the sessions Node
var sessionsRef = root.child('sessions');
// Retrieve session ID
sessionId = $editor.data('id');
// Get reference to the Node of the current session
var thisSessionRef = sessionsRef.child(sessionId);

var app = {
    init: function() {
       app.bindEvents()
    },
    events: {
        updateFirebase: function(e) {
            if (e.keyCode == 13) {
                thisSessionRef.update({
                    content: editor.getValue()
                }, function(err) {

                });
            }
        },
        updateEditor: function(snap) {
            var session = snap.val();
            editor.setValue(session.content);
        }
    },
    bindEvents: function() {
        $editor.keyup(app.events.updateFirebase);
        thisSessionRef.on('value', app.events.updateEditor);
    }
};

app.init();