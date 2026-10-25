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

  function addControls() {
    if (document.getElementById("ia-display-toggle")) return;

    var style = document.createElement("style");
    style.textContent =
      ".ia-footer-tools{display:flex;justify-content:flex-end;align-items:center;gap:12px;margin:18px auto 0;padding:12px 0;font:12px/1.5 system-ui,-apple-system,sans-serif;color:#647887}" +
      "#ia-display-toggle{border:0;padding:3px 0;background:transparent;color:inherit;font:inherit;text-decoration:underline;text-underline-offset:3px;cursor:pointer}" +
      "#ia-display-toggle:hover{color:#176d65}" +
      "#ia-display-toggle:focus-visible,#ia-back-to-top:focus-visible{outline:3px solid #ffb58d;outline-offset:3px}" +
      "#ia-back-to-top{position:fixed;z-index:9999;right:14px;bottom:14px;width:42px;height:42px;border:1px solid #b8d8d9;border-radius:50%;background:#10243a;color:#fff;font:700 23px/1 system-ui,-apple-system,sans-serif;box-shadow:0 2px 10px #10243a30;cursor:pointer;display:grid;place-items:center}" +
      "#ia-back-to-top:hover{background:#176d65}" +
      "@media print{.ia-footer-tools,#ia-back-to-top{display:none!important}}";
    document.head.appendChild(style);

    var footer = document.querySelector("footer");
    if (!footer) {
      footer = document.createElement("footer");
      document.body.appendChild(footer);
    }
    var footerTools = document.createElement("div");
    footerTools.className = "ia-footer-tools";
    var toggle = document.createElement("button");
    toggle.id = "ia-display-toggle";
    toggle.type = "button";
    toggle.textContent = mode === "desktop" ? "スマホ表示に戻す" : "PC表示に切替";
    toggle.setAttribute("aria-label", toggle.textContent);
    toggle.addEventListener("click", function () {
      var next = mode === "desktop" ? "mobile" : "desktop";
      try { localStorage.setItem(KEY, next); } catch (e) {}
      applyViewport(next);
      window.location.reload();
    });
    footerTools.appendChild(toggle);
    footer.appendChild(footerTools);

    var topButton = document.createElement("button");
    topButton.id = "ia-back-to-top";
    topButton.type = "button";
    topButton.textContent = "↑";
    topButton.setAttribute("aria-label", "ページの先頭へ戻る");
    topButton.title = "ページの先頭へ戻る";
    topButton.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    document.body.appendChild(topButton);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addControls, { once: true });
  } else {
    addControls();
  }
})();