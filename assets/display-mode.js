(function () {
  "use strict";
  var KEY = "ia-display-mode";
  var viewport = document.querySelector('meta[name="viewport"]');
  var mode = "mobile";
  try {
    mode = localStorage.getItem(KEY) === "desktop" ? "desktop" : "mobile";
  } catch (e) {}
  function applyViewport(value) {
    if (!viewport) {
      viewport = document.createElement("meta");
      viewport.name = "viewport";
      document.head.appendChild(viewport);
    }
    viewport.setAttribute("content", value === "desktop"
      ? "width=1024, initial-scale=1"
      : "width=device-width, initial-scale=1");
  }
  applyViewport(mode);

  function addToggle() {
    if (document.getElementById("ia-display-toggle")) return;
    var style = document.createElement("style");
    style.textContent = "#ia-display-toggle{position:fixed;z-index:9999;right:12px;bottom:12px;border:1px solid #b8d8d9;border-radius:999px;padding:10px 14px;background:#10243a;color:#fff;font:700 14px/1.2 system-ui,-apple-system,sans-serif;box-shadow:0 3px 14px #10243a35;cursor:pointer}#ia-display-toggle:focus-visible{outline:3px solid #ffb58d;outline-offset:3px}@media print{#ia-display-toggle{display:none}}";
    document.head.appendChild(style);
    var button = document.createElement("button");
    button.id = "ia-display-toggle";
    button.type = "button";
    button.textContent = mode === "desktop" ? "スマホ表示に戻す" : "PC表示に切替";
    button.setAttribute("aria-label", button.textContent);
    button.addEventListener("click", function () {
      var next = mode === "desktop" ? "mobile" : "desktop";
      try { localStorage.setItem(KEY, next); } catch (e) {}
      applyViewport(next);
      window.location.reload();
    });
    document.body.appendChild(button);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addToggle, { once: true });
  } else {
    addToggle();
  }
})();