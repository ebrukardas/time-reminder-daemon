Windows (Using Task Scheduler)

Steps:
1 Save the script as time_announcer.py in a permanent location
(e.g., C:\scripts\time_announcer.py).

    2 Use pythonw.exe (runs without opening a terminal). Find its path using:
        $ where pythonw

    3 Create a Task in Task Scheduler:
        - Open Task Scheduler (Win + R, then type taskschd.msc).
        - Click Create Basic Task.
        - Name: Time Announcer.
        - Trigger → Choose At log on.
        - Action → Choose Start a Program.
        - Program/Script:
            $ C:\Path\To\pythonw.exe
        - Add arguments:
            $ C:\scripts\time_announcer.py
        - Finish and enable Run whether user is logged in or not.
    4 Test the Task:
        - Right-click the task and click Run.
        - Check if the voice announces the time.
