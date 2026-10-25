(() => {
  const list = document.getElementById("category-articles");
  const size = document.getElementById("category-page-size");
  const count = document.getElementById("category-result-count");
  if (!list || !size || !count) return;
  const cards = [...list.querySelectorAll(".article-card")];
  const navs = [
    document.getElementById("category-pagination-top"),
    document.getElementById("category-pagination-bottom")
  ].filter(Boolean);
  let page = 1;
  const render = () => {
    const pageSize = Number(size.value) || 10;
    const total = cards.length;
    const pages = Math.max(1, Math.ceil(total / pageSize));
    page = Math.min(Math.max(1, page), pages);
    cards.forEach((card, i) => {
      card.hidden = i < (page - 1) * pageSize || i >= page * pageSize;
    });
    count.textContent = total
      ? "全" + total + "件中 " + ((page - 1) * pageSize + 1) + "〜" + Math.min(page * pageSize, total) + "件を表示"
      : "該当する記事はありません";
    navs.forEach(nav => {
      nav.replaceChildren();
      nav.hidden = pages <= 1;
      if (pages <= 1) return;
      const add = (label, target, disabled = false, current = false) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "category-page-button";
        button.textContent = label;
        button.disabled = disabled;
        if (current) button.setAttribute("aria-current", "page");
        button.addEventListener("click", () => {
          page = target;
          render();
          document.querySelector("h1")?.scrollIntoView({ behavior: "auto", block: "start" });
        });
        nav.append(button);
      };
      add("前へ", page - 1, page === 1);
      let first = Math.max(1, page - 2);
      let last = Math.min(pages, first + 4);
      first = Math.max(1, last - 4);
      if (first > 1) {
        add("1", 1, false, page === 1);
        if (first > 2) {
          const dots = document.createElement("span");
          dots.className = "category-page-status";
          dots.textContent = "…";
          nav.append(dots);
        }
      }
      for (let n = first; n <= last; n++) add(String(n), n, false, page === n);
      if (last < pages) {
        if (last < pages - 1) {
          const dots = document.createElement("span");
          dots.className = "category-page-status";
          dots.textContent = "…";
          nav.append(dots);
        }
        add(String(pages), pages, false, page === pages);
      }
      add("次へ", page + 1, page === pages);
      const status = document.createElement("span");
      status.className = "category-page-status";
      status.textContent = page + " / " + pages + "ページ";
      nav.append(status);
    });
  };
  size.addEventListener("change", () => {
    page = 1;
    render();
  });
  render();
})();