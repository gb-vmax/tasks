# Bug Report

### Describe the bug

When using the `Tabs` component, the tabs are not functioning correctly. The tab content doesn't update when clicking on different tabs, and the active tab state is not being tracked properly.

### Reproduction

```jsx
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="apple" label="Apple">
    This is an apple 🍎
  </TabItem>
  <TabItem value="orange" label="Orange">
    This is an orange 🍊
  </TabItem>
  <TabItem value="banana" label="Banana">
    This is a banana 🍌
  </TabItem>
</Tabs>
```

### Expected behavior

- Clicking on different tabs should switch the visible content
- The active tab should be highlighted
- Tab selection state should be maintained

### Actual behavior

The tabs render but clicking them doesn't switch the content. The active state is not being managed and all tab content appears to be broken.

### System Info

- Docusaurus version: latest
- Theme: @docusaurus/theme-classic
- Browser: Chrome/Firefox

---
Repository: /testbed
