"use strict";
const $ = (id) => document.getElementById(id);
const params = new URLSearchParams(location.search);
function validDate(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value || "")) return "";
  const timestamp = Date.parse(value + "T00:00:00Z");
  return Number.isFinite(timestamp) && new Date(timestamp).toISOString().slice(0,10) === value ? value : "";
}
const initialDate = validDate(params.get("date"));
const initialFrom = validDate(params.get("from"));
const initialTo = validDate(params.get("to"));
const state = {
  data: null, topic: params.get("topic") || "all", query: params.get("q") || "",
  onlyNew: params.get("new") === "1", limit: 40,
  dateMode: !initialDate && (initialFrom || initialTo) ? "range" : "day",
  dateFrom: initialDate || initialFrom, dateTo: initialDate ? "" : initialTo,
  period: initialDate || initialFrom || initialTo ? "custom" : (["7","30"].includes(params.get("period")) ? params.get("period") : "all")
};
const shortNames = {quantization:"Quantization",pruning:"Pruning & sparsity",distillation:"Distillation","efficient-training":"Efficient training","attention-kv-cache":"Attention / KV cache","decoding-reasoning":"Decoding / reasoning","llm-systems":"LLM systems","diffusion-acceleration":"Diffusion acceleration","visual-generation":"Visual generation"};
function element(tag, className, text) { const node = document.createElement(tag); if (className) node.className = className; if (text !== undefined) node.textContent = text; return node; }
function link(label, url, className) { const a = element("a", className, label); const parsed = new URL(url, location.href); if (!["https:","http:"].includes(parsed.protocol)) return element("span", className, label); a.href = parsed.href; a.target = "_blank"; a.rel = "noopener noreferrer"; return a; }
function updateUrl() {
  const p = new URLSearchParams();
  if (state.topic !== "all") p.set("topic", state.topic);
  if (state.query) p.set("q", state.query);
  if (state.onlyNew) p.set("new", "1");
  if (state.dateMode === "day" && state.dateFrom) p.set("date", state.dateFrom);
  if (state.dateMode === "range") {
    if (state.dateFrom) p.set("from", state.dateFrom);
    if (state.dateTo) p.set("to", state.dateTo);
  }
  if (["7","30"].includes(state.period)) p.set("period", state.period);
  if ($("sort").value === "updated") p.set("sort", "updated");
  history.replaceState(null, "", location.pathname + (p.size ? "?" + p : "") + location.hash);
}
function syncDateControls() {
  const range = state.dateMode === "range";
  $("date-day").setAttribute("aria-pressed", String(!range));
  $("date-range").setAttribute("aria-pressed", String(range));
  $("date-to-field").hidden = !range;
  $("date-from-label").textContent = range ? "起始日期（可留空）" : "发表日期";
  $("date-from").value = state.dateFrom;
  $("date-to").value = state.dateTo;
  $("clear-date").hidden = !state.dateFrom && !state.dateTo;
  $("period").value = state.period;
}
function applyDateFilter() {
  state.period = state.dateFrom || state.dateTo ? "custom" : "all";
  state.limit = 40;
  syncDateControls(); renderPapers(); updateUrl();
}
function clearDateFilter() {
  state.dateFrom = ""; state.dateTo = ""; state.period = "all";
  syncDateControls();
}
function renderTopics() {
  const topics = [{id:"all",name:"All research"}, ...state.data.topics];
  $("topics").replaceChildren(...topics.map((topic) => {
    const count = topic.id === "all" ? state.data.papers.length : state.data.papers.filter(p => p.topics.includes(topic.id)).length;
    const button = element("button", "topic" + (state.topic === topic.id ? " selected" : ""));
    button.type = "button"; button.setAttribute("aria-pressed", String(state.topic === topic.id));
    button.append(element("span", "", topic.name), element("span", "count", count));
    button.addEventListener("click", () => { state.topic = topic.id; state.limit = 40; renderTopics(); renderPapers(); updateUrl(); });
    return button;
  }));
}
function card(p) {
  const article = element("article", "paper");
  const meta = element("div", "paper-meta"); const date = element("time", "", p.published.slice(0,10)); date.dateTime = p.published; meta.append(date);
  if (p.first_seen === state.data.scan_date) meta.append(element("span", "new-label", "NEWLY INDEXED"));
  const heading = element("h3"); heading.append(link(p.title, p.url));
  const names = p.authors.slice(0,3).join(", ") + (p.authors.length > 3 ? " et al." : "");
  const tags = element("div", "tags"); p.topics.forEach(t => tags.append(element("span", "tag", shortNames[t] || t)));
  const excerpt = p.abstract.length > 220 ? p.abstract.slice(0,220).replace(/\s+\S*$/, "") + "…" : p.abstract;
  const details = element("details"); details.append(element("summary", "", "Read original abstract"), element("p", "", p.abstract));
  if (p.updated.slice(0,10) !== p.published.slice(0,10)) details.append(element("small", "", "Latest revision: " + p.updated.slice(0,10)));
  const links = element("div", "paper-links"); links.append(link("Paper ↗", p.url), link("PDF ↗", p.pdf_url));
  if (p.code_urls.length) links.append(link("Code ↗", p.code_urls[0]));
  links.append(element("span", "id", p.id));
  article.append(meta, heading, element("p", "authors", names), tags, element("p", "excerpt", excerpt), details, links);
  return article;
}
function renderPapers() {
  const words = state.query.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  const days = state.period;
  // Use the scan date as the reference, so an old snapshot never looks newer than it is.
  const cutoff = ["7","30"].includes(days) ? Date.parse(state.data.scan_date + "T23:59:59+08:00") - Number(days) * 86400000 : null;
  const invalidRange = state.dateMode === "range" && state.dateFrom && state.dateTo && state.dateFrom > state.dateTo;
  $("date-error").hidden = !invalidRange;
  ["date-from","date-to"].forEach(id => $(id).setAttribute("aria-invalid", String(Boolean(invalidRange))));
  // Compare the same calendar date shown on each card; both range endpoints are inclusive.
  const matchesDate = p => {
    const date = p.published.slice(0,10);
    if (state.dateMode === "day") return !state.dateFrom || date === state.dateFrom;
    return (!state.dateFrom || date >= state.dateFrom) && (!state.dateTo || date <= state.dateTo);
  };
  const papers = state.data.papers.filter(p => (state.topic === "all" || p.topics.includes(state.topic))
    && !invalidRange && matchesDate(p)
    && (!state.onlyNew || p.first_seen === state.data.scan_date)
    && (cutoff === null || Date.parse(p.published) >= cutoff)
    && words.every(w => (p.title + " " + p.abstract + " " + p.authors.join(" ") + " " + p.id).toLocaleLowerCase().includes(w)));
  const sortKey = $("sort").value;
  papers.sort((a,b) => b[sortKey].localeCompare(a[sortKey]) || b.id.localeCompare(a.id));
  $("papers").replaceChildren(...papers.slice(0,state.limit).map(card));
  $("empty").hidden = papers.length > 0 || Boolean(invalidRange);
  $("more").hidden = papers.length <= state.limit;
  $("more").textContent = "Show more papers (" + (papers.length - state.limit) + " remaining)";
  $("result-count").textContent = invalidRange ? "请调整日期范围" : papers.length.toLocaleString() + " papers · " + Math.min(state.limit,papers.length) + " shown";
  const topic = state.data.topics.find(t => t.id === state.topic);
  $("topic-title").textContent = topic ? topic.name : "All research";
}
async function init() {
  try {
    const response = await fetch("papers.json"); if (!response.ok) throw new Error("Feed unavailable");
    state.data = await response.json();
    if (!state.data.topics.some(t => t.id === state.topic)) state.topic = "all";
    $("total").textContent = state.data.papers.length.toLocaleString();
    $("new-count").textContent = state.data.papers.filter(p => p.first_seen === state.data.scan_date).length.toLocaleString();
    $("updated").textContent = state.data.updated;
    $("newest").textContent = "Newest submission: " + state.data.newest_submission;
    const scanIsToday = new Intl.DateTimeFormat("en-CA", {timeZone:"Asia/Shanghai", year:"numeric",month:"2-digit",day:"2-digit"}).format(new Date()) === state.data.scan_date;
    if (!scanIsToday) {
      $("new-count").nextElementSibling.textContent = "NEWLY INDEXED · " + state.data.scan_date;
      $("only-new").parentElement.lastChild.textContent = " Added on " + state.data.scan_date;
    }
    $("search").value = state.query; $("only-new").checked = state.onlyNew;
    $("sort").value = params.get("sort") === "updated" ? "updated" : "published";
    const dates = state.data.papers.map(p => p.published.slice(0,10)).sort();
    const latestDate = dates[dates.length - 1];
    $("date-info").textContent = dates.length ? "已收录发表日期：" + dates[0] + " — " + latestDate + "；与论文卡片上的日期一致。" : "暂无已收录论文。";
    $("latest-date").disabled = !latestDate;
    syncDateControls();
    renderTopics(); renderPapers();
    let timer;
    $("search").addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => { state.query = $("search").value; state.limit = 40; renderPapers(); updateUrl(); },150); });
    $("only-new").addEventListener("change", () => { state.onlyNew = $("only-new").checked; state.limit = 40; renderPapers(); updateUrl(); });
    $("period").addEventListener("change", () => {
      const period = $("period").value;
      if (period === "custom") {
        state.period = "custom";
        if (!state.dateFrom && !state.dateTo && latestDate) state.dateFrom = latestDate;
      } else {
        clearDateFilter(); state.period = period;
      }
      state.limit = 40; syncDateControls(); renderPapers(); updateUrl();
      if (period === "custom") $("date-from").focus();
    });
    $("sort").addEventListener("change", () => { state.limit = 40; renderPapers(); updateUrl(); });
    $("date-from").addEventListener("change", () => { state.dateFrom = validDate($("date-from").value); applyDateFilter(); });
    $("date-to").addEventListener("change", () => { state.dateTo = validDate($("date-to").value); applyDateFilter(); });
    ["day","range"].forEach(mode => $("date-" + mode).addEventListener("click", () => {
      state.dateMode = mode;
      if (mode === "day") { state.dateFrom = state.dateFrom || state.dateTo; state.dateTo = ""; }
      // An unfinished range stays open-ended until the user chooses its other bound.
      if (state.dateFrom || state.dateTo) applyDateFilter(); else syncDateControls();
    }));
    $("latest-date").addEventListener("click", () => {
      state.dateMode = "day"; state.dateFrom = latestDate; state.dateTo = ""; applyDateFilter();
    });
    $("clear-date").addEventListener("click", () => { clearDateFilter(); state.limit = 40; renderPapers(); updateUrl(); });
    $("more").addEventListener("click", () => { state.limit += 40; renderPapers(); });
    $("reset").addEventListener("click", () => { state.topic = "all"; state.query = ""; state.onlyNew = false; state.limit = 40; $("search").value = ""; $("only-new").checked = false; clearDateFilter(); renderTopics(); renderPapers(); updateUrl(); });
  } catch (error) { $("error").hidden = false; $("result-count").textContent = "Feed unavailable"; $("updated").textContent = "Unable to load"; console.error(error); }
}
init();
