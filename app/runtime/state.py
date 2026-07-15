from enum import Enum

class RequestState(Enum):
    RECEIVED = "received"
    PLANNING ="planning"
    EXECUTING = "executing"
    VERIFYING = "verifying"
    COMPLETED = "completed"
    FAILED = "failed"
    