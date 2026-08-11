/* Rotary Club of Jurong Town, Singapore
   Two small jobs: the mobile menu, and working out the next meeting date.
   No libraries, nothing to update. */
(function () {

  /* Mobile menu */
  var burger = document.querySelector('.burger');
  var links = document.getElementById('links');
  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* Next meeting: 2nd and 4th Tuesday of the month, 12.50 pm.
     If the club ever changes its meeting pattern, change the numbers below. */
  var target = document.getElementById('nextDate');
  if (!target) return;

  function nthWeekday(year, month, weekday, n) {
    var first = new Date(year, month, 1);
    var offset = (weekday - first.getDay() + 7) % 7;
    return new Date(year, month, 1 + offset + 7 * (n - 1));
  }

  var TUESDAY = 2;
  var now = new Date();
  var candidates = [
    nthWeekday(now.getFullYear(), now.getMonth(), TUESDAY, 2),
    nthWeekday(now.getFullYear(), now.getMonth(), TUESDAY, 4),
    nthWeekday(now.getFullYear(), now.getMonth() + 1, TUESDAY, 2),
    nthWeekday(now.getFullYear(), now.getMonth() + 1, TUESDAY, 4)
  ];

  var months = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'];

  for (var i = 0; i < candidates.length; i++) {
    var meeting = new Date(candidates[i]);
    meeting.setHours(12, 50, 0, 0);
    if (meeting >= now) {
      target.textContent = 'Tuesday ' + meeting.getDate() + ' ' + months[meeting.getMonth()];
      break;
    }
  }
})();
