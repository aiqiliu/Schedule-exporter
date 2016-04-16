/**
  * Class Schedule to ICS File Exporter
  * (c) 2016 Aiqi Liu
  *
  * Get ICS files for university class schedules in Oracle PeopleSoft systems 
**/

$(function() {
  // Timezone for tool.
  var timezone = 'America/Chicago';

  //locate to the course boxes
  $('.PSGROUPBOXWBO').each(function() {
      //get course name
      var courseName = $(this).find("PAGROUPDIVIDER").text();
      console.log(courseName);



  })
 })