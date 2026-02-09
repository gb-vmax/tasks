# Bug Report

### Describe the bug

When using spotlight with grouped actions, only the first action from each group is being displayed instead of all actions within the group. This causes most of the actions to be missing from the spotlight search results.

### Reproduction

```js
const actions = [
  {
    group: 'Navigation',
    actions: [
      { id: 'home', label: 'Home' },
      { id: 'about', label: 'About' },
      { id: 'contact', label: 'Contact' }
    ]
  },
  {
    group: 'Settings',
    actions: [
      { id: 'profile', label: 'Profile' },
      { id: 'preferences', label: 'Preferences' }
    ]
  }
];

// When opening spotlight with these actions, only 'Home' and 'Profile' appear
// The other actions ('About', 'Contact', 'Preferences') are missing
```

### Expected behavior

All actions from each group should be displayed in the spotlight, not just the first one from each group.

### System Info
- @mantine/spotlight version: latest
- Browser: Chrome

---
Repository: /testbed
