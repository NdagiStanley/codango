/* global Firebase: true, $:true, FB:true, prettyPrint: true */
/* eslint no-var: 0, func-names: 0*/
/* eslint no-alert: 0, func-names: 0*/

var myDataRef = new Firebase('https://popping-inferno-54.firebaseio.com/');
var ajaxContent;
var formPost;
var mobileNav;
var votes;
var deleteComment;
var editComment;
var readNotification;
var followAction;
var realTime;
var eventListeners;
var invitedUsers = [];
var inviteToSession;

$.ajaxSetup({
  headers: {
    'X-CSRFToken': $("meta[name='csrf-token']").attr('content')
  },
  beforeSend: function beforeSend() {
    $('#preloader').show();
  },
  complete: function complete() {
    $('#preloader').hide();
  }
});


/**
 * Loads comment to a particular div after an action.
 * @param {func} _this - jquery instance to be mainpulated for the comment session
 */
function loadComments(_this) {
  var selector = '#' + _this.closest('.comments').attr('id');
  $(selector).load(document.URL + ' ' + selector);
}

/**
 * Post user activity firebase server
 * @param {object} data - Object container the data information to be passed to the firebase backend
 */
function postDataToFireBase(data) {
  var firebaseData = {
    link: data.link,
    activity_type: data.type,
    read: data.read,
    content: data.content,
    user_id: data.user_id,
    created_at: Firebase.ServerValue.TIMESTAMP
  };

  myDataRef.push(firebaseData);
}
/**
 * Post user activity to django backend.
 * @param {object} data - the data instance to be sent to firebase server
 */
function postActivity(data) {
  $.ajax({
    url: $('#notification-li').data('url'),
    type: 'POST',
    data: data,
    success: function () {
      postDataToFireBase(data);
    }
  });
}

ajaxContent = {
  config: {
    contentDiv: '#community-content'
  },
  init: function (config) {
    if (config && typeof(config) === 'object') {
      $.extend(ajaxContent.config, config);
    }
    $('body').on('click', ajaxContent.config.filter, function (e) {
      var _this = $(this);
      var _text = _this.text().replace(/\s+/g, '');
      var url = ajaxContent.buildUrl($(this));
      e.preventDefault();
      if (!(_this.closest('ul').hasClass('filter-menu'))) $('#community a').removeClass('active');
      $('#community a').each(function () {
        if ($(this).text().replace(/\s+/g, '') === _text) {
          $(this).addClass('active');
          return;
        }
      });
      $(this).addClass('active');
      ajaxContent.loadContent(url);
      window.history.pushState('object or string', 'Title', url);
    });
  },
  buildUrl: function (_this) {
    _this.closest('ul').closest('li').removeClass('open');
    if (_this.hasClass('filterby')) {
      return location.protocol + '//' + location.host + location.pathname + _this.attr('href');
    }
    return _this.attr('href');
  },
  loadContent: function (url) {
    $(ajaxContent.config.contentDiv).load(url, ajaxContent.afterAction);
  },
  afterAction: function () {
    $('#sidebar-mobile-link').show();
    $('#sidebar-mobile').animate({
      left: '-=200px'
    });
    prettyPrint();
  }
};


