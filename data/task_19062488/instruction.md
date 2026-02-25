As a site reliability engineer, you have received an updated version of a website status page template, and you need to check what has changed from the previous version. 

Your tasks are as follows:

1. In the directory <code>/home/user/uptime_check/</code>, you will find two files: <code>status_page_v1.html</code> (the original template) and <code>status_page_v2.html</code> (the updated template).
2. Use a suitable tool to generate a unified diff file that shows the changes between <code>status_page_v1.html</code> and <code>status_page_v2.html</code>. 
   <ul>
     <li>Name the diff file <code>/home/user/uptime_check/status_page.patch</code>.</li>
     <li>The diff must be in unified format (lines should begin with <code>@@</code> for chunks, <code>+</code> for additions, and <code>-</code> for removals, and start with <code>---</code> and <code>+++</code> headers).</li>
     <li>The filename headers in the patch must use the relative filenames <code>status_page_v1.html</code> and <code>status_page_v2.html</code>.</li>
   </ul>
3. Next, create a backup of <code>status_page_v1.html</code> and name it <code>status_page_v1_backup.html</code> in the same directory.
4. Apply the patch (<code>status_page.patch</code>) to the original file (<code>status_page_v1.html</code>), so that it becomes identical to <code>status_page_v2.html</code>.
5. Finally, verify your work by generating a log file at <code>/home/user/uptime_check/patch_verification.log</code> containing:
   <ul>
     <li>The output of the <code>diff -u status_page_v1.html status_page_v2.html</code> command after the patch was applied (should be empty if the patch was correctly applied).</li>
     <li>If the output is empty, the log file must contain only the line: <br><code>Patching successful: Files are identical after patch application.</code></li>
     <li>If there are any differences, output those differences in the log file.</li>
   </ul>
