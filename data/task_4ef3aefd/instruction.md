You are managing a set of microservice containers and need to extract the names and images of the running containers from a simulated status file for documentation purposes. The file <code>/home/user/logs/service_status.log</code> contains lines in the following format: <br/>
<code>container_id: &lt;id&gt;; name: &lt;name&gt;; image: &lt;image&gt;; status: &lt;status&gt;</code><br/>
For all lines in <code>/home/user/logs/service_status.log</code> with <code>status: running</code>, extract the <code>name</code> and <code>image</code> fields, and write them into a new file <code>/home/user/logs/running_containers.csv</code>.<br/><br/>
The output CSV file should NOT contain a header and each line must strictly follow the format:<br/>
<code>&lt;name&gt;,&lt;image&gt;</code><br/>
For example:<br/>
<code>api-service,micro/api:latest</code><br/>
<code>web-front,company/web:1.2</code><br/>
Only containers with a <code>status</code> of <code>running</code> should be included in the CSV. Make sure there are no extra spaces before or after the commas or the fields. The resulting file must reside at <code>/home/user/logs/running_containers.csv</code> after completion.
