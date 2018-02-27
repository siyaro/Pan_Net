Configure rsyslog service with the following settings:
  ● logging of default log files from /var/log/*
  ● logging of custom log files

This is done by Ansible. I used user prompt messages to use propper tasks to accomplish:

  ● logging only default log files
  ● logging custom files
  ● selecting external log server to send logs to