formPost = {
  config: {
    share: '#id_share_form'
  },
  init: function (config) {
    if (config && typeof(config) === 'object') {
      $.extend(formPost.config, config);
    }
    $('body').on('submit', formPost.config.share, function (e) {
      var fd = formPost.formContents($(this));
      var url = $(this).attr('action');
      e.preventDefault();
      formPost.share(url, fd, $(this));
    });
  },
  formContents: function (_this) {
    var fd = new FormData();
    var fileData;
    var otherData;
    if (_this.hasClass('share')) {
      fileData = _this.find('input[type="file"]')[0].files[0];
      fd.append('resource_file', fileData);
    }
    otherData = _this.serializeArray();
    $.each(otherData, function (key, input) {
      fd.append(input.name, input.value);
    });
    return fd;
  },

  share: function (url, fd, _this) {
    var data = _this.serializeArray();
    $('#preloader').show();
    $.ajax({
      url: url,
      type: 'POST',
      contentType: false,
      processData: false,
      data: fd,
      success: function (userData) {
        if (typeof(userData) === 'object') {
          if (Array.isArray(userData.user_id)) {
            userData.user_id.forEach(function (value) {
              // Re-assgin the call back variable
              var postData = userData;
              // set the user id to the current value
              postData.user_id = value;

              postActivity(postData);
            });
          } else {
            postActivity(userData);
          }
          _this.append('<div class="alert alert-success successmsg">' + userData.status + '</div>');
          setTimeout(function () {
            $('.successmsg').hide();
          }, 5000);
        }
      },
      error: function (status) {
        if (status.responseText === 'emptypost') {
          _this.prepend('<div class="alert alert-danger errormsg">Empty Post!!</div>');
        } else {
          _this.prepend('<div class="alert alert-danger errormsg">' +
            'Invalid file type or greater than 10MB</div>');
        }
        setTimeout(function () {
          $('.errormsg').hide();
        }, 5000);
      },
      complete: function () {
        var selector = '#rcomments-' + data[1].value;
        var commentcount = '.commentcount-' + data[1].value;
        if (_this.hasClass('share')) {
          $('#community-content').load(document.URL, function () {
            $('#id-snippet-body').hide();
            $('#id-pdf-file').removeClass('show');
            _this.trigger('reset');
            prettyPrint();
          });
        } else {
          $(selector).load(document.URL + ' ' + selector);
          $(commentcount).load(document.URL + ' ' + commentcount);
        }
        _this.trigger('reset');
      }
    });
  }
};

mobileNav = {
  config: {
    linkNav: '#sidebar-mobile-link i'
  },
  init: function (config) {
    if (config && typeof(config) === 'object') {
      $.extend(mobileNav.config, config);
    }
    $(mobileNav.config.linkNav).click(function (e) {
      e.preventDefault();
      mobileNav.showNav($(this));
    });
  },
  showNav: function (_this) {
    if (_this.hasClass('glyphicon glyphicon-chevron-right')) {
      $('#sidebar-mobile-link').hide();
      $('#sidebar-mobile').animate({
        left: '0px'
      });
    }
  }
};

votes = {
  config: {
    voteButton: '.like, .unlike'
  },
  init: function (config) {
    if (config && typeof(config) === 'object') $.extend(votes.config, config);
    $('body').on('click', votes.config.voteButton, function (e) {
      var resourceId = $(this).data('id');
      var url = $(this).attr('href');
      e.preventDefault();

      votes.doVote(url, resourceId, $(this));
    });
  },
  doVote: function (url, resourceId, _this) {
    $.ajax({
      url: url,
      type: 'POST',
      data: {
        resource_id: resourceId
      },
      success: function (data) {
        if (data.user_id !== undefined) postActivity(data);
        if (data.status === 'unvotes') _this.removeClass('active');
        else _this.addClass('active');
        if (_this.hasClass('like')) {
          _this.siblings('.unlike').removeClass('active')
          .find('span').html('&nbsp;&nbsp;' + data.downvotes);
          _this.find('span').html('&nbsp;&nbsp;' + data.upvotes);
        } else {
          _this.siblings('.like').removeClass('active')
          .find('span').html('&nbsp;&nbsp;' + data.upvotes);
          _this.find('span').html('&nbsp;&nbsp;' + data.downvotes);
        }
      }
    });
  }
};


deleteComment = {
  config: {
    button: '.delete-comment'
  },
  init: function (config) {
    if (config && typeof config === 'object') $.extend(deleteComment.config, config);
    $('body').on('click', deleteComment.config.button, function (e) {
      e.preventDefault();
      if (!confirm('Are you sure you want to delete this comment')) return;
      deleteComment.sendAction($(this));
    });
  },
  sendAction: function (_this) {
    $.ajax({
      url: _this.attr('href'),
      type: 'DELETE',
      success: loadComments(_this)
    });
  }
};

