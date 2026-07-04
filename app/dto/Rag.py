from typing import Any

from pydantic import BaseModel, Field


class IngestPathRequest(BaseModel):
    path: str = Field(min_length=1)


class IngestPathResponse(BaseModel):
    ingested: int
    skipped: int


class QueryRequest(BaseModel):
    question: str = Field(min_length=1)


class SourceItem(BaseModel):
    id: str
    text: str
    score: float
    metadata: dict[str, Any] | None = None


class QueryResponse(BaseModel):
    answer: str
    sources: list[SourceItem]

