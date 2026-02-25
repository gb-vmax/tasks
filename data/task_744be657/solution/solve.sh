#!/bin/bash
set -e
cd /home/user

jq '
  (has("articles") and (.articles | type=="array") and 
    all(.articles[]?; 
      (type=="object" and
       (.id|type)=="number" and (.title|type)=="string" and
       (.author|type)=="string" and (.published|type)=="boolean"))) 
' /home/user/docs/articles.json | grep -qxF "true" && 
( jq '[.articles[]|{title,author}]' /home/user/docs/articles.json > /home/user/docs/article_summaries.json && echo "SCHEMA VALID" > /home/user/docs/validation.log ) || 
echo "INVALID SCHEMA" > /home/user/docs/validation.log
sudo apt-get update && sudo apt-get install -y jq
jq '
  (has("articles") and (.articles | type=="array") and 
    all(.articles[]?; 
      (type=="object" and
       (.id|type)=="number" and (.title|type)=="string" and
       (.author|type)=="string" and (.published|type)=="boolean"))) 
' /home/user/docs/articles.json | grep -qxF "true" && 
( jq '[.articles[]|{title,author}]' /home/user/docs/articles.json > /home/user/docs/article_summaries.json && echo "SCHEMA VALID" > /home/user/docs/validation.log ) || 
echo "INVALID SCHEMA" > /home/user/docs/validation.log
cat /home/user/docs/validation.log
cat /home/user/docs/article_summaries.json
