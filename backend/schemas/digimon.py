from pydantic import BaseModel


class SkillSchema(BaseModel):
    id: int
    name: str
    description: str | None = None


class FieldSchema(BaseModel):
    id: int
    name: str
    image: str | None = None


class EvolutionSchema(BaseModel):
    id: int
    name: str
    image: str
    condition: str | None = None


class DigimonListItem(BaseModel):
    id: int
    name: str
    image: str
    level: str | None = None
    attribute: str | None = None


class DigimonDetail(BaseModel):
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
    current_page: int
    total_pages: int
    total_elements: int
    has_next: bool
    has_previous: bool


class DigimonListResponse(BaseModel):
    content: list[DigimonListItem]
    pagination: PaginationInfo
