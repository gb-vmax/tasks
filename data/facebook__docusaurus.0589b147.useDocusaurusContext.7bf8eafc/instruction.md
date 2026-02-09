# Bug Report

### Describe the bug

The `useDocusaurusContext()` hook is returning stale/cached context data instead of the current context values. When the context updates during runtime (e.g., theme changes, locale switches, or other dynamic updates), components using this hook don't receive the updated values and continue to use the initial cached data.

### Reproduction

```jsx
function MyComponent() {
  const {siteConfig, i18n} = useDocusaurusContext();
  
  // Initially shows correct locale
  console.log(i18n.currentLocale); // 'en'
  
  // After switching locale via the locale dropdown
  // The component still shows 'en' instead of the new locale
  // Even though the context provider has updated values
  
  return <div>{i18n.currentLocale}</div>;
}
```

Steps to reproduce:
1. Create a component that uses `useDocusaurusContext()`
2. Display some context value (like current locale or theme)
3. Trigger a context update (switch theme/locale)
4. The displayed value doesn't update, shows the initial cached value

### Expected behavior

The hook should return the current context values from the React Context provider, not cached values. When the context updates, all components using `useDocusaurusContext()` should receive the new values and re-render accordingly.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome/Firefox

This seems to have started recently. The context values should be live and reactive, not cached across renders.

---
Repository: /testbed
