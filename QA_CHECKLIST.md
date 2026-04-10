# QA Regression Checklist

## Functional Smoke

- [ ] Run `npm test`
- [ ] Open `ui/index.html` and verify page renders
- [ ] Click action button and verify:
- [ ] Alert appears
- [ ] Status text updates

## Browser Matrix

- [ ] Chrome (latest stable)
- [ ] Edge (latest stable)
- [ ] Firefox (latest stable)

## Accessibility Basics

- [ ] Interactive button is keyboard focusable
- [ ] Status update is visible after action
- [ ] No obvious console errors on load/click

## Release Gate

- [ ] QA sign-off recorded in PR comment
- [ ] Product/boss sign-off recorded in PR comment
