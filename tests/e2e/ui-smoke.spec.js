const path = require("path");
const { test, expect } = require("@playwright/test");

test("UI smoke: page loads and action button exists", async ({ page }) => {
  const filePath = path.resolve(__dirname, "../../ui/index.html");
  await page.goto(`file://${filePath}`);

  await expect(page.locator("h1.title")).toBeVisible();
  await expect(page.locator("#action-btn")).toBeVisible();
});