editComment = {
  config: {
    button: '.edit-comment'
  },
  init: function (config) {
    if (config && typeof config === 'object') $.extend(editComment.config, config);
    $('body').on('submit', editComment.config.button, function (e) {
      e.preventDefault();
      editComment.sendAction($(this));
    });
  },
  sendAction: function (_this) {
    $.ajax({
      url: _this.attr('action'),
      type: 'PUT',
      contentType: 'application/json; charset=utf-8',
      processData: false,
      data: JSON.stringify({
        content: _this.find('textarea[name="content"]').val()
      }),
      success: loadComments(_this)
    });
  }
};

readNotification = {
  config: {
    button: '#notifications .list-group-item'
  },
  init: function (config) {
    if (config && typeof config === 'object') $.extend(readNotification.config, config);
    $('body').on('click', readNotification.config.button, function (e) {
      e.preventDefault();
      readNotification.readAction($(this));
    });
  },
  readAction: function (_this) {
    $.ajax({
      url: _this.data('url'),
      type: 'PUT',
      contentType: 'application/json; charset=utf-8',
      processData: false,
      data: JSON.stringify({
        id: _this.data('id')
      }),
      success: function () {
        location.assign(_this.attr('href'));
      }
    });
  }
};
// Handling follow

followAction = {
  config: {
    button: '#follow-btn'
  },
  init: function (config) {
    if (config && typeof config === 'object') $.extend(followAction.config, config);
    $('body').on('click', followAction.config.button, function (e) {
      var _this = $(this);
      var url = $(this).attr('href');
      e.preventDefault();
      followAction.doFollow(_this, url);
    });
  },
  doFollow: function (_this, url) {
    $.ajax({
      url: url,
      type: 'POST',
      success: function (data) {
        postActivity(data);
        $('h2.stats.followers').text(data.no_of_followers);
        $('h2.stats.following').text(data.no_following);

        _this.attr('disabled', true);
        _this.text('following');
      }

    });
  }
};

realTime = {
  config: {
    ulItems: '#notification-li', // For the ul elements from the fixed navbar
    panel: '#notifcation-panel', // The panel to add new notifcation real time
    newNotficationDiv: '#new-notifications', // The fixed new-notifications div at the bottom right
    timeoutid: 2, // Timeout avoid memory leak
    newItems: false // variable to disable firebase real time loading all the ojects at once
  },
  init: function (config) {
    if (config && typeof config === 'object') $.extend(realTime.config, config);
    // If there is changes to the databsse initalize new items to true
    myDataRef.once('value', function () {
      realTime.config.newItems = true;
    });
    myDataRef.on('child_added', function (snapshot) {
      var activity = snapshot.val(); // Value of the newly added database values
      if (!realTime.config.newItems) return; // if there is no new item dont load any div
      if (activity.user_id === Number($(realTime.config.ulItems).data('id'))) {
        realTime.loadNotifications(activity);
      }
    });
  },
  newNotification: function (activity) {
    // New items from the notification firebase realtime link
    var newNotification = '<div class="list-group">';
    newNotification += '<a href="+activity.link+"" class="list-group-item">';
    newNotification += '<h4 class="list-group-item-heading">' + activity.activity_type + '</h4>';
    newNotification += '<p class="list-group-item-text">' + activity.content + '<br>';
    newNotification += '<small>about ' +
                        Math.round((new Date() - new Date(activity.created_at)) / 60000) +
                      ' minutes ago<small></p>';
    newNotification += '</a>';
    newNotification += '</div>';

    return newNotification;
  },
  loadNotifications: function (activity) {
    $(realTime.config.ulItems).load($(realTime.config.ulItems).data('url'), function () {
      realTime.callbackDiv(activity);
    });
  },
  callbackDiv: function (activity) {
    var notifyDiv = realTime.newNotification(activity);
    $(realTime.config.panel).html(notifyDiv);
    $(realTime.config.newNotficationDiv).show();
    clearTimeout(realTime.config.timeoutid);
    realTime.config.timeoutid = setTimeout(function () {
      $(realTime.config.newNotficationDiv).fadeOut('slow');
      $(realTime.config.panel).empty();
    }, 3000);
  }
};


