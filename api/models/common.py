from pydantic import BaseModel
from enum import Enum

class Todo(BaseModel):
    title: str
    description: str

class Fleet(str, Enum):
    M501D = "501D"
    M501F = "501F"
    M501G = "501G"
    M501J = "501J"
    M701D = "701D"
    M701F = "701F"
    M701G = "701G"
    M701J = "701J"

class Parts(str, Enum):
    NZL = "NZL"
    BAS = "BAS"
    TRA = "TRA"
    TRS = "TRS"
    T1C = "T1C"
    T2C = "T2C"
    T3C = "T3C"
    T4C = "T4C"
    T1S = "T1S"
    T2S = "T2S"
    T3S = "T3S"
    T4S = "T4S"
    RS1 = "RS1"
    RS2 = "RS2"
    RS3 = "RS3"
    RS4 = "RS4"

class UseKBN(str, Enum):
    STD = "STD"
    OTHER = "OTHRE"

class Clasify(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    undeterminable = "undeterminable"