from dataclasses import dataclass
from typing import Dict, List

from pilot.model.base import WorkerApplyType
from pilot.model.parameter import WorkerType
from pilot.scene.base_message import ModelMessage
from pydantic import BaseModel

WORKER_MANAGER_SERVICE_TYPE = "service"
WORKER_MANAGER_SERVICE_NAME = "WorkerManager"


class PromptRequest(BaseModel):
    messages: List[ModelMessage]
    model: str
    prompt: str = None
    temperature: float = None
    max_new_tokens: int = None
    stop: str = None
    echo: bool = True
    span_id: str = None


"""
上面的代码这样定义类是基于面向对象编程的原则和封装的思想。
通过这种方式，代码能够更清晰地表示现实世界中的实体和它们的属性。

PromptRequest类只是一个用于保存数据的类，而不需要任何特定的行为或操作。
或者，方法的实现可能在BaseModel类中，因为PromptRequest继承自BaseModel，
所以如果BaseModel中定义了方法，PromptRequest会继承这些方法。
"""


class EmbeddingsRequest(BaseModel):
    model: str
    input: List[str]
    span_id: str = None


class WorkerApplyRequest(BaseModel):
    model: str
    apply_type: WorkerApplyType
    worker_type: WorkerType = WorkerType.LLM
    params: Dict = None
    apply_user: str = None


class WorkerParameterRequest(BaseModel):
    model: str
    worker_type: WorkerType = WorkerType.LLM


class WorkerStartupRequest(BaseModel):
    host: str
    port: int
    model: str
    worker_type: WorkerType
    params: Dict
