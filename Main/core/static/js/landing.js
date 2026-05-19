/* EventNest Landing Page — Scroll Reveal & Interactions */
(function () {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── Scroll Reveal ─────────────────────────────────────────── */
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    document.querySelectorAll('.reveal').forEach(function (el) {
      observer.observe(el);
    });
  } else {
    /* Immediately show everything for reduced-motion users */
    document.querySelectorAll('.reveal').forEach(function (el) {
      el.classList.add('revealed');
    });
  }

  /* ── Counter animation ─────────────────────────────────────── */
  function animateCounter(el) {
    var target = parseInt(el.getAttribute('data-target'), 10);
    var duration = 1600;
    var start = performance.now();
    function step(now) {
      var progress = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target).toLocaleString() + (el.getAttribute('data-suffix') || '');
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (!reduceMotion && 'IntersectionObserver' in window) {
    var counterObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    document.querySelectorAll('.stat-number[data-target]').forEach(function (el) {
      counterObserver.observe(el);
    });
  } else {
    document.querySelectorAll('.stat-number[data-target]').forEach(function (el) {
      el.textContent = parseInt(el.getAttribute('data-target'), 10).toLocaleString() + (el.getAttribute('data-suffix') || '');
    });
  }

  /* ── Smooth scroll for hero CTAs ───────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
      }
    });
  });
})();
