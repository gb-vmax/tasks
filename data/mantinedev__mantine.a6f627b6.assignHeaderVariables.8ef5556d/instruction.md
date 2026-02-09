# Bug Report

### Describe the bug

When using `AppShell` with a collapsed header, the header offset is not being calculated correctly. The offset should be set to `0px` when the header is collapsed in fixed mode, but instead it's using the actual header height value.

### Reproduction

```jsx
<AppShell
  header={{
    height: 60,
    collapsed: true,
    offset: true
  }}
>
  <AppShell.Header>Header content</AppShell.Header>
  <AppShell.Main>Main content</AppShell.Main>
</AppShell>
```

When the header is collapsed, the main content area doesn't adjust properly because `--app-shell-header-offset` is being set to the header height instead of `0px`.

### Expected behavior

When `header.collapsed` is `true` and mode is `fixed`, the `--app-shell-header-offset` CSS variable should be set to `0px` to properly offset the content area. Currently, the collapsed header still reserves space even though it's visually hidden.

### System Info
- @mantine/core version: 7.x
- Browser: Chrome/Firefox
- OS: Any

---
Repository: /testbed
