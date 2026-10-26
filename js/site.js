(function () {
  "use strict";

  /* reveal on scroll */
  var reveal = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.08 });
    reveal.forEach(function (el) { io.observe(el); });
  } else {
    reveal.forEach(function (el) { el.classList.add("in"); });
  }

  /* highlight the nav link for the section in view */
  var links = Array.prototype.slice.call(document.querySelectorAll(".links a"));
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  function mark(id) {
    links.forEach(function (a) {
      if (a === byId[id]) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
  }
  if ("IntersectionObserver" in window) {
    var visible = {};
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
      var current = "";
      Object.keys(byId).forEach(function (id) { if (visible[id]) current = id; });
      mark(current);
    }, { rootMargin: "-35% 0px -60% 0px" });
    Object.keys(byId).forEach(function (id) {
      var s = document.getElementById(id);
      if (s) spy.observe(s);
    });
  }

  /* practicals: open on mouse hover, or pin open with a click, tap or keyboard */
  document.querySelectorAll(".rep").forEach(function (rep) {
    var head = rep.querySelector(".rep-h");
    var hovered = false, pinned = false;
    function sync() {
      var open = hovered || pinned;
      rep.classList.toggle("open", open);
      head.setAttribute("aria-expanded", open ? "true" : "false");
    }
    head.addEventListener("click", function () { pinned = !pinned; sync(); });
    rep.addEventListener("pointerenter", function (e) { if (e.pointerType === "mouse") { hovered = true; sync(); } });
    rep.addEventListener("pointerleave", function (e) { if (e.pointerType === "mouse") { hovered = false; sync(); } });
  });

  /* copy the email address */
  var copy = document.getElementById("copy");
  var status = document.getElementById("copy-status");
  var addr = document.getElementById("addr");
  if (copy && addr) {
    copy.addEventListener("click", function () {
      function done() { status.textContent = "Address copied"; copy.textContent = "Copied"; setTimeout(function () { copy.textContent = "Copy Address"; status.textContent = ""; }, 1800); }
      function select() {
        var r = document.createRange(); r.selectNodeContents(addr);
        var s = getSelection(); s.removeAllRanges(); s.addRange(r);
        status.textContent = "Address selected, press Ctrl+C to copy";
      }
      try { navigator.clipboard.writeText(addr.textContent).then(done, select); } catch (err) { select(); }
    });
  }

  /* remove the intro overlay once it has finished */
  var intro = document.getElementById("intro");
  if (intro) intro.addEventListener("animationend", function (e) { if (e.animationName === "introOut") intro.remove(); });
})();
