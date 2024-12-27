---
title: Discord-RPC
date: 2021-12-13
summary: An Python wrapper for Discord RPC
description: An Python wrapper for Discord RPC
toc: true
readTime: false
autonumber: false
math: true
tags:
  - projects
  - python
  - discord-rpc
showTags: true
hideBackToTop: false
hidePagination: true
draft: false
---

# Discord RPC
An Python wrapper for Discord RPC API. Allow you to make own custom RPC.
# Install
- PyPI
```
pip install discord-rpc
```

# Quick example
```py
import discordrpc

rpc = discordrpc.RPC(app_id=12345678910)

rpc.set_activity(
      state="A super simple rpc",
      details="simple RPC"
    )

# Required if you only run Discord RPC on this file or current instance.
rpc.run()
```
`rpc.run()` is only used if you are only running Discord RPC on the current file/instance. If there are other programs/tasks on the current instance, `rpc.run()` does not need to be used.

See documentation [here](https://github.com/Senophyx/Discord-RPC/blob/main/DOCS.md).<br>
More examples [here](https://github.com/Senophyx/discord-rpc/tree/main/examples).


# Change Logs

## 5.1

**Updates :**
- Added [Activity Types](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-types) (Listening, Watching, etc).
```py
rpc.set_activity(act_type=0)
```
- Added more detailed information in the output.

## 5.0

**Critical updates & changes :**

- Inputting id is no longer in `RPC.set_id`. Replaced with inputing inside `RPC` class.

Before:

```py
rpc = discordrpc.RPC.set_id(app_id=1234567890)
```

After:

```py
rpc = discordrpc.RPC(app_id=1234567890)
```

**Updates :**
- Removing many functions. List:
  - `RPC.set_id`
  - `RPC._connect`
  - `RPC._write`
  - `RPC._recv`
  - `RPC._recv_exact`
  - And many more...

- Package `logging` is used again as output.
- Removing `timestamp` argument and added `ts_start` and `ts_end` on `set_activity()` as a replacement for the timestamp argument.
- Added `debug` parameter on `RPC` class if you want to print more outputs.
- `timestamp` variable is moved to `discordrpc.utils`. So if you want to import timestamp variable, use
  ```py
  from discordrpc.utils import timestamp
  ```
- `button` on `discordrpc.button` changed to `Button`.
- added `date_to_timestamp` function on `discordrpc.utils`. with format `%d/%m/%Y-%H:%M:%S` or `day/month/year-hour:minute:second`
  Example :
  ```py
  date_to_timestamp('14/06/2025-00:00:00')
  ```
  

## 4.0

**Critical update :**
- Changing `DiscordRPC` folder (when you import the package) to `discordrpc`.
Before :
```py
import DiscordRPC
```
After :
```py
import discordrpc
```

**Updates :**
- No longer using `logging` package.
- `GCAR` or `get_current_application_running` removed because it can't be cross-platform (I spent days just looking for this solution lmao).
- `setLoggerEnabled()` function removed.
- `Set_ID` changed to `set_id`.
- `output()` function changed to `show_output` variable, [Example](https://github.com/LyQuid12/Discord-RPC/blob/main/examples/print-rpc-output.py#L5).
- Shorten the code in `presence.py` (not that much though).

## 3.0

**New & Updates :**
- Added `GCAR` method. GCAR : Get Current Application Running. Basically, you can switch your rpc status (state/details) automatically to the application you're running

## 2.0

**New & Updates :**
- Added button (Example [here](https://github.com/LyQuid12/discord-rpc/blob/main/examples/rpc-with-button.py))
- RPC output (Example [here](https://github.com/LyQuid12/discord-rpc/blob/main/examples/print-rpc-output.py))
- RPC still running even though "large_text" and "small_text" are not set
- The message when RPC is running successfully is now working fine, and an error will appear if the RPC is not set properly