import uuid
from datetime import datetime
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import(
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    JSON,
    func
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ticket(Base):
    _tablename_ = "tickets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(200), nullable = False)
    message: Mapped[str] = mapped_column(Text, nullable = False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    priority: Mapped[str] = mapped_column(String(20), nullable = False)
    status: Mapped[str] = mapped_column(String(20), nullable = False, default = "open")
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone =True), server_default=func.now())

class Document(Base):
    _tablename = "documents"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True), primary_key = True,
        default = uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), nullable = False)
    content_hash: Mapped[str] =mapped_column(
        String(64), nullable = False, unique = True
    )
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone = True), server_default = func.now()
    )

class DocumentChunk(Base):
    _tablename_ = "documents_chunks"

    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True), primary_key = True,
        default = uuid.uuid4
    )
    document_id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True), 
        ForeignKey("documents.id", ondelete = "CASCADE"),
        nullable = False,
        index = True
    )
    chunk_index: Mapped[int] = mapped_column(
        Integer, nullable = False
    )
    content : Mapped[str] = mapped_column(
        Text, nullable = False
    )
    embedding : Mapped[Any | None] = mapped_column(
        Vector(), nullable = True
    )


class AIRun(Base):
    _tablename_ = "ai_runs"

    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid= True),
        ForeignKey("tickets.id", ondelete = "CASCADE"),
        nullable = False,
        index = True
    )
    prompt_version: Mapped[str] = mapped_column(
        String(50), nullable = False
    )
    trace : Mapped[dict] = mapped_column(
        JSON, nullable = False, default = dict
    )
    duration_ms: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), server_default = func.now()
    )

class DraftReview(Base):
    _tablename_ = "draft_reviews"

    id :  Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid = True),
        ForeignKey("ai_runs.id", ondelete = "CASCADE"),
        nullable = False,
        unique = True
    )
    original_draft : Mapped[str] = mapped_column(
        Text, nullable = False
    )
    final_response: Mapped[str | None] = mapped_column(
        Text
    )
    decision : Mapped[str] = mapped_column(
        String(20), nullable = False, default = "pending"
    )
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timeozone = True), server_default = func.now()
    )
