from enum import Enum

from robot_interface.models.mission.status import MissionStatus, StepStatus


class ExrMissionStatus(str, Enum):
    StartRequested = "START_REQUESTED"
    PauseRequested = "PAUSE_REQUESTED"
    ResumeRequested = "RESUME_REQUESTED"
    Rejected = "REJECTED"
    WakingUp = "WAKING_UP"
    Starting = "STARTING"
    InProgress = "IN_PROGRESS"
    Paused = "PAUSED"
    Completed = "COMPLETED"
    ResetRequested = "RESET_REQUESTED"

    def to_mission_status(self) -> MissionStatus:
        return {
            ExrMissionStatus.StartRequested: MissionStatus.NotStarted,
            ExrMissionStatus.PauseRequested: MissionStatus.InProgress,
            # Current implementation paused is cancelled
            ExrMissionStatus.ResumeRequested: MissionStatus.Cancelled,
            ExrMissionStatus.Rejected: MissionStatus.Failed,
            ExrMissionStatus.WakingUp: MissionStatus.NotStarted,
            ExrMissionStatus.Starting: MissionStatus.NotStarted,
            ExrMissionStatus.InProgress: MissionStatus.InProgress,
            ExrMissionStatus.Paused: MissionStatus.Cancelled,
            ExrMissionStatus.Completed: MissionStatus.Successful,
            ExrMissionStatus.ResetRequested: MissionStatus.Cancelled,
        }[self]


class ExrStepStatus(str, Enum):
    StartRequested = "START_REQUESTED"
    PauseRequested = "PAUSE_REQUESTED"
    ResumeRequested = "RESUME_REQUESTED"
    Rejected = "REJECTED"
    WakingUp = "WAKING_UP"
    Starting = "STARTING"
    InProgress = "IN_PROGRESS"
    Paused = "PAUSED"
    Completed = "COMPLETED"
    ResetRequested = "RESET_REQUESTED"

    def to_step_status(self) -> StepStatus:
        return {
            ExrStepStatus.StartRequested: StepStatus.NotStarted,
            ExrStepStatus.PauseRequested: StepStatus.InProgress,
            ExrStepStatus.ResumeRequested: StepStatus.Cancelled,
            ExrStepStatus.Rejected: StepStatus.Failed,
            ExrStepStatus.WakingUp: StepStatus.NotStarted,
            ExrStepStatus.Starting: StepStatus.NotStarted,
            ExrStepStatus.InProgress: StepStatus.InProgress,
            ExrStepStatus.Paused: StepStatus.Cancelled,
            ExrStepStatus.Completed: StepStatus.Successful,
            ExrStepStatus.ResetRequested: StepStatus.Cancelled,
        }[self]
