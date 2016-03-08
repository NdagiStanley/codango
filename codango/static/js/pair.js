/* global Firebase: true, $:true, FB:true, prettyPrint: true,
  ace:true, Firepad: true, FirepadUserList: true*/
/* eslint no-var: 0, func-names: 0*/
/* eslint no-alert: 0, func-names: 0*/
var FIRBASE_URL = 'https://intense-fire-2301.firebaseio.com/';

var editor = ace.edit('firepad-container');
var session = editor.getSession();

/**
 * Handles ace editor initialization
 * @param {string} langauge - the programming language of the session
 * @param {object} theme - the present theme being used by the session
 */
function init(language, theme) {
  editor.setTheme('ace/theme/' + theme);
  session.setMode('ace/mode/' + language);
}

$(document).ready(function () {
  var app = {
    init: function (selectedLanguage, selectedTheme) {
      // Set defaults for the theme and language
      var theme = selectedTheme || 'monokai';
      var language = selectedLanguage || 'javascript';
      // Get current session firebase ref

      app.bindEvents();
      // Initialize ACE Editor
      editor.setTheme('ace/theme/' + theme);
      session.setUseWrapMode(true);
      session.setUseWorker(false);
      session.setMode('ace/mode/' + language);
    },
    bindEvents: function () {
      // Language change event handler
      $('#language').change(function () {
        init($(this).val(), $('#theme').val());
      });

      // Theme change event handler
      $('#theme').change(function () {
        init($('#language').val(), $(this).val());
      });
    },
    getPageRef: function () {
      var firepadRef = new Firebase(FIRBASE_URL);
      var sessionId = $('#session-id').val();
      return firepadRef.child('session/' + sessionId);
    }
  };
  app.init();
});
