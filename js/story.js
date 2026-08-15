document.addEventListener('DOMContentLoaded', function () {
  var storyEl = document.querySelector('.story-scroll');
  if (!storyEl) return;

  var panels = Array.prototype.slice.call(storyEl.querySelectorAll('.story-panel'));
  var dots = Array.prototype.slice.call(storyEl.querySelectorAll('.story-progress span'));
  var svgStages = Array.prototype.slice.call(storyEl.querySelectorAll('.story-svg .st'));

  function setActive(stage) {
    storyEl.setAttribute('data-active', stage);
    panels.forEach(function (p) {
      var s = parseInt(p.dataset.stage, 10);
      p.classList.toggle('active', s === stage);
    });
    dots.forEach(function (d, i) {
      d.classList.toggle('on', i === stage);
    });
    svgStages.forEach(function (g) {
      var s = parseInt(g.dataset.stage, 10);
      g.classList.toggle('on', s === stage);
    });
  }

  // Tie the description text to the illustration: hovering a tag
  // highlights the matching piece of the current stage's artwork.
  var tagEls = Array.prototype.slice.call(storyEl.querySelectorAll('.story-tags span.linkable'));
  tagEls.forEach(function (tag) {
    var link = tag.dataset.link;
    function on() {
      tag.classList.add('tag-hot');
      var stageEl = storyEl.querySelector('.story-svg .st.on');
      if (!stageEl) return;
      var targets = stageEl.querySelectorAll('[data-link="' + link + '"]');
      targets.forEach(function (t) { t.classList.add('linked-hot'); });
    }
    function off() {
      tag.classList.remove('tag-hot');
      storyEl.querySelectorAll('.linked-hot').forEach(function (t) {
        t.classList.remove('linked-hot');
      });
    }
    tag.addEventListener('mouseenter', on);
    tag.addEventListener('mouseleave', off);
    tag.addEventListener('touchstart', on, { passive: true });
    tag.addEventListener('touchend', off);
  });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
          setActive(parseInt(entry.target.dataset.stage, 10));
        }
      });
    }, { threshold: [0, 0.5, 1] });
    panels.forEach(function (p) { io.observe(p); });
    setActive(0); // initial state before first intersection fires
  } else {
    setActive(0);
    panels.forEach(function (p) { p.classList.add('active'); });
  }
});
