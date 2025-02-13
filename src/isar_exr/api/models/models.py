from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from isar_exr.api.models.enums import ChargerType, ChargingState


class Point3DInput(BaseModel):
    x: float
    y: float
    z: float


class QuaternionInput(BaseModel):
    x: float
    y: float
    z: float
    w: float


class Pose3DInput(BaseModel):
    position: Point3DInput
    orientation: QuaternionInput


class Pose3DStampedInput(BaseModel):
    timestamp: int
    frameID: str
    position: Point3DInput
    orientation: QuaternionInput


class PointOfInterestTypeEnum(str, Enum):
    MANOMETER = "MANOMETER"
    FIRE_EXTINGUISHER = "FIRE_EXTINGUISHER"
    GENERIC = "GENERIC"


class PointOfInterestActionPhotoInput(BaseModel):
    robotPose: Pose3DInput
    sensor: str


class PointOfInterestActionVideoInput(BaseModel):
    robotPose: Pose3DInput
    sensor: str
    duration: float


class AddPointOfInterestInput(BaseModel):
    name: str
    customerTag: Optional[str] = None
    site: str
    frame: str
    type: PointOfInterestTypeEnum = Field(default=PointOfInterestTypeEnum.GENERIC)
    pose: Pose3DInput
    photoAction: Optional[PointOfInterestActionPhotoInput] = None
    videoAction: Optional[PointOfInterestActionVideoInput] = None


class PointOfInterestByCustomerTag(BaseModel):
    customerTag: str
    siteId: str


class RobotTypeEnum(str, Enum):
    SPOT = "SPOT"
    EXR2 = "EXR2"
    ROVER = "ROVER"
    DJI_DRONE = "DJI_DRONE"


class PointOfInterestProducerTypeEnum(str, Enum):
    ROBOT_TEACHING = "ROBOT_TEACHING"
    VISUAL_MARKER = "VISUAL_MARKER"
    MANUAL_IMPORT = "MANUAL_IMPORT"


class PointOfInterestProducerInput(BaseModel):
    type: PointOfInterestProducerTypeEnum = Field(
        default=PointOfInterestProducerTypeEnum.MANUAL_IMPORT
    )
    robotNumber: int
    robotType: RobotTypeEnum = Field(default=RobotTypeEnum.EXR2)


class UpsertPointOfInterestInput(BaseModel):
    key: str
    name: str
    type: PointOfInterestTypeEnum = Field(default=PointOfInterestTypeEnum.GENERIC)
    siteId: str
    pose: Pose3DStampedInput
    producer: PointOfInterestProducerInput
    inspectionParameters: dict


class BatteryStatusType(BaseModel):
    percentage: float
    chargingState: ChargingState
    chargerType: ChargerType
    chargingCurrent: float
