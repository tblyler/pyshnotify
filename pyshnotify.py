import weechat as w
import shlex, subprocess

SCRIPT_NAME    = "pyshnotify"
SCRIPT_AUTHOR  = "Tony Blyler <tony@blyler.cc>"
SCRIPT_VERSION = "1.0"
SCRIPT_LICENSE = "MPL2"
SCRIPT_DESC    = "Execute command from highlights and private messages"

def on_msg(data, buffer, timestamp, tags, displayed, highlight, sender, message):
    if data == "private" or int(highlight) or w.buffer_get_string(buffer, "localvar_type") == "private":
        buffer_name = w.buffer_get_string(buffer, "name")
        cmd = w.config_get_plugin("command")
        if not cmd:
            return w.WEECHAT_RC_OK

        cmd = cmd.replace("{{buffer_name}}", buffer_name).replace("{{msg}}", message)

        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode != 0:
            w.prnt("", w.prefix("error") + " Unable to run command: '" + cmd + "' stdout: '" + stdout + "' stderr: '" + stderr + "'")
            return w.WEECHAT_RC_ERROR

    return w.WEECHAT_RC_OK

if __name__ == "__main__" and w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
    w.config_set_desc_plugin("command", "Shell command to execute {{buffer_name}} and {{msg}} will be replaced per message")
    if not w.config_get_plugin("command"):
        w.config_set_plugin("command", "")
    w.hook_print("", "irc_privmsg", "", 1, "on_msg", "")
