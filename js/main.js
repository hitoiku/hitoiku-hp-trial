document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    var closeNav = function () {
      toggle.classList.remove('open');
      nav.classList.remove('is-visible');
      document.body.classList.remove('nav-open');
      var onEnd = function (e) {
        if (e.target === nav && e.propertyName === 'transform') {
          nav.classList.remove('open');
          nav.removeEventListener('transitionend', onEnd);
        }
      };
      nav.addEventListener('transitionend', onEnd);
    };
    var openNav = function () {
      toggle.classList.add('open');
      nav.classList.add('open');
      document.body.classList.add('nav-open');
      void nav.offsetWidth; // force reflow so the transform transition still animates in
      nav.classList.add('is-visible');
    };
    toggle.addEventListener('click', function () {
      if (nav.classList.contains('is-visible')) { closeNav(); } else { openNav(); }
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
        closeNav();
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

  // About page: Management Philosophy (Mission + Vision together) / Company
  // Overview subnav tabs -- only the selected tab's section is visible at a
  // time, so switching tabs never leaves unrelated content peeking into view.
  var aboutSubnavTabs = document.querySelectorAll('.about-subnav-item[data-panel]');
  if (aboutSubnavTabs.length) {
    var missionSection = document.getElementById('mission');
    var companySection = document.getElementById('company');
    var valuesSection = document.getElementById('about-values');
    var arrowDown = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg>';
    var arrowRight = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
    var activateAboutTab = function (target, scroll) {
      var tab = Array.prototype.filter.call(aboutSubnavTabs, function (t) { return t.dataset.panel === target; })[0];
      if (!tab) return;
      if (missionSection) missionSection.hidden = target === 'company';
      if (valuesSection) valuesSection.hidden = target === 'company';
      if (companySection) companySection.hidden = target !== 'company';
      aboutSubnavTabs.forEach(function (t) {
        var isActive = t === tab;
        t.classList.toggle('active', isActive);
        var arrow = t.querySelector('.subnav-arrow');
        if (arrow) arrow.innerHTML = isActive ? arrowDown : arrowRight;
      });
      var section = target === 'company' ? companySection : missionSection;
      if (section) {
        if (scroll) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        section.classList.remove('about-panel-fade');
        void section.offsetWidth;
        section.classList.add('about-panel-fade');
      }
    };
    aboutSubnavTabs.forEach(function (tab) {
      tab.addEventListener('click', function (e) {
        e.preventDefault();
        activateAboutTab(tab.dataset.panel, true);
      });
    });
    // Deep-link support: activate the right tab when arriving via a hash
    // link (e.g. the header dropdown's "about.html#company"), both on
    // initial load and on same-page hash navigation.
    var applyHashTab = function () {
      var hash = window.location.hash.replace('#', '');
      if (hash === 'company' || hash === 'vision') {
        activateAboutTab('company', false);
      } else if (hash === 'mission') {
        activateAboutTab('mission', false);
      }
    };
    applyHashTab();
    window.addEventListener('hashchange', applyHashTab);
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

// Tag blocks that contain a deliberate (desktop) <br> so narrow-screen CSS can
// balance the wrapped lines of each segment instead of leaving short orphans.
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('p,li,td,h1,h2,h3,h4').forEach(function (el) {
    if (el.querySelector('br:not(.mobile-only)')) el.classList.add('has-br');
  });
});

// Phrase-aware line breaking for Japanese on tablet / phone widths.
// word-break:keep-all stops mid-word splits but makes long punctuation-less
// runs unbreakable, so the overflow fallback can strand a lone 。 on its own
// line. BudouX (Google) splits text into natural phrases; we add zero-width
// break opportunities between them so wrapping happens at phrase boundaries.
// Applied at <=900px only (desktop wrapping is untouched) and silently
// skipped if the library can't load -- the CSS-only behaviour remains.
(function () {
  var mq = window.matchMedia('(max-width: 900px)');
  var originals = new Map();
  var parser = null;
  var loading = false;
  var SKIP = 'script,style,noscript,textarea,input,select,svg,.intro-splash,[data-no-phrase]';

  function textNodes() {
    var list = [];
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!/[぀-ヿ一-鿿]/.test(n.nodeValue)) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement;
        if (!p || p.closest(SKIP)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    while (walker.nextNode()) list.push(walker.currentNode);
    return list;
  }

  // Clause-first wrapping, like the desktop layout: text is kept whole between
  // 、/。 and only a clause too wide for its line gets phrase-level breaks.
  function blockWidth(el) {
    while (el && getComputedStyle(el).display === 'inline') el = el.parentElement;
    if (!el) return 0;
    var cs = getComputedStyle(el);
    return el.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  }

  function apply() {
    if (!parser) return;
    textNodes().forEach(function (n) {
      if (originals.has(n)) return;
      var text = n.nodeValue;
      var fs = parseFloat(getComputedStyle(n.parentElement).fontSize) || 16;
      var width = blockWidth(n.parentElement);
      var clauses = text.match(/[^、。，．！？]+[、。，．！？」』）]*|[、。，．！？」』）]+/g) || [text];
      var out = clauses.map(function (c) {
        var parts = c.length * fs <= width ? [c] : parser.parse(c);
        return parts.join('​');
      }).join('');
      if (out === text) return;
      originals.set(n, text);
      n.nodeValue = out;
    });
  }

  function revert() {
    originals.forEach(function (text, n) { if (n.parentNode) n.nodeValue = text; });
    originals.clear();
  }

  function sync() {
    if (!mq.matches) { revert(); return; }
    if (parser) { apply(); return; }
    if (loading) return;
    loading = true;
    import('https://cdn.jsdelivr.net/npm/budoux@0.6.4/module/index.js').then(function (m) {
      parser = m.loadDefaultJapaneseParser();
      if (mq.matches) apply();
    }).catch(function () { /* CSS fallback stays in effect */ });
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(sync);
  } else {
    window.addEventListener('load', sync);
  }
  if (mq.addEventListener) mq.addEventListener('change', sync); else mq.addListener(sync);
  var resizeTimer = null;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      if (!mq.matches || !parser) return;
      revert();
      apply();
    }, 200);
  });
})();
