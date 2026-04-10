const path = require("path");
const { test, expect } = require("@playwright/test");

test("UI smoke: page loads and action button exists", async ({ page }) => {
  const filePath = path.resolve(__dirname, "../../ui/index.html");
  await page.goto(`file://${filePath}`);

  await expect(page.locator("h1.title")).toBeVisible();
  const actionButton = page.locator("#action-btn");
  const statusMessage = page.locator("#status-msg");
  await expect(actionButton).toBeVisible();

  let dialogMessage = "";
  page.once("dialog", async (dialog) => {
    dialogMessage = dialog.message();
    await dialog.accept();
  });

  await actionButton.click();
  await expect(statusMessage).toHaveText("Aktion erfolgreich ausgefuehrt.");
  expect(dialogMessage).toBe("Aktion ausgefuehrt!");
});