eventListeners = {
  init: function () {
    // Shows the edit comments box
    $('body').on('click', '.show-edit', function (e) {
      e.preventDefault();
      $(this).closest('div').siblings('.edit-view').show();
      $(this).closest('.view').hide();
    });

    // Deletes all notifications
    $('body').on('click', '#delete-notifications', function (e) {
      e.preventDefault();
      if (!confirm('Are you sure you want to clear your notifications')) return;
      $.ajax({
        url: $('#notification-li').data('url'),
        type: 'DELETE',
        data: { sample: 'data' },
        success: function () {
          $('#notification-li').load($('#notification-li').data('url'));
        }
      });
    });

    // Shows the comments when we stop editing
    $('body').on('click', '.show-view', function (e) {
      e.preventDefault();
      $(this).closest('.edit-view').hide();
      $('.view').show();
    });

    // Shows all the comments on a resource
    $(document).on('click', '.mdi-comment', function (e) {
      e.preventDefault();
      $(this).closest('.feed-content').find('.comments-div').toggle();
    });

    // Responsive view sidebar slide in
    $('#more a').click(function (e) {
      e.preventDefault();
      if ($('#sidebar-more').css('display') === 'block') {
        $('#sidebar-more').css('display', 'none');
        $(this).text('...more...');
      } else {
        $('#sidebar-more').css('display', 'block');
        $(this).text('...less...');
      }
    });

    // Shows the snippet box
    $('#id-snippet-button').click(function () {
      $('#id-snippet-body').toggle();
    });

    // Shows the file upload field
    $('#id-pdf-button').on('click', function (hidden) {
      hidden.preventDefault();
      $('#id-pdf-file').toggleClass('show');
    });

    // Ensures all flash messages fadeout after 2 seconds
    setTimeout(function () {
      $('#flash-message').fadeOut();
    }, 2000);
  }
};

