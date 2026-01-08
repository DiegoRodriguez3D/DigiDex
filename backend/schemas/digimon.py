from pydantic import BaseModel


class SkillSchema(BaseModel):
    """A Digimon skill/attack."""
    id: int
    name: str
    description: str | None = None


class FieldSchema(BaseModel):
    """A Digimon field (Nature Spirits, Dragon's Roar, etc.)."""
    id: int
    name: str
    image: str | None = None


class EvolutionSchema(BaseModel):
    """An evolution (prior or next) for a Digimon."""
    id: int
    name: str
    image: str
    condition: str | None = None


class DigimonListItem(BaseModel):
    """Simplified Digimon data for grid display."""
    id: int
    name: str
    image: str
    level: str | None = None
    attribute: str | None = None


class DigimonDetail(BaseModel):
    """Full Digimon detail for the analyzer view."""
    id: int
    name: str
    image: str
    level: str | None = None
    attribute: str | None = None
    types: list[str] = []
    description: str | None = None
    skills: list[SkillSchema] = []
    fields: list[FieldSchema] = []
    prior_evolutions: list[EvolutionSchema] = []
    next_evolutions: list[EvolutionSchema] = []


class PaginationInfo(BaseModel):
    """Pagination metadata."""
    current_page: int
    total_pages: int
    total_elements: int
    has_next: bool
    has_previous: bool


class DigimonListResponse(BaseModel):
    """Paginated list response."""
    content: list[DigimonListItem]
    pagination: PaginationInfo
