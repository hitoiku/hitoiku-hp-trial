document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('open');
      nav.classList.toggle('open');
    });
  }

  // Mobile dropdown accordion (サービス)
  document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 980) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // Close mobile nav on link click
  document.querySelectorAll('.main-nav .dropdown a, .main-nav > ul > li > a:not(.has-dropdown > a)').forEach(function (link) {
    link.addEventListener('click', function () {
      if (window.innerWidth <= 980) {
        toggle.classList.remove('open');
        nav.classList.remove('open');
      }
    });
  });

  // Scroll reveal
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
    // Safety net: ensure content is never permanently invisible
    // (covers crawlers / tools that don't simulate scrolling).
    setTimeout(function () {
      revealEls.forEach(function (el) { el.classList.add('in'); });
    }, 2500);
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  // About teaser: slide the diagonal green bands into place (shape-a
  // down from above, shape-b up from below) every time the section
  // scrolls into view -- and reset when it scrolls back out, so the
  // animation replays each time rather than only once.
  var aboutTeaser = document.querySelector('.about-teaser');
  if (aboutTeaser) {
    if ('IntersectionObserver' in window) {
      var teaserIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          aboutTeaser.classList.toggle('in-view', entry.isIntersecting);
        });
      }, { threshold: 0.25 });
      teaserIo.observe(aboutTeaser);
    } else {
      aboutTeaser.classList.add('in-view');
    }
  }

  // Slide-in-from-the-left text (e.g. the big "Our Services" label):
  // replays every time each element scrolls into view.
  var slideLeftEls = document.querySelectorAll('.slide-in-left');
  if (slideLeftEls.length) {
    if ('IntersectionObserver' in window) {
      var slideLeftIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          entry.target.classList.toggle('in-view', entry.isIntersecting);
        });
      }, { threshold: 0.4 });
      slideLeftEls.forEach(function (el) { slideLeftIo.observe(el); });
    } else {
      slideLeftEls.forEach(function (el) { el.classList.add('in-view'); });
    }
  }

  // Plain fade entrance (e.g. the stat rings): replays every time the
  // element scrolls into view.
  var fadeEls = document.querySelectorAll('.fade-in-scroll');
  if (fadeEls.length) {
    if ('IntersectionObserver' in window) {
      var fadeIo = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          entry.target.classList.toggle('in-view', entry.isIntersecting);
        });
      }, { threshold: 0.3 });
      fadeEls.forEach(function (el) { fadeIo.observe(el); });
    } else {
      fadeEls.forEach(function (el) { el.classList.add('in-view'); });
    }
  }

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq-item');
      var wasOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.faq-item.open').forEach(function (o) {
        if (o !== item) o.classList.remove('open');
      });
      item.classList.toggle('open', !wasOpen);
    });
  });

  // FAQ tab filter
  var tabs = document.querySelectorAll('.tab-btn');
  if (tabs.length) {
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        tabs.forEach(function (t) { t.classList.remove('active'); });
        tab.classList.add('active');
        var cat = tab.dataset.cat;
        document.querySelectorAll('.faq-item').forEach(function (item) {
          item.style.display = (cat === 'all' || item.dataset.cat === cat) ? '' : 'none';
        });
      });
    });
  }

  // Active nav link highlight
  var path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === path) a.classList.add('active');
  });

  // About page: Mission / Vision / Company Overview subnav tabs -- only
  // the selected tab's content is visible at a time (the other panels,
  // and the Company Overview section entirely, are hidden) so switching
  // tabs never leaves unrelated content peeking into view.
  var aboutSubnavTabs = document.querySelectorAll('.about-subnav-item[data-panel]');
  if (aboutSubnavTabs.length) {
    var aboutPanels = document.querySelectorAll('.mv-item[data-panel]');
    var missionSection = document.getElementById('mission');
    var companySection = document.getElementById('company');
    var arrowDown = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg>';
    var arrowRight = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
    aboutSubnavTabs.forEach(function (tab) {
      tab.addEventListener('click', function (e) {
        e.preventDefault();
        var target = tab.dataset.panel;
        aboutPanels.forEach(function (panel) { panel.hidden = panel.dataset.panel !== target; });
        if (missionSection) missionSection.hidden = target === 'company';
        if (companySection) companySection.hidden = target !== 'company';
        aboutSubnavTabs.forEach(function (t) {
          var isActive = t === tab;
          t.classList.toggle('active', isActive);
          var arrow = t.querySelector('.subnav-arrow');
          if (arrow) arrow.innerHTML = isActive ? arrowDown : arrowRight;
        });
        var section = target === 'company' ? companySection : missionSection;
        if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        var shown = target === 'company' ? companySection : document.querySelector('.mv-item[data-panel="' + target + '"]');
        if (shown) {
          shown.classList.remove('about-panel-fade');
          void shown.offsetWidth;
          shown.classList.add('about-panel-fade');
        }
      });
    });
  }

  // About page: "詳しく読む" / "すべて見る" buttons expand extra content
  // in place instead of navigating to message.html.
  document.querySelectorAll('.message-toggle').forEach(function (btn) {
    var fulls = btn.parentElement.querySelectorAll('.message-full');
    if (!fulls.length) return;
    var label = btn.querySelector('.message-toggle-label');
    var openLabel = label ? label.textContent : '';
    btn.addEventListener('click', function () {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
      fulls.forEach(function (el) { el.hidden = expanded; });
      if (label) label.textContent = expanded ? openLabel : '閉じる';
    });
  });
});
