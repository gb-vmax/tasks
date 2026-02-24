You are automating part of a server provisioning workflow for an infrastructure engineering team. Your task is to set up a standardized directory structure for configuration management and provide a verifiable report in a specific format. Follow these requirements:

1. Create a directory at /home/user/provisioning/configs.
2. Within /home/user/provisioning/configs, create three regular files named web.conf, db.conf, and cache.conf. Each file should contain a single line with its respective name in uppercase, for example, WEB.CONF in web.conf.
3. In /home/user/provisioning/, create a directory named active.
4. Inside /home/user/provisioning/active, create symbolic links to the config files as follows:
   - Link named web_active.conf pointing to /home/user/provisioning/configs/web.conf
   - Link named db_active.conf pointing to /home/user/provisioning/configs/db.conf
   - Link named cache_active.conf pointing to /home/user/provisioning/configs/cache.conf
   All symlinks should be relative (not absolute) so they remain valid if /home/user/provisioning is moved.
5. Create a plain text report at /home/user/provisioning/symlink_report.txt. This report must contain exactly three lines, one per symlink, in the following comma-separated format:

   <symlink_name>,<relative_target>,<link_target_content_line>

   For example, for web_active.conf, the line should look like:
   web_active.conf,../configs/web.conf,WEB.CONF

   The order of the lines must be web_active.conf, db_active.conf, then cache_active.conf.

The automated test will check:
- The existence and content of all files and directories as specified.
- That the symlinks are present, are relative, and point to the correct targets.
- That symlink_report.txt has the correct lines, in the correct order, with correct file content values.
