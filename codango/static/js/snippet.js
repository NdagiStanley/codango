$(document).ready(function(){
    var snippet = $('#snippet');
    var editor = ace.edit('editor');
    editor.setTheme('ace/theme/twilight');
    editor.session.setMode('ace/mode/python');
    editor.getSession().on('change', function() {
        snippet.val(editor.getSession().getValue());
    });
});