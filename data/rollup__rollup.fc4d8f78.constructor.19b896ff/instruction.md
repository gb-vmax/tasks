# Bug Report

### Issue with plugin context initialization when using basePluginDriver

I'm encountering an issue where plugin contexts aren't being created correctly when a basePluginDriver is provided. It seems like the plugin contexts are only being generated for plugins from the base driver, but not for the newly added user plugins.

### Reproduction

When creating a new PluginDriver with a basePluginDriver:

```js
const baseDriver = new PluginDriver(graph, options, basePlugins, cache);
const outputDriver = new PluginDriver(graph, outputOptions, outputPlugins, cache, baseDriver);
```

The `outputDriver` only has plugin contexts for the `basePlugins`, not for the `outputPlugins` that were passed in. This causes issues when trying to execute hooks on the output plugins since they don't have proper contexts initialized.

### Expected behavior

All plugins (both from the base driver and the new user plugins) should have their contexts properly initialized in the pluginContexts Map. The new driver should be able to execute hooks on all its plugins.

### Additional context

This appears to affect the output phase of the build process where output plugins need to have their own contexts but are inheriting from an input plugin driver.

---
Repository: /testbed
