document.addEventListener("DOMContentLoaded", function() {

  // Global variables to hold the reference to the template row that we can clone
  var theTemplate = document.querySelector('.template-row');
  var theTable = document.querySelector("table tbody");

  // Helper function to inject a new row into the table
  function injectTableRow(actor) {
    let theTable = document.querySelector("table tbody");
    let theRow = theTable.insertRow();

    theRow.insertCell().innerHTML = actor['id'];
    theRow.insertCell().innerHTML = actor['first_name'];
    theRow.insertCell().innerHTML = actor['last_name'];
    theRow.insertCell().innerHTML = "<a href='/actor/"+actor['id']+"'>"+actor['email']+"</a>";
    theRow.insertCell().innerHTML = actor['age'];
  }

  // Function to make a REST call and retrieve a single actor instance
  function getActor(actorId) {
    theRequest = '/actor/' + actorId;
    fetch(theRequest)
    .then(response => response.json())
    .then(actor => injectTableRow(actor));
  }

  // Function to make a REST call and retrieve a collection of actors
  function getActors() {
    theRequest = '/actors';
    fetch(theRequest)
    .then(response => response.json())
    .then(function(actors) {
      for (const key in actors) {
        injectTableRow(actors[key]);
      }
    });
  }

  // Demo #1: Retrieve all actors and inject them into the table using the helper function
  getActors();

  // Demo #2: Retrieve each actor individually and inject them one at a time with a slight delay
  for (let i=1; i<5; i++) {
    setTimeout(function(){getActor(i); }, 500*i);
  }

});
