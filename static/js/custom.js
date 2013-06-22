// JavaScript Document

//Close button for information
$(function(){
  $('.notification').hide().append('<span class="close"><img src="/static/img/mes_close.png" alt="close" class="png_bg" /></span>').fadeIn('slow');
  $('.notification .close').click(function() {
    $(this).parent().fadeOut('slow', function() { $(this).remove(); });
  });
});

// Settings tab layout :
$(function(){
  $('.box .boxContent div.tab-content').hide(); // Hide the content divs
  $('ul.boxTabs li a.default-tab').addClass('current'); // Add the class "current" to the default tab
  $('.boxContent div.default-tab').show(); // Show the div with class "default-tab"
  
  $('.box ul.boxTabs li a').click( // When a tab is clicked...
    function() { 
      $(this).parent().siblings().find("a").removeClass('current'); // Remove "current" class from all tabs
      $(this).addClass('current'); // Add class "current" to clicked tab
      var currentTab = $(this).attr('href'); // Set variable "currentTab" to the value of href of clicked tab
      $(currentTab).siblings().hide(); // Hide all content divs
      $(currentTab).show(); // Show the content div with the id equal to the id of clicked tab
      return false; 
    }
  );
});

//data input
//Settings date picker
$(function() {
  $($.date_input.initialize);
});

//droppy
//Settings Pull-down navigation 
$(function(){
  $('.navi').droppy({trigger: 'click'});
});

//table
//table sort
// $(function(){
//   $(".sort1").tablesorter({
//     //Case sort：Granted only to the class even rows 
//     widgets: ['zebra'],
//     //Zero and Fifth is not sorted 
//     headers: {
//       0: {
//         sorter: false
//       },
//       5: {
//         sorter: false
//       }
//     }
//   });
// }); 

$(function() {
    var zIndexNumber = 1000;
    $('div.header').each(function() {
        $(this).css('zIndex', zIndexNumber);
        zIndexNumber -= 10;
    });
});
