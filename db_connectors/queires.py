import pandas as pd

# Sample data
data = [
    {
        "gerrit": "54675647",
        "joblink": "http://ci.example.com/job/12345",
        "status": "RUNNING",
        "submission time": "2025-04-30 10:00:00",
        "project": "example-project",
        "branch": "main"
    },
    {
        "gerrit": "12345",
        "joblink": "http://ci.example.com/job/12345",
        "status": "RUNNING",
        "submission time": "2025-04-30 10:00:00",
        "project": "example-project",
        "branch": "main"
    },
    {
        "gerrit": "234556",
        "joblink": "http://ci.example.com/job/12345",
        "status": "RUNNING",
        "submission time": "2025-04-30 10:00:00",
        "project": "example-project",
        "branch": "main"
    },
    {
        "gerrit": "12346",
        "joblink": "http://ci.example.com/job/12346",
        "status": "QUEUED",
        "submission time": "2025-04-30 11:00:00",
        "branch": "dev"
    },
    {
        "gerrit": "23421",
        "joblink": "http://ci.example.com/job/12346",
        "status": "QUEUED",
        "submission time": "2025-04-30 11:00:00",
        "branch": "dev"
    },
    {
        "gerrit": "34545",
        "joblink": "http://ci.example.com/job/12346",
        "status": "QUEUED",
        "submission time": "2025-04-30 11:00:00",
        "branch": "dev"
    },
]

# Create DataFrame
df = pd.DataFrame(data)

def temp():
    return df
