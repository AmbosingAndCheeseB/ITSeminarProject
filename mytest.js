//TODO: Make es6 class, this is a quick example

var events = document.querySelectorAll('.event');
var eventsWrapper = document.querySelector('.events-wrapper');
var eventsViewPort = document.querySelector('.events-viewport');
var eventsLoadMore = document.querySelector('.events-load-more');
var eventsChunks = _.chunk(events, 9);
var eventLandmarks = getLandmarks(eventsChunks);
var eventLandmarkIndex = 0;
var eventLandmarkIndexMax = eventLandmarks.length - 1;

function getLandmarks($chunks) {
  var landmarks = [];
  for(var $i = 0; $i < $chunks.length; $i++) {
    var chunk = $chunks[$i];
    var landmark = chunk[chunk.length - 1];
    landmarks.push(landmark.offsetTop + landmark.offsetHeight);
  }
  return landmarks;
}

function updateViewportHeight(landmark) {
  eventsViewPort.style.height = landmark + 'px';
}

// Run on initialize
function init() {
  updateViewportHeight(eventLandmarks[eventLandmarkIndex]);
}


function onResize() {
  eventLandmarks = getLandmarks(eventsChunks); // re-fetch landmark locations
  init();
}

init();

eventsLoadMore.addEventListener('click', (e) => {
  eventLandmarkIndex++;
  if(eventLandmarkIndex === eventLandmarkIndexMax) {
    eventsLoadMore.style.display = 'none';
    eventsViewPort.style.height = 'auto';
  } else {                
    updateViewportHeight(eventLandmarks[eventLandmarkIndex]);
  }
});

window.addEventListener('resize', _.debounce(onResize, 200))