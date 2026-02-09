# Bug Report

### Describe the bug

When running rollup in watch mode with a config file, I'm getting duplicate warning messages appearing in the console. It seems like warning handlers are accumulating instead of being properly cleaned up between config reloads.

### Reproduction

1. Create a rollup config file (e.g., `rollup.config.js`)
2. Run rollup in watch mode: `rollup -c -w`
3. Make a change to the config file to trigger a reload
4. Observe that warning messages start appearing multiple times

Each time the config file reloads, the warnings seem to multiply. After a few reloads, the same warning can appear 3-4 times in the console.

### Expected behavior

Warning messages should only appear once, regardless of how many times the config file has been reloaded in watch mode.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