inviteToSession = {
  config: {
    button: '#invite-div > button',
    deleteButton: '#invited-users .mdi-delete',
    sendButton: '.invite > button',
    form: 'form.invite',
    inviteDiv: '#invited-users',
    validateDiv: '#validation-error',
    loader: '#loader'
  },
  init: function (config) {
    if (typeof(config) === 'object') $.extend(inviteToSession.config, config);
    $(inviteToSession.config.button).click(function (e) {
      var email = $('#invite-div').find('input').val();
      e.preventDefault();

      // checks if the email is valid
      if (!inviteToSession.verifyEmail(email)) {
        return inviteToSession.validationError('Invalid Email Address');
      }
      // Checks if the email is not already on the list
      if (!inviteToSession.isEmailInList(email)) {
        return inviteToSession.validationError('Email is already in the list');
      }
      // Reset the error message paragraph tag
      $(inviteToSession.config.validateDiv).html('');

      // Push the email to the list of emails available
      invitedUsers.push(email);
       // Reset the input form
      $(this).closest('form').trigger('reset');
      // Show the email in the html div
      inviteToSession.buildHtml();
    });
    $('body').on('click', inviteToSession.config.deleteButton, function (e) {
      // Deletes email from the list
      var email = $(this).data('email');
      e.preventDefault();

      // Connects to the method that deletes the email from the available array
      inviteToSession.deleteEmail($(this), email);
    });

    $(inviteToSession.config.sendButton).click(function (e) {
      // Sends the email array to the backend
      var url = $(this).closest('form').attr('action');
      e.preventDefault();
      // Checks if the invited users list is not empty and output the required message
      if (invitedUsers.length > 0) inviteToSession.sendInvites(url);
      else inviteToSession.validationError('No email address(es) present');
    });
    $(inviteToSession.config.form).submit(function (e) {
      // Sets the default action of the form to add email instead of submit
      e.preventDefault();
      inviteToSession.config.button.trigger('click');
    });
  },
  verifyEmail: function (email) {
    // email validation logic
    if (!/[^\s@]+@[^\s@]+\.[^\s@]+/.test(email)) {
      return false;
    }
    return true;
  },
  isEmailInList: function (email) {
    // Validate email presence
    if (invitedUsers.indexOf(email) !== -1) return false;
    return true;
  },
  buildHtml: function () {
    // Build the html for the emails present
    var htmlElement = '';
    invitedUsers.forEach(function (val) {
      htmlElement += '<div class="form-group>" <p class="lead">' + val +
                      '&nbsp;&nbsp;' +
                      '<span class="mdi mdi-delete" data-email=' + val +
                      '></span></p></div>';
    });
    // Insert the html to the required div
    $(inviteToSession.config.inviteDiv).html(htmlElement);
  },
  deleteEmail: function (_this, email) {
    // Deletes email from the global scope
    var index = invitedUsers.indexOf(email);
    invitedUsers.splice(index, 1);
    _this.closest('div').remove();
  },
  sendInvites: function (url) {
    // Send Invitation to the backend server
    $.ajax({
      url: url,
      type: 'POST',
      data: {
        'userList[]': invitedUsers
      },
      beforeSend: function () {
        $(inviteToSession.config.loader).toggle();
      },
      success: function (resp) {
        inviteToSession.successMessage(resp.response);
      },
      error: function () {
        // On error display message
        inviteToSession.validationError('There was an error with the server');
      },
      complete: function () {
        // Cleanup the div after succesful completion
        $(inviteToSession.config.loader).toggle();
        inviteToSession.cleanUp();
      }
    });
  },
  successMessage: function (result) {
    var sucessHtml = '';
    result.forEach(function (obj) {
      sucessHtml += '<p class="text-' + obj.status + '">' +
      obj.email + ' - ' + obj.message + '</p>';
    });
    return $(inviteToSession.config.inviteDiv).html(sucessHtml);
  },
  validationError: function (message) {
    $(inviteToSession.config.validateDiv).html(message);
  },

  errorMessage: function () {
    return $(inviteToSession.config.inviteDiv).html('<p class="text-danger">' +
            'Some erros where encountered when sending the email</p>');
  },
  cleanUp: function () {
    invitedUsers = [];
    setTimeout(function () {
      $(inviteToSession.config.inviteDiv).html('');
    }, 7000);
  }
};

var deleteSession = {
    init: function(){
     $('body').on('click', '#remove', function (e) {
       e.preventDefault();
       var result = confirm("Are you sure");
       if (result){
         var id_session = $(this).data('id');
       $.ajax({
         url: '/pair/delete/',
         type: 'POST',
         data: {
           session_id: id_session
         },
         success: function (data){
           window.location.reload();
         },
         error: function (){
         }
       })
       }

     })
    }
};

$(document).ready(function () {
  realTime.init();
  inviteToSession.init();

  formPost.init({
    share: '#id_share_form, .commentform'
  });
  ajaxContent.init({
    filter: '#community a,.filter-menu a,#codango-link a'
  });
  editComment.init({
    button: '.edit-comment'
  });

  eventListeners.init();
  mobileNav.init();
  votes.init();
  deleteComment.init();
  deleteSession.init();
  followAction.init({
    button: '#follow-btn,.follow-btn'

  });
  readNotification.init({
    button: '#notifications .list-group-item'
  });

  $('#id-snippet-body').hide();
  $(document).click(function () {
    $('#notifications').hide();
  });
// Endless pagination plugin
  $.endlessPaginate({
    paginateOnScroll: true,
    paginateOnScrollMargin: 20
  });
  prettyPrint();

  $('#session-name').submit(function (e) {
    var data = $(this).serializeArray();
    var _this = $(this);
    e.preventDefault();
    $.ajax({
      url: _this.attr('action'),
      type: 'POST',
      processData: false,
      data: data
    });
  });

  $('body').on('click', '.notification-icon', function (e) {
    e.stopPropagation();
    e.preventDefault();
    $('#notifications').toggle();
  });
});