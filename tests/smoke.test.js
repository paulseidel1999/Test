const fs = require("fs");
const path = require("path");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

const root = path.resolve(__dirname, "..");
const htmlPath = path.join(root, "ui", "index.html");
const cssPath = path.join(root, "ui", "style.css");
const jsPath = path.join(root, "ui", "script.js");

assert(fs.existsSync(htmlPath), "Missing ui/index.html");
assert(fs.existsSync(cssPath), "Missing ui/style.css");
assert(fs.existsSync(jsPath), "Missing ui/script.js");

const html = fs.readFileSync(htmlPath, "utf8");
const script = fs.readFileSync(jsPath, "utf8");

assert(html.includes('id="action-btn"'), "Missing action button in ui/index.html");
assert(script.includes("action-btn"), "Missing action button hookup in ui/script.js");
assert(script.includes("addEventListener"), "Missing click handler in ui/script.js");

console.log("Smoke test passed.");
