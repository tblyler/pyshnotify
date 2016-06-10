# pyshnotify
[Weechat](https://weechat.org) shell executions from notifications

## Installation and Usage
1. `curl https://raw.githubusercontent.com/tblyler/pyshnotify/master/pyshnotify.py > "${HOME}/.weechat/python/autoload/pyshnotify.py`
2. If Weechat is running you can load the plugin with `/python reload`
3. Set the command to run with `/set plugins.var.python.pyshnotify.command "curl example.com/{{buffer_name}}/{{msg}}"`
